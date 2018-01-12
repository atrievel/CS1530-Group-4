# Setting Up Flask Environment

## Getting Started

A brief introduction to setting up a Flask environment and running a simple example

### Installing

A step by step series of examples that tell you have to get a development environment running

1. **Install [python](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe)**
* During the install, select the option to add python to the path variable
* Also make sure to select the option to install pip as well

2. **Install virtualenv**

* Virtualenv creates a Python environment that is segregated from your system wide Python installation
  * We can test our module without any external packages affecting the result
  * They are designed to be set up with a minimum of fuss, and to "just work" without requiring extensive configuration or specialized knowledge.
  * Generally a good practice and widely used in industry today

* How to create virtualenv
  * Run the following command in the terminal **(must be in admin mode)**
  ``` python
  pip install virtualenv
  ```
  * Navigate to the desired path of the environment *(example: C:\Users\Alec\Documents\GitHub\CS1530-Group-4)*

  * Run the following commands in the terminal *I am using SampleCode as my directory name. This name is up to you*
  ``` bash
  virtualenv --no-site-packages SampleCode
  SampleCode\Scripts\activate
  ```
3. **Install Python packages and dependencies**
* Download requirements.txt from this repository and copy it to your virtualenv directory

* Run the following command in the terminal to install the python packages **(must be in admin mode)**
  ```python
  pip install -r requirements.txt
  ```

Now everything should be installed and ready to run! To leave the virtual environment, simply type `deactivate` in the terminal