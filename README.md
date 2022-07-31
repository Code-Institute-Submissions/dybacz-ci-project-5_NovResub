# Peak Fitness E-commerce Site

![Peak Fitness logo](/static/images/readme/logo.png)

An E-Commerce WebApp store specialising in personal gym equiptment, fitness accessories, healthy consumables & activewear. It also specialises in a range of subscriptions plans realted to healthy living and fitness by providing personalised diet plans & exercise routines.
Provides a small social platform for other users to share their achievements and active & completed subscriptions 

The backend runs on the Django 3.2 python web-framework with a PostgreSQL database using the Django MVT model (similar to the standard MVC), the front-end web pages are rendered from templates served by the Django backend, these templates were written in a combination of HTML5 & Django templating language which allows for pythonic functions such as loops and variables to be utilised. 

CSS3, Bootstrap 5, JavaScript were utilised to gain the desired front-end functionality, UX and dynamic UI. AJAX requests will are performed using the Fetch API.

This WebApp & PostgreSQL database are hosted on Heroku with all static & media files hosted on AWS S3 and handled through Django.

[Click here for the live version](https://peak-fitness.herokuapp.com/)

# Current Features

## User Features

### **Navigation**

**Main Navigation**
* Search Bar
* Live Basket Total
* User Menu
* E-Commerce Nav
    * All 
    * Fitness
    * Nutrition
    * Activewear
    * Offers
    
#### Desktop Nav:
![Desktop Navigation](/static/images/readme/nav_desktop.png)

#### Mobile / Small Devices Navs:
![Mobile Navigation](/static/images/readme/nav_mobile_1.png)
#### Mobile / Small Devices Nav Search:
![Mobile Navigation Search](/static/images/readme/nav_mobile_2.png)


### **E-commerce / Shop**

* Browse Product Page

* Product Details Page

* Basket Page

* Checkout Page

* Confirmation Page

* E-commerce / Plans

* User Account
    * Profile Page
    * Orders Page
    * Plans Page
    * Settings Page
    * Help Page

* Login / Register - Accounts Authorisation

## Admin/Staff Features

### **Dashboard**

### **Dev Admin**

### **Functionality Left to Implement**

## Future Features

## How To Use

## Data Model

## Testing 

### General Testing


### Javascript Testing

**Jest**
- N/A

### Django Testing
**Coverage** - Ran on local sqlite3 database.

### User Testing

**Guest**

**Staff**

### Browser Testing
**Lighthouse**

## Deployment

This project was deployed using Heroku.

### Steps for deployment with AWS

* Fork or clone this repository
* Create a new Heroku app
* Create new PostgreSQL database for your Heroku app
* Set the build packs to `Python`
* Link the Heroku app to the repository
* Set Config Vars in settings as follows:
    * AWS_ACCESS_KEY_ID : Your AWS Access Key
    * AWS_SECRET_ACCESS_KEY: Your AWS Secret Access Key
    * DATABASE_URL : PostgreSQL database URL
    * SECRET_KEY : A_SECRET_KEY_OF_YOUR_CHOICE
    * USE_AWS : True
* Click on **Deploy**
* Run Heroku console:
    ```
        $ python3 manage.py migrate
    ```
* Finally to create a super user, in the Heroku console:
    ```
        $ python3 manage.py createsuperuser
    ```

The live link can be found here - [Peak Fitness](https://peak-fitness.herokuapp.com/)

## Design

### Model Designs

**Initial Models:**

### Initial Wireframes & Design Features

## Credits 

**Python Packages:**
- Django (3.2) - Web-Framework
- gunicorn (20.0.4) - Python WSGI HTTP Server for UNIX
- django-allauth (0.48) - Authentication
- django-crispy-forms (1.8.1) - Forms
- dj-database-url (0.5.0) - Allows connection to db
- psycopg2 (2.9.3) - Interact with PostgreSQL
- Pillow (9.2.0) - Not yet implemented, ready for menu images.
- s3transfer (0.3.3) - AWS S3
- Stripe (2.42.0) - Payment handler

**Front end:**

- [Bootstrap 5](https://getbootstrap.com/) - CSS Framework
- [Font Awesome](https://fontawesome.com/) - Icons

**Media:**
- The images/videos used in this webapp were sourced from [Pexels](https://www.https://www.pexels.com/) & [Pixabay](https://pixabay.com/)

**Fonts**
- Some of the fonts used in this webapp were sourced from [Google Fonts](https://fonts.google.com/)



