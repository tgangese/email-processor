
![Python Tests](https://github.com/tgangese/email-processor/actions/workflows/python-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# Email Processor

Simple but production-ready Python project that validates, cleans, and splits emails into `username` / `domain` with structured logging and full pytest coverage.

### ✨ Features
- **Regex validation** - rejects invalid formats before processing
- **Clean + split** - trims, lowercases, and splits into `username`, `domain`, `cleaned_email`
- **Orchestration** - `orchestrate_email_processing()` handles validation -> transformation -> logging
- **Structured Logging** - logs to `logs/app.log` + console (INFO, WARNING, ERROR)
- **Loop until valid** - keeps asking until you enter a valid email or `q`
- **Tests** - 5 pytest cases, run automatically by GitHub Actions

### 📁 Structure

email-processor/
├── app/
│ ├── init.py
│ └── processor.py # core logic
├── tests/
│ └── test_processor.py
├── logs/
│ └── app.log
├── .github/workflows/python-tests.yml
├── requirements.txt
└── README.md

###  Run
```bash
# create venv (Linux)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python -m app.processor
# or unbuffered: python -u -m app.processor

# Try:
# gangeseterkulagmail.com -> ❌ Invalid, try again
# gangesefelixt@gmail.com -> ✅ Valid! {'username': 'gangesefelixt', ...}

✅ Test
Bash
pytest -v
# 5 passed