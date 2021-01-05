# GraphQL_System
This is a backend package that plans to build an API server, that is backed by SQLAlchemeny, Redis and graphene. The authentication will be done through MySQL

## </br> API Routes Documentation Format
* Describes the documenation structure for routes, how they are accessed, parameters they use and their responses.</br>

Package Name | Layer {
<blockquote>
[x] __API__ - *Provides the URL of the API, states whether it is a POST, GET, DELETE or UPDATE method, provides the library used to build/support page.*</br>

[x] __Input__ - *Describes the parameters of the __API__*.</br>

[x] __Class__ - *Specifies the name of the class used by the route and the location of the file containing the route.*<br>

[x] __Output__ - *Feedback from server, depends on __Input__*</br>
</blockquote>
}


## **Layered package Architecture**
![Layed package description diagram](/images/Architecture.png)
### <br>*Register User | API* {
<blockquote>
[x] __API__ -  

```python
{"URL" : "###",  "method": "Post", "library": ["fastApi", "app/authentication/register_user.py"]}
``` 

[x] __Input__ - *
```python
{"username":"###", "password":"###", "age":"###", "gender":"###"}
```
*.</br>

[x] __Class__ - 
```python

# Class name: RegisterUser()
# file location: app/routes/register_user.py

```
<br>

[x] __Output__ - *Feedback from server, depends on __Input__*</br>
</blockquote>
}

### <br>*Register User | Authenticate* {
<blockquote>
[x] __API__ -  

```python
{"URL" : "###",  "method": "Insert to db", "library": "sqlalchemy"}
``` 

[x] __Input__ - *
```python
{"username":"###", "password":"###", "age":"###", "gender":"###"}
```
*.</br>

[x] __Class__ - 
```python

# Class name: RegisterUserModel(sqlalchemy)
# file location: app/authentication/register_user.py

```
<br>

[x] __Output__ - *Feedback from server, depends on __Input__*</br>
</blockquote>
}