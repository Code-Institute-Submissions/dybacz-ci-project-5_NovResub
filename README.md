# Peak Fitness E-commerce Site

![Peak Fitness logo](/static/images/readme/logo.png)

An E-Commerce B2C WebApp store specialising in personal gym equiptment, fitness accessories, healthy consumables & activewear. It also plans to specialise in a range of subscriptions plans realted to healthy living and fitness by providing personalised diet plans & exercise routines.
Provides a small social platform for other users to share their achievements and active & completed subscriptions 

The backend runs on the Django 3.2 python web-framework with a PostgreSQL database using the Django MVT model (similar to the standard MVC), the front-end web pages are rendered from templates served by the Django backend, these templates were written in a combination of HTML5 & Django templating language which allows for pythonic functions such as loops and variables to be utilised. 

CSS3, Bootstrap 5, JavaScript were utilised to gain the desired front-end functionality, UX and dynamic UI. AJAX requests will are performed using the Fetch API.

This WebApp & PostgreSQL database are hosted on Heroku with all static & media files hosted on AWS S3 and handled through Django.

Welcome to Peak Fitness!

We're here to make your search for the perfect fitness equipment that little bit easier. 

From sportswear to exercise equipment to nutritional meals, we've got you covered! Gone are the days of endlessly trawling the web for fitness inspiration that never seems to come. Here at Peak Fitness we aspire to bring you on a journey to help take your fitness to the next level. 

Not only do we offer a wide and unique range of sports equipment to suit all budgets, but we also offer personalised subscription plans tailored to you, meaning fitness no longer has to be a chore. Whether you're a sports enthusiast, looking to improve your health, or just want to browse for some nutritional inspiration, we are here to guide you in the right direction.

Why not subscribe to our monthly newsletter to be the first to hear about our latest offers and get inspiration on all things fitness! 


[Click here for the live version](https://peak-fitness.herokuapp.com/)

![Homepage](/static/images/readme/homepage.png)


# Current Features

## User Features

### **Navigation**

**Main Navigation**
* Search Bar
* Live Basket Total
* User Menu
* E-Commerce Nav
    * Home
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
![Product Page Desktop](/static/images/readme/product_page_desktop.png)
![Product Page mobile](/static/images/readme/product_page_mobile.png)

* Product Details Page
![Product Details Desktop](/static/images/readme/product_details_desktop.png)
![Product Details mobile](/static/images/readme/product_details_mobile.png)

* Basket Page/Checkout
![Product Basket Desktop](/static/images/readme/product_basket_desktop.png)
![Product Basket mobile](/static/images/readme/product_basket_mobile.png)

* Basket Canvas - on click of basket in desktop.
![Product Basket Canvas Desktop](/static/images/readme/product_basket_canvas_desktop.png)

* Secure Checkout Page
![Checkout Desktop](/static/images/readme/checkout_desktop.png)
![Checkout Mobile](/static/images/readme/checkout_mobile.png)

* Confirmation Page
![Confirmation Desktop](/static/images/readme/confirmation_desktop.png)
![Confirmation Mobile](/static/images/readme/confirmation_mobile.png)

* User Account
    * Profile Page
    ![Profile Desktop](/static/images/readme/profile_desktop.png)
    ![Profile Mobile](/static/images/readme/profile_mobile.png)
    * Orders Page
    ![Order Desktop](/static/images/readme/order_desktop.png)
    ![Order Mobile](/static/images/readme/order_mobile.png)

* Accounts Authorisation
    * Login
    ![Login Desktop](/static/images/readme/login_desktop.png)
    ![Login Mobile](/static/images/readme/login_mobile.png)
    * Register
    ![Register Desktop](/static/images/readme/register_desktop.png)
    ![Register Mobile](/static/images/readme/register_mobile.png)

* Cookies Accept
![Cookies Desktop](/static/images/readme/cookies_desktop.png)
![Cookies Mobile](/static/images/readme/cookies_mobile.png)

### **Rating system**
* System has live updating ratings system for users only. 
* Once a product is purchased by a user, they will recieve an instance to review the product in the Accounts > My ratings section
![My Ratings Desktop](/static/images/readme/myratings_desktop.png)
![My Ratings Mobile](/static/images/readme/myratings_mobile.png)
* User clicks leave a rating and is lead to the review page for the item.
![Rate Product Desktop](/static/images/readme/rate_desktop.png)
![Rate Product Mobile](/static/images/readme/rate_mobile.png)
* Once rating is submitted, it is added to ratings for that product and an avergage is summed for the total product rating.


## Admin/Staff Features


### **Account Canvas Admin**
![Admin Account Desktop](/static/images/readme/admin_account_canvas_desktop.png)
![Admin Account Mobile](/static/images/readme/admin_account_mobile.png)

* Add Product
![Add Product Desktop](/static/images/readme/add_product_desktop.png)
![Admin Product Mobile](/static/images/readme/add_product_mobile.png)
* Edit/Delete Product
![Edit Product Desktop](/static/images/readme/edit_product_desktop.png)
![Edit Product Mobile](/static/images/readme/edit_product_mobile.png)

### **Voucher Admin**
![Voucher Admin Desktop](/static/images/readme/voucheradmin_desktop.png)
![Voucher Admin Mobile](/static/images/readme/voucheradmin_mobile.png)
![Voucher Desktop](/static/images/readme/voucher_desktop.png)
![Voucher Mobile](/static/images/readme/voucher_mobile.png)


### **Functionality Left to Implement**
- Expiry Dates for Vouchers
- Plans App

## Future Features
- Gift Cards /Credit Vouchers
- Returns

## Data Model
- I confirmed the name entry input works; requires an entry into the field, accepts only characters (Desktop). Start button works and user name is added to the DOM.

### Browser Testing
**Lighthouse**
- Mobile Results
![Mobile Lighthouse Report](/static/images/readme/mobile_lighthouse_report.png)

- Desktop Results
![Desktop Lighthouse Report](/static/images/readme/desktop_lighthouse_report.png)
<!-- ![Lighthouse Results]()
- I confirmed that ... are all readable and easy to understand. -->

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

**Models:**
* Order Model:
- ![Order Model](/static/images/readme/order_model.png)
* Order Line Item Model:
- ![OrderLineItem Model](/static/images/readme/orderlineitem_model.png)
* User Profile Model:
- ![User Profile Model](/static/images/readme/userprofile_model.png)
* Main Category Model:
- ![Main Category Model](/static/images/readme/maincategory_model.png)
* Sub Category Model:
- ![Sub Category Model](/static/images/readme/subcategory_model.png)
* Product Model:
- ![Product Model](/static/images/readme/product_model.png)
* Item Rating Model:
- ![Item Rating Model](/static/images/readme/itemrating_model.png)
* User Rating Line ItemModel:
- ![UserRatingLineItem Model](/static/images/readme/userratingitemline_model.png)
* Voucher Model
- ![Voucher Model](/static/images/readme/voucher_model.png)

### Keyword Research

![Keyword Initial Research](/static/images/readme/keyword_1.png)

### Business Intents
- B2C Model
- E-commerce focusing on Fitness and Nutrition at good value.
- Unique range of sporting equipment to suit all budgets
- Environmentally Safe sourced products & nutrition.
- Eventual goal was to offer personalised subscription plans tailored to you.
- Plans were to include P.A workouts over a course or a diet/nutrition plan composed by a professional nutritionalist.

### Marketing Strategies 
- Subscription Newsletters with vouchers to apply on website.
- Social media such as Facebook et al.
- SEO Optimisation with help from tools such as Google services.

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
- [Cookie Consent](https://orestbida.com/demo-projects/cookieconsent/) - Cookie Consent

**Media:**
- Some images/videos used in this webapp were sourced from [Pexels](https://www.https://www.pexels.com/) & [Pixabay](https://pixabay.com/)
- Product images/videos used in this webapp were sourced from [Decathalon](https://www.decathlon.co.uk/)

**Fonts**
- Some of the fonts used in this webapp were sourced from [Google Fonts](https://fonts.google.com/)



