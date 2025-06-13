# Databases

After fetching data via APIs, storing them is also really important for training a Machine Learning model.

You have multiple option:

Relation database
Not Relation database
Key-Value storage
Document storage
Data Lake
etc.
In this project, you will touch the first 2: relation and not relation database.

Relation databases are mainly used for application, not for source of data for training your ML models, but it can be really useful for the data processing, labeling and injection in another data storage. In this project, you will play with basic SQL commands but also create automation and computing on your data directly in SQL - less load at your application level since the computing power is dispatched to the database.

Not relation databases, known as NoSQL, will give you flexibility on your data: document, versioning, not a fix schema, no validation to improve performance, complex lookup, etc.

Resources
Read or watch:

MySQL:
What is Database & SQL?
MySQL Cheat Sheet
MySQL 5.7 SQL Statement Syntax
MySQL Performance: How To Leverage MySQL Database Indexing
Stored Procedure
Triggers
Views
Functions and Operators
Trigger Syntax and Examples
CREATE TABLE Statement
CREATE PROCEDURE and CREATE FUNCTION Statements
CREATE INDEX Statement
CREATE VIEW Statement
NoSQL:
NoSQL Databases Explained
What is NoSQL ?
Building Your First Application: An Introduction to MongoDB
MongoDB Tutorial 2 : Insert, Update, Remove, Query
Aggregation
Introduction to MongoDB and Python
mongo Shell Methods
The mongo Shell
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What’s a relational database
What’s a none relational database
What is difference between SQL and NoSQL
How to create tables with constraints
How to optimize queries by adding indexes
What is and how to implement stored procedures and functions in MySQL
What is and how to implement views in MySQL
What is and how to implement triggers in MySQL
What is ACID
What is a document storage
What are NoSQL types
What are benefits of a NoSQL database
How to query information from a NoSQL database
How to insert/update/delete information from a NoSQL database
How to use MongoDB
Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
All your SQL files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.39)
All your SQL queries should have a comment just before (i.e. syntax above)
All SQL keywords should be in uppercase (SELECT, WHERE…)
All your Mongo files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4.29)
The first line of all your Mongo files should be a comment: // my comment
All your Python files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9) and PyMongo (version 4.6.2)
The first line of all Python your files should be exactly #!/usr/bin/env python3
Your Python code should use the pycodestyle style (version 2.11.1)
All your Python modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your Python functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
Your Python code should not be executed when imported (by using if __name__ == "__main__":)
All your files should end with a new line
The length of your files will be tested using wc
