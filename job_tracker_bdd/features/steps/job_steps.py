from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, datetime, os, csv

# 📸 Screenshot helper
def take_screenshot(driver, label):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join("screenshots", f"{label}_{timestamp}.png")
    driver.save_screenshot(path)
    print(f"[SCREENSHOT] Saved: {path}")

# 🌐 Step 1: Launch browser
@given('I launch the Edge browser')
def step_launch_browser(context):
    options = Options()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.driver = webdriver.Edge(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

# 🏠 Step 2: Open job portal
@when('I open the job portal')
def step_open_portal(context):
    try:
        context.driver.set_page_load_timeout(60)
        context.driver.get("https://www.naukri.com")
        take_screenshot(context.driver, "naukri_home")
    except Exception as e:
        print("[ERROR] Failed to open portal:", e)
        take_screenshot(context.driver, "portal_error")
        context.driver.quit()
        assert False, "Portal did not load"

# 🔍 Step 3: Search for job
@when('I search for "{role}" in "{location}"')
def step_search_job(context, role, location):
    try:
        take_screenshot(context.driver, "before_typing")

        role_box = WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter skills / designations / companies']"))
        )
        role_box.clear()
        role_box.send_keys(role)

        loc_box = WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter location']"))
        )
        loc_box.clear()
        loc_box.send_keys(location)

        search_btn = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "qsbSubmit"))
        )
        search_btn.click()

        time.sleep(3)
        take_screenshot(context.driver, "search_results")
    except Exception as e:
        print("[ERROR] Search failed:", e)
        take_screenshot(context.driver, "search_error")

# 📄 Step 4: Validate and export results
@then('I should see a list of job results')
def step_validate_results(context):
    try:
        take_screenshot(context.driver, "before_extracting_jobs")

        jobs = WebDriverWait(context.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'srp-jobtuple-wrapper')]"))
        )
        print(f"[DEBUG] Total job cards found: {len(jobs)}")

        # 📁 Create results folder in current working directory
        results_path = os.path.join(os.getcwd(), "results")
        os.makedirs(results_path, exist_ok=True)

        # 🕒 Create timestamped CSV file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(results_path, f"job_results_{timestamp}.csv")

        # 📝 Write job data to CSV
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Location", "Description"])

            for job in jobs[:10]:
                try:
                    title = job.find_element(By.CLASS_NAME, "title").text if job.find_elements(By.CLASS_NAME, "title") else "N/A"
                    company = job.find_element(By.CLASS_NAME, "companyName").text if job.find_elements(By.CLASS_NAME, "companyName") else "N/A"
                    location = job.find_element(By.CLASS_NAME, "location").text if job.find_elements(By.CLASS_NAME, "location") else "N/A"
                    description = job.find_element(By.CLASS_NAME, "job-desc").text if job.find_elements(By.CLASS_NAME, "job-desc") else "N/A"
                    writer.writerow([title, company, location, description])
                    print(f"🔹 {title} at {company} ({location})")
                except Exception as e:
                    print("[WARN] Skipped one job card due to error:", e)

        print(f"[CSV] Saved: {filename}")
        print(f"[CHECK] CSV file exists? {os.path.exists(filename)}")
        take_screenshot(context.driver, "job_listings")

    except Exception as e:
        print("[ERROR] No job results found:", e)
        take_screenshot(context.driver, "no_results")
    finally:
        context.driver.quit()