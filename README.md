In project used:
- Selenium
- Pytest
- Allure
- pytest-rerunfailures
- pytest-failed-screenshot
- Selenoid

python -m pytest -v -q --browser=chrome --reruns 2 --screenshot=on --alluredir=allure-results

This command will run tests and create report, if test failed - it will restart twice. In report will be screenshot of failed steps.
