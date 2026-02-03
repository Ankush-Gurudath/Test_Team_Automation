# Introduction

## About

This is UI web Automation project.

Language used: ```Python```

Framework used: ```Pytest``` with ```Cucumber```

Environment we are running: ```int```, ```stg```, ```prod```

Browser supported: ```Chrome```, ```Firefox```, ```Edge```, ```Safari```

Cloud platform: ```Browserstack```

CICD: ```Jenkins```



# Setup

## pre-request:

1. Install Python 3 or latest version of Python on your machine.
You can download the latest version of python from [here](https://www.python.org/downloads/)

2. Install Git on your machine.
You can download the git from [here](https://git-scm.com/downloads)

3. Install allure on your machine
- [For allure installation in windows](https://allurereport.org/docs/install-for-windows)
- [For allure installation in Mac](https://allurereport.org/docs/install-for-macos/)


**Verify pre-request:**

***Open new terminal or command prompt and check below***

Give below command to check whether python version is showing correctly or not

```python3 --version```


Give below command to check whether pip version is showing or not

```pip3 --version```


Give below command to check whether git command was working or not

```git --version```


Give below command to check whether allure command working or not

```allure --version```



## Repository Details

### Repository link

https://github.com/lytx-qa/web-automation


### Directories in repository:

```browserstack``` ***- This directory has browserstack config and yaml***

```data``` ***- This directory has all test data files for int, stg and prod***

```features``` ***- This directory has all cucumber feature files***

```locators``` ***- This directory has files which has locators***

```pages``` ***- This different has page classes and its methods***

```properties``` ***- This directory has properties/configuration of automation for int, stg and prod***

```results``` ***- This directory is used to store results***

```steps``` ***- This directory has all step test files***

```utils``` ***- This directory has classes and its methods required for utilities***


**Use below command to clone**

Open terminal or command prompt and go to directory where you want to clone the repository

```git clone https://github.com/lytx-qa/web-automation.git```


**Follow below steps to setup and run:**

Move inside the repository

```cd web-automation```


Use below command to install all required dependencies

```pip install -r requirements.txt```


Use below command to run the test

```pytest steps/<Give the test file which we wanted to run>```

Eg:

```pytest steps/test_localization_english.py```


Use `--browser` in command to run on required browser

```pytest steps/<Give the test file which we wanted to run> --browser=<browserName>```

Eg:
```pytest steps/test_localization_english.py --browser=chrome``` 



Use `--env` in command to run on automation on required environment

```pytest steps/<Give the test file which we wanted to run> --env=<environmentName>```

Eg:

```pytest steps/test_localization_english.py --env=stg```


### To run on browserstack

Use ```browserstack-sdk``` to run the automation on browserstack

Eg:

```browserstack-sdk pytest steps/<Give the test file which we wanted to run> --browserstack.config browserstack/ymlconfig/<browserstackYmlFile>.yml```


Eg:

```browserstack-sdk pytest steps/<Give the test file which we wanted to run> --browserstack.config "browserstack/ymlconfig/browserstack_brinks.yml"```


Below is one example of complete command we use in CICD to run automation on browserstack:

```browserstack-sdk pytest -s -v --env=prod --cucumberjson results/test_sanity_brinks.json steps/test_sanity_brinks.py --alluredir allure-results --browserstack.config "browserstack/ymlconfig/browserstack_brinks.yml"```


**[Optional]If you want the automation to run on python virtual environment, use below steps. Its optional**

Use below command to install virtual environment dependencies

```pip install virtualenv```


Use below command to create python virtual environment

```python -m venv <virtualEnvironmentName>``` - This will create virtual environment in current directory

Eg:
```python -m venv env``` 


Use below command to activate the python virtual environment

```source env/bin/activate``` - For mac/linux

```env\Scripts\activate.bat``` - For windows

Now the python virtual environment was activate. We can use command to execute the tests inside the virtual environment 


Use below command to deactivate the python virtual environment

```deactivate```



## Result & Report

Use `--cucumberjson` in command to generate cucumber result json file

```pytest steps/<Give the test file which we wanted to run> --cucumberjson results/result_file_name.json```

Eg:

```pytest steps/test_localization_english.py --cucumberjson results/test_sanity_brinks.json```


Use `--alluredir allure-results` in command to generate allure report. This will store allure results in allure-results folder

```pytest steps/<Give the test file which we wanted to run> --alluredir allure-results```

Eg:

```pytest steps/test_localization_english.py --alluredir allure-results```


To generate report & use below command

```allure serve```

This will open the allure report in browser



## Contributors & Contact details:
***For any query, please contact:***

- jaya.prakash@lytx.com

- aaron.fawcett@lytx.com

- robin.r@lytx.com

- ruksar.madalmatti@lytx.com

- satish.punekar@lytx.com

- balaji.kamaraj@lytx.com
