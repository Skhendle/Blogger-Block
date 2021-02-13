[![Build Status](https://travis-ci.org/Skhendle/GraphQL_System.svg?branch=main)](https://travis-ci.org/Skhendle/GraphQL_System)
[![codecov](https://codecov.io/gh/Skhendle/GraphQL_System/branch/main/graph/badge.svg?token=rSx7WWHUb9)](https://codecov.io/gh/Skhendle/GraphQL_System)
<br>
# **GraphQL_System**
This is a webserver application that plans to build an API server for  a user blogging platform. It will be built with fastApi, SQLAlchemeny, SQLlite, Redis and graphene. It will have three layers. The storage layer that will store\cache all the platform data, service layer that will allow us to implement the system requirements\logic, and API layer that will allow external programs to commincate with the system.


## **How To Start The APP** <br>
```python
# Python version: 3.9.0
"MINGW64 - bash terminal"
# Run command in directory you will be working from.
$ : git clone https://github.com/Skhendle/GraphQL_System.git
$ : cd GraphQL_System

To create virtual environment.
$ GraphQL_System : python -m venv env

# To activate virtual environment
# Windows 
$ GraphQL_System : source ".\env\Scripts\activate"
# Ubuntu 
$ GraphQL_System : source ./env/bin/activate

# To install the requirements run
$ GraphQL_System : pip  install -r requirements.txt

# To update requirements.txt after installing new package
$ GraphQL_System\app : pip freeze > requirements.txt

# To run the application use the following command
$ GraphQL_System : uvicorn app.main:app --reload

# To run a service of the application use the following command
$ GraphQL_System : uvicorn app.'service name'.main:app --reload
# E.g
$ GraphQL_System : uvicorn app.b_register.main:app --reload

# To deactivate virtual enviroment
$ GraphQL_System : deactivate
```


## **Accessing API DOCUMENTATION** <br>
- {server url}/docs
- {server url}/redoc


## </br> **API Routes Documentation Format**
* Describes the documenation structure for routes, how they are accessed, parameters they use, service packages used and the response.</br>


### **Package Layout | For Each System requirements**
<blockquote>

[x] __Input__ - *Contains parameters the API, will require to execute.*
</br>

[x] __Route__ - *Provides the URL of an API, states its Protocol( POST, GET, DELETE or UPDATE) and calls  the service to be executed*
</br>

[x] __Services__ - *Where the logic for a system requirement is executed*
</br>

[x] __Main__ - *Allows us to run a service of the application independently*</br>
</blockquote>

## **Layered Package Architecture**
![Layed package description diagram](/images/Architecture.png)

<br>

## **Class Diagrams**
![Layed package description diagram](/images/ClassDiagram.png)




