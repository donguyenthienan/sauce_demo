# Precondition
    1. Install Python 3.8
    2. Install libraries in requirements.txt file by command "python install -r requirements.txt"

# Execution
1. Run all test cases in 'TestCases' folder by ...
2. Run all test cases in 'TestSuites' folder by ...

# Framework coverage
1. Run testcases on Chrome, Firefox, Safari

2. Perform running in parallel

3. Get Test Data from JSON,CSV,Property file

4. Generate html report on specific folder named by the running time

5. Generate log file on specific folder named by the running time

# Framework structure
## 'Drivers' folder
    Include required browser driver
## 'Locators' folder
    Include locators of web elements of each specific pages
## 'Objects' folder
    Include objects that used in test case (login account, product item, ...)
## 'Pages' folder
    Include methods describe actions in specific page (Ex: In Login page, we have method 'login')
## 'TestCases' folder
    Include implemented test cases files (.py)
## 'TestSuites' folder
    Include test suites files that include many test cases in each file
## 'Utils' folder
    Include methods for common actions that can be used anytime when implementing. Ex:Methods for formatting string, analyzing email,....
## .gitignore file
    