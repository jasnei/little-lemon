# Little lemon restaurant api

This is a simple restaurant api built using Python and Django. It allows users to create, read, update and delete restaurants and menu items.

## Getting started

To get started, clone the repository and install the required packages using pip.

```
git clone https://github.com/jasnei/little-lemon.git
cd littlelemon
pip install -r requirements.txt
```

## Running the server

To run the server, use the following command:

```
python manage.py runserver
```

## API endpoints

The API has the following endpoints:

| Endpoint | Method | Description |
| --- | --- | --- |
|auth/users/ | POST | Register a new user |
|auth/users/login/ | POST | Login a user |
|auth/users/logout/ | POST | Logout a user |
|api/api-token-auth/ | POST | Get an access token |
|api/menu-items | GET | Get a list of all restaurants |
|api/menu-items | POST | Create a new menu item |
|api/menu-items/{id} | GET | Get a specific menu item |
|api/menu-items/{id} | PUT | Update a specific menu item |
|api/menu-items/{id} | DELETE | Delete a specific menu item |



