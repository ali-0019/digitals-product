# digitals-product

django dimple app for display digitals product(mp4,jpg,...)
with user subsciption for watch and share content


## Features of this Project

### A. Admin Users Can
1. Manage Products (edit caregories and products : Add, Update, Filter and Delete)
2. Manage Users and subscription(Update, Filter and Delete)
3. Manage Payments (gateways and payments : Update, Filter and Delete)

### B. Non-Subscription Users Can
1. View Categories
2. View details of category

### C. Subscription Users Can Can
1. All ot Non-Subscription Users
2. see the order status
3. view products
4. share products
5. get payment for orders
6. Update Profile 
7. Change Password
8. Reset Password

## How to Install and Run this project?
### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```
**3. Clone this project**
```
$  git clone https://github.com/ali-0019/digitals-product.git
```

Then, Enter the project
```
$  cd digitals-product
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the settings**

- Got to settings.py file
- create file like local_settings.py.example

*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (Admin)

Command for PC:
```
$  python manage.py createsuperuser
```

Command for MAC:
```
$  python3 manage.py createsuperuser
```
Then Add Email, Username and Password


