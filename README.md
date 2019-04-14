# apitask

apitask is a Python + Django Project designed and built for managing a local books database and consulting an external books API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing

## Clone the project

Run, in the CLI:
```bash
git clone https://github.com/ezequielsalas/apitask.git
```

Then, move to the project:
```bash
cd apitask
```

Install dependencies
```bash
pip install -r requirements.txt
```

## Deployment

```bash
python manage.py runserver 8080
```

## Running the tests

```bash
coverage run --source='.' manage.py test api
```

## Built With

* [Django REST framework](https://github.com/encode/django-rest-framework) - Web Framework
* [Coverage](https://github.com/nedbat/coveragepy) - Testing, code coverage tool

## Authors

**Ezequiel Salas**

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
