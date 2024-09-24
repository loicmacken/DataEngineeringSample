# DataEngineeringSample

A sample project for Data Engineering which receives and sorts country names from a public API endpoint.

## Description

This project retrieves country names and codes from [This Webservice](http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso).
In the country names, _"&"_ is first replaced by _"and"_, then they are sorted alphabetically and finally the first `N` countries are displayed by the user. The value for `N` can be entered as a commandline argument.

## Usage

First clone this repository:

```
  git clone <url>
```

Then build the docker container with the following command, where `<n>` should be replaced with the number of countries you would like to display (default is 10):

```
  docker-compose build --build-arg N_COUNTRIES=<n>
```

Finally run the docker container:

```
  docker-compose up
```

And the countries will be shown in the output.

## Software used

- Python modules:
  - `psycopg2` for interaction with Postgres.
  - `Requests` for fetching country data.
  - `SQLAlchemy` for creating and executing sql queries.
- Postgres as a database.
- Docker for containerization.
