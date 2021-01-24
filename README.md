[![Build Status](https://travis-ci.org/Skhendle/GraphQL_System.svg?branch=main)](https://travis-ci.org/Skhendle/GraphQL_System)
[![codecov](https://codecov.io/gh/Skhendle/GraphQL_System/branch/main/graph/badge.svg?token=rSx7WWHUb9)](https://codecov.io/gh/Skhendle/GraphQL_System)
<br>
# **GraphQL_System**
This is a backend system that plans to build an API server for  a user blogging platfrom. It will be built with SQLAlchemeny, SQLlite, Redis and graphene. It will have three layers. The storage layer that contains all the system data, service layer that will allow us to implement the system requirements logic and API  layer that will allow external programs to  commincate with the system.


## **How To Start She APP** <br>
```python
# Python version: 3.9.0
"MINGW64 - bash terminal"
Run  command in directory you will be coding.
$ : git clone https://github.com/Skhendle/GraphQL_System.git
$ : cd GraphQL_System

To create virtual environment.
$ GraphQL_System : python -m venv env

To activate virtual environment
$ GraphQL_System : source ".\env\Scripts\activate"

To install the requirements run
$ GraphQL_System : pip  install -r requirements.txt

To update requirements.txt after installing new package
$ GraphQL_System\app : pip freeze > requirements.txt

To run the application use the following command
$ GraphQL_System : uvicorn app.main:app --reload

To deactivate virtual enviroment
$ GraphQL_System : deactivate
```


## **Accessing API DOCUMENTATION** <br>
- {server url}/docs
- {server url}/redoc


## </br> **API Routes Documentation Format**
* Describes the documenation structure for routes, how they are accessed, parameters they use, service packages used and the response.</br>


### **Package Layer Name | Layer**
<blockquote>


[x] __API__ - *Provides the URL of the API, states whether it is a POST, GET, DELETE or UPDATE method, provides the library used to build/support page.*
</br>


[x] __Input__ - *Describes the parameters of the __API__.*
</br>


[x] __Services__ - *Specifies the name of the class used by the route and the location of the file containing the route.*
</br>


[x] __Output__ - *Feedback from server, depends on __Input__*</br>
</blockquote>
</br>


## **Layered Package Architecture**
![Layed package description diagram](/images/Architecture.png)


### <br>*[ 1 ]. Register User | API*
<blockquote>
[x] __API__ -  

```python
{
    "route name": "register_api()",
    "method": "Post",
    "library": ["fastApi", "app.data_models.validator_models.user"],
    "file path":"app.routes.register_user.py"
}
```

[x] __Input__ -
```python
{
    "class name": "UserRegistrationModel()",
    "library": ["pydantic","typing"],
    "file path": "app.data_models.validator_models.user.py",
}
```

</br>

[x] __Service__ -
```python
{
    "Class name": "RegisterUser()",
    "packages": ["app.data_models.databse_models",
        "app.data_models.validator_models"],
    "file path": "app.services.user_registration.py"
}

```
<br>

[x] __Output__ - *Feedback can be viewed in __Service__ class*</br>
</blockquote>

### <br>*[ 2 ]. Login User | API*
<blockquote>
[x] __API__ -  

```python
{
    "route name": "login_api()",
    "method": "Get",
    "library": ["fastApi", "app.data_models.validator_models.user"],
    "file path":"app.routes.register_user.py"
}
```

[x] __Input__ -
```python
{
    "class name": "UserLoginnModel()",
    "library": ["pydantic","typing"],
    "file path": "app.data_models.validator_models.user.py",
}
```
</br>

[x] __Service__ -
```python
{
    "Class name": "UserLogin(), UserFriends()",
    "packages": ["app.data_models.databse_models",
        "app.data_models.validator_models"],
    "file path": ["app.services.user_login.py", "app.services.get_friends.py"]
}

```
<br>

[x] __Output__ - *Feedback can be viewed in __Service__ class*</br>
</blockquote>

### <br>*[ 3 ]. Create Post | API*
<blockquote>
[x] __API__ -  

```python
{
    "route name": "create_user_api()",
    "method": "POST",
    "library": ["fastApi", "app.data_models.validator_models.post","app.services.create_post"],
    "file path":"app.routes.create_post.py"
}
```

[x] __Input__ -
```python
{
    "class name": "CreateUserModel()",
    "library": ["pydantic","typing"],
    "file path": "app.data_models.validator_models.post.py",
}
```
</br>

[x] __Service__ -
```python
{
    "Class name": "CreateUser()",
    "packages": ["app.data_models.databse_models.post",
        "app.data_models.validator_models.post"],
    "file path": "app.services.create_post.py"
}

```
<br>

[x] __Output__ - *Feedback can be viewed in __Service__ class*</br>
</blockquote>


## **Class Diagrams**
![Layed package description diagram](/images/ClassDiagram.png)




