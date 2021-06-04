# seleniumbase-interview
Take home project test for seleniumbase.io & python. For more on the pytest webdriver framework reference: www.seleniumbase.io

---
# Fork this project and create a pull request to this repository
---
# Pre-requisites
Having the following installed

python
pip
seleniumbase.io
Selenium base has good documentation how to install python, pip and sbase here (This will also take care of all webdriver needs) https://seleniumbase.io/help_docs/install_python_pip_git/

# Install

From there you can install seleniumbase with pip: pip install seleniumbase

# The project
Use the demo website: https://www.saucedemo.com/ to login and write test cases for each of folliwing three user scenarios. (password: `secret_sauce` for each user)

```
users:

* standard_user
* locked_out_user
* problem_user
```

# Run the automation
Write automated test cases for the three users in the MyTestClass(BaseCase):
```
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://www.saucedemo.com/")
        
    # standard user


    # locked_out_user


    # problem_user
```

How to run the test file
`pytest sbaseTest.py`


Output

![Alt text](output.png?raw=true "Output")