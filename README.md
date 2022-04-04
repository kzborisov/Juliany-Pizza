# Juliany Pizza
[![Juliany Pizza Tests](https://github.com/kzborisov/Juliany-Pizza/actions/workflows/ci.yml/badge.svg)](https://github.com/kzborisov/Juliany-Pizza/actions/workflows/ci.yml)

## Visit the website
To view the website
* click [Juliany Pizza](https://juliany-pizza.herokuapp.com/)

## Description
The website is divided into the following sections:
1. Public Part:
   - Landing Page
   - Menu Page
   - About Page
   - Contacts Page
   - Login Page
   - Forgotten Password
   - Register Page
   - Cart Page
2. Private Part:
   - Profile Page
   - Orders Page (Staff only)
3. Admin Panel: <br>
   ```NOTE: Based on which group the user is in different options are shown in the admin panel.```
   
   - Admin User - Full CRUD Operations
   - Staff User - Limited CRUD Operations

## Features
- Everyone can see the menu
- Everyone can place an order
- Everyone can review their cart items
- Everyone can send mail through the contact form
- Everyone can register/login
- Registered users can request new password
- Logged-in user can modify their profile
- If the logged-in user is `staff` they can review/changed the status of the placed orders
- If the logged-in user is `staff` they can add/change menu items
- If the logged-in user is `admin` the have full CRUD permissions

## Known Bugs
There are no known bugs.

## Technology Stack
* Django
* HTML
* CSS
* BOOTSTRAP
* JAVASCRIPT
* jQUERY
* PostgreSQL
