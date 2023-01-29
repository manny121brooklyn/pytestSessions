
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

