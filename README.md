# Email Processor

Simple Python project that validates, cleans, and splits emails into username/domain with structured logging and full test coverage.

### Features
- Regex validation
- Clean + split transformation
- Orchestration function `orchestrate_email_processing()`
- Logging to file + console
- pytest tests

### Run
source venv/bin/activate
python -m app.processor

### Test
pytest -v
