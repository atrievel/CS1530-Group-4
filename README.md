# CS1530-Group-4

Term project for Pitt CS1530 - Software Engineering

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

``` python
Give examples
```
(need python? https://www.python.org/downloads/)

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

``` python
Give the example
```

And repeat

``` python
until finished
```

End with an example of getting some data out of the system or using it for a little demo

Quick Flask tutorial here.

1. To acquire Flask, create a directory with the cmd command prompt in a preferred place.
2. after the directory is created, type in the cmd window pip install flask.
3. Create a file "app.py"  with the content:

from flask import Flask
app = Flask(__name__)

4. Define the main route and handle the request with "Welcome!". Append the content to app.py below:

@app.route("/")
def main():
    return "Welcome!"
   
5. In command prompt, type in the command "python app.py" and redirect a web browser to http://localhost:5000/
You should see "Welcome!" 

For consistency so far, please check app.py in the repo.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

``` python
Give an example
```

### And coding style tests

Explain what these tests test and why

``` python
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://flask.pocoo.org/docs/0.12/) - The web framework used

## Versioning

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
