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
