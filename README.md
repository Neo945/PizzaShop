<!-- Documentation -->
<!-- •	Proper documentation for each of the API endpoints 
and the accepted response for each endpoint should be 
mentioned in a README file on the repo. -->
<!-- •	Include the steps to run the project as well -->
# PizzaShop
A simple application for ordering pizza from a resturant.<br/> This application will store all the information about pizza which is ordered by the user.
- The pizza can be of type:
  - Regualr
  - Square
- The pizza can be of any size:
  - Small
  - Large
  - Medium
  - extra large
- And the user can add any types of toppings


## Table of Contents
- [Technologies](#technologies)
- [Endpoints](#endpoints)
- [Installation](#steps-to-install)
- [Extras](#extras)

## Endpoints
There are multiple endpoints in this application. These endpoints will perform different operation such as to place an order, delete an order, modify or view the order details.
### 1. Place an order
This operation will place an order as per **POST** request send by the user.<br/> 
In order to perform this the user will send a **POST** request at this endpoint sepecified below.
```

  http://127.0.0.1:8000/api/add/pizza

```
The format of the request body should be as mentiond below.
```javascript
{
  "name":"", // Name of the order
  "size":"",  // Size of the pizza ['regular','square']
  "type":"",  //Type of pizza ['small','large','medium','extra large']
  "topping":["toppings"] // Any toppings
}
```

> **_NOTE:_** The user should be logged in order to make this request

Example
|-|-|
|Reqest|Output|
|-|-|

### 2. Delete an order
This operation will delete an order from the database.<br/>
In order to perform this the user will send a **GET** request at this endpoint sepecified below.
```

  http://127.0.0.1:8000/api/delete/pizza/<int:order_number>

```
> **_NOTE:_** The user should be logged in order to make this request and the order cannot be deleted after 20 mins.

Example
|-|-|
|Reqest|Output|
|-|-|

### 3. Update an order
This operation will update an order as per **POST** request send by the user.<br/> 
In order to perform this the user will send a **POST** request at this endpoint sepecified below.
```

  http://127.0.0.1:8000/api/update/pizza/<int:order_number>

```
The format of the request body should be as mentiond below.
```javascript
{
  "id":"", // Order number
  "action":"", // Action thats need to be performend in order to with the toppings ['add','remove']
  "name":"", // Updated name (required=False)
  "size":"",  // updated Size ['regular','square'] (required=False)
  "type":"",  // updated Type of pizza ['small','large','medium','extra large'] (required=False)
  "topping":["toppings"] // Any toppings (required=False)
}
```

> **_NOTE:_** The user should be logged in order to make this request and the order cannot be updated after 20 mins.

Example
|-|-|
|Reqest|Output|
|-|-|

### 4. Get order Details
This operation will return the order details as per order number specified in the **GET** request send by the user.<br/> 
In order to perform this the user will send a **GET** request at this endpoint sepecified below.
```

  http://127.0.0.1:8000/api/get/pizza/<int:order_number>

```
> **_NOTE:_** The user should be logged in order to make this request.

Example
|-|-|
|Reqest|Output|
|-|-|

### 5. Get orders by their size
This operation will return all the orders with their details as per the size metioned in the **POST** request.<br/> 
In order to perform this the user will send a **POST** request at this endpoint sepecified below.
```

  http://127.0.0.1:8000/api/get/pizza/size

```
The format of the request body should be as mentiond below.
```javascript
{
  "size":"",  // Size of the pizza ['regular','square']
}
```
> **_NOTE:_** The user should be logged in order to make this request.

Example
|-|-|
|Reqest|Output|
|-|-|

### 6. Get orders by their type
This operation will return all the orders with their details as per the type metioned in the **POST** request.<br/> 
In order to perform this the user will send a **POST** request at this endpoint sepecified below.
```

  http://127.0.0.1:8000/api/get/pizza/size

```
The format of the request body should be as mentiond below.
```javascript
{
  "type":"",  //Type of pizza ['small','large','medium','extra large']
}
```
> **_NOTE:_** The user should be logged in order to make this request.

Example
|-|-|
|Reqest|Output|
|-|-|

## Technologies
This Application is made using Django framework (3.2.4) with Django Rest framework (3.12.4), Django (1.3.6) and MongoDB for database.<br/>
- Django is a python-based web framework that follows the model–template–views architectural pattern.<br/>
- Django REST framework is a toolkit for building Web APIs in Django.<br/>
- Djongo is used to connect Django with MongoDB server without changing the ORM.<br/>

## Steps to Install
### 1. Clone the project

```
  
  git clone https://github.com/Neo945/PizzaShop.git

```

<details open>
  <summary> For windows</summary>
  
### 2. Create a virtual environment

  ```
  
    python -m venv Django

  ```
### 3. Activate the Virtual environment

  ```
  
    ./Django/Scripts/activate

  ```
</details>
<details>
  
<summary> For Linux</summary>

### 2. Create a virtual environment

  ```
  
    virtualenv Django
  
  ```

### 3. Activate the Virtual environment

  ```
  
    source Django/bin/activate
  
  ```
</details>

### 4. Install all Packages
```

  pip install -r requirements.txt

```

### 6. Create a Superuser
```

python manage.py createsuperuser # create a superuser

```
> **_NOTE:_** Before running the application make sure that your MongoDB server is running with a database **pizzashop**
### 6. Run the project
```
  python manage.py check # check for any errors
  python manage.py makemigrations # creates new migrations based on the changes in model
  python manage.py migrate # applying those migrations
  python manage.py runserver # start a development Web server

```
## Extras
Set DEBUG to False in order to see the default JSON response.
