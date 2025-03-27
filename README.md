This is a Sample project that I created to show QA Automation using Playwright, Python, Pytest and Github Actions. 
A demo website "https://www.saucedemo.com/" is used to implement different type of test cases, that run Auto with Github on every code push.

PLAYWRIGHT-PYTHON-TESTS/
│── tests/                 # Main test folder
│   ├── test_example.py    # Sample test file
│   ├── test_login.py      # (New) Separate login test file
│   ├── conftest.py        # (New) Pytest setup for Playwright fixtures
│   ├── pages/             # Page Object Model (POM) files
│   │   ├── login_page.py  # (New) Page Object for login
│   ├── utils/             # Utility functions
│   │   ├── helpers.py     # (New) Helper functions (if needed)
│── reports/               # Test reports
│── playwright.config.py   # (Optional) Playwright config file
│── requirements.txt       # Python dependencies
│── .gitignore             # Ignore unnecessary files
│── README.md              # Project documentation

  •	Fixtures (@pytest.fixture) for reusability
  •	Parametrization (@pytest.mark.parametrize) to test multiple cases
  •	Setup & teardown methods (conftest.py)

- Instead of writing locators inside test files, we create a Page Object Model (POM).
	•	Keeps tests clean and readable.
	•	Makes it easy to reuse login logic across multiple tests.
        Keeps test scripts clean – No need to repeat locators in every test.
        Increases maintainability – If a button’s locator changes, update it in one place.
        Makes test cases readable – Test scripts only contain logic, not detailed locators.
		Reduce duplicate code in test files
		Ensures easy updates if the UI changes

- Refactored Test to Use LoginPage (test_login.py)
	•	Uses LoginPage class for better code structure.
	•	Easier to maintain and expand (e.g., adding logout tests).

- Added conftest.py for Pytest Fixtures
	•	Provides a fresh browser session for each test.
	•	Automatically closes the browser after the test.
	•	Works across all tests without needing to redefine page in every test file.
