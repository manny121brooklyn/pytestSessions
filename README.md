
## To execute the tests from a specific file, use the 
## following syntax −

pytest <filename> -v
pytest test_compare.py -v


## To execute the tests containing a string in its name we can use the following syntax −

pytest -k <substring> -v
pytest -k great -v

def test_greater():
num = 100
assert num > 100
assert 100 > 100

## Markers 
# Pytest allows us to use markers on test functions. 
# Markers are used to set various features/attributes to test functions.

# Markers are applied on the tests using the syntax given below −
@pytest.mark.<markername>

test_compare.py
import pytest
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

# Now to run the tests marked as others, run the following command −
pytest -m others -v
# Run tests marked great stored in pytest_scripts folder
pytest -m great pytest_scripts
# or
py.test -m great pytest_scripts

# Run run only test cases marked with login marker in test_demo.py file under pytest_scripts folder
pytest pytest_scripts/test_demo.py -m login
# or
py.test pytest_scripts/test_demo.py -m login

## To run several test cases in one file in parallel use pytest xdist plugin
# How to install xdist plugin: 
pip install pytest-xdist
# Syntax
# run 5 test methods in test_webpage_login.py from pytest_scripts folder
pytest -n 5  pytest_scripts/test_webpage_login.py

## Pytest html report installation 
pip install pytest-html 

## Then run the command: 
pytest --html=report.html

## Run the command to save report in a seperate folder 
pytest -vs pytest_scripts/test_google.py --html=reports/google_test_report.html

# Explanation
Run file test_google.py from pytest_scripts folder and generate html report 
google_test_report.html and save under reports folder

