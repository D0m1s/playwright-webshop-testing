# Website test automation with Playwright

## Before running
1. Install [Python](https://www.python.org/downloads/)
2. Install Pytest: `pip install pytest`
3. Install Playwright: `pip install pytest-playwright`
4. Install required browsers: `playwright install`

## How to run
- Headless: `pytest`
- Headed with 500ms delay between actions: `pytest --headed --slowmo 500`

## [Test Case](test_case.md)