# CodeFeed

CodeFeed is a social media interface designed for software engineers, by software engineers. This web application implements certain functionalities from already popular social-media platforms, including: Twitter, Reddit and Stack Overflow. However, CodeFeed combines and modifies the best features of these platforms to create a unique and refreshing user experience. This platform will be sure to attract developers who wish to create quality and inspirational codebases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

``` python
pip install requirements.txt
```

Note: CodeFeed was built on Python 3.6.3

### Installing

A step by step series of examples that tell you have to get a development env running

On Windows (admin mode on Powershell or CMD)

``` python
set FLASK_APP=codefeed.py
flask initdb
python -m flask run
```

Or on Linux/Mac OSx

``` python
export FLASK_APP=codefeed.py
flask initdb
flask run
```

Then go to localhost:5000 on your web browser to run the application. You should see a page called landing.html

## Running the tests

TO DO

### Break down into end to end tests

TO DO

``` python
Give an example
```

### And coding style tests

TO DO

``` python
Give an example
```

## Deployment

In order to deploy this application, the database will need to be migrated to something like PostgreSQL or MySQL. The application will also need to be hosted on a site such as PythonAnywhere, Heroku, or AWS.

## Built With

* [Flask](http://flask.pocoo.org/docs/0.12/) - The web microframework
* [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM database tool
* [ECMAScript 6](http://es6-features.org/#Constants) - The version of JavaScript compliance used
* [BootStrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - The front-end framework
* [PyTest](http://pytest-flask.readthedocs.io/en/latest/) - The back-end testing suite
* [Mocha](https://mochajs.org/) - The front-end testing suite

## Versioning

* *Current Build (in progress)* 1.0.0 - Initial release based on documentation requirements

## Authors

* **Alec Trievel** - *Project Manager, Front-end Specialist, Quality Assurance* - [GitHub](https://github.com/AlecT58)
* **Tim Plats** - *Front-end specialist, Database Admin* - [GitHub](https://github.com/twsp)
* **Jeremy Kato** - *Database Admin* - [GitHub](https://github.com/jeremykato)
* **Joseph Kostial** - *Back-end Specialist* - [GitHub](https://github.com/jmk243)
* **Albert Yang** - *Back-end specialist, Quality Assurance* - [GitHub](https://github.com/aly31)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* TO DO