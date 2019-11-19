# Models package
## Usage
`database_engine` establishes the connection with the database

`base` helps us spread classes across files [reason](https://stackoverflow.com/questions/7478403/sqlalchemy-classes-across-files)

[Docs for `base`](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping)

`for each table` there is gonna be a model in this package

## Requirements
 * [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.