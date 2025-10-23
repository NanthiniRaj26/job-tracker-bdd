# 🧪 Job Tracker BDD Automation

This project automates job search on [Naukri.com](https://www.naukri.com) using **Python**, **Selenium**, and **Behave (BDD)**. It searches for roles like *Python Selenium Tester* in a given location, extracts job listings, and saves them to a CSV file — all with screenshots and clean folder structure.

---

## 🔍 What It Does

- Launches Edge browser using Selenium
- Searches Naukri.com for jobs by role and location
- Extracts job title, company name, location, and description
- Saves results to a timestamped CSV file
- Captures screenshots at each step for documentation

---

## 📁 Folder Structure


```
job-tracker-bdd/
├── features/
│   ├── job_search.feature
│   └── steps/
│       ├── job_steps.py
│       ├── results/         # Auto-created for CSV output
│       └── screenshots/     # Auto-created for screenshots
├── environment.py
├── requirements.txt
├── README.md
```

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the test:
    behave

📂 CSV files will be saved in features/steps/results/
🖼️ Screenshots will be saved in features/steps/screenshots/


🛠 Technologies Used
- Python 3.x
- Selenium WebDriver
- Behave (BDD Framework)
- Edge Browser Automation
- CSV and Screenshot Logging

👩‍💻 Built By
Nanthini — Python Automation Learner
🎓 AJR Institute, Tambaram
📍 Chennai, India

📌 Future Enhancements
- Add job experience and posted date
- Export to Excel or JSON
- Integrate with Power BI dashboard
- Deploy as a web app using Django


📣 Feedback & Support
If you found this project helpful, feel free to ⭐ star the repo and share your thoughts.
For suggestions or collaboration, reach out via LinkedIn or GitHub Issues.

---
