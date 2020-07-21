# Full-Stack Development Milestone Project

[![Build Status](https://travis-ci.com/faithy80/fsd-project.svg?branch=master)](https://travis-ci.com/faithy80/fsd-project)

This is my final project at Code Institute Full-Stack Web Developer course. The purpose of the project is to demonstrate the strength of the Django framework and its scalability. Also, the ease of use encourages anybody to learn full-stack web development.

The features of Django:

* Django has an excellent documentation as it was developed by a newspaper at the beginning.
* Django uses Python Web-framework. Python is one of the easiest language to learn. Its simplicity allows us to create, modify, and debug backend codes and frontend templates easily.
* Django is optimized for search engines. Django works with URLs rather than IP addresses. Easy to add them to search engines without the need of conversion.
* Django is highly scalable. Only the necessary features need to be implemented. It suits both small and large projects.
* Django is very versatile in its own way. The logical structure (MVT, Model-View-Template) is a bit strict but it gives a stable fundamental for the developers.
* Django offers high level security. The sensitive information remains hidden at all time. Also, the csrf security tokens allow the users to pass information to the backend in a secure way.
* Django provides automated testing environment. Writing unit tests makes debugging easier and helps to understand defensive programming. The tests are useful at creating error-proof applications as the code can be tested thoroughly.
* Django provides rapid development. The framework already has a lot of built-in features. Also, external applications can be added to the project from [pypi.org](https://pypi.org/) to speed-up the development.

My project was inspired by the Covid-19 crysis. My children handed in their homework in digital format and were communicating with their teachers via an android application called seesaw during the pandemic. This project is an application for local schools. It is not only for communication but for buying certain products/services from the school. Although, it is developed for local schools, it can be scaled for county-sized or country-sized use.

## Table of contents

* [Demo](#demo)
* [UX](#ux)
  * [Strategy plane](#strategy-plane)
  * [Scope plane](#scope-plane)
  * [Structure plane](#structure-plane)
  * [Skeleton plane](#skeleton-plane)
  * [Surface plane](#surface-plane)
* [Features](#features)
  * [Frontend features](#frontend-features)
  * [Backend features](#backend-features)
  * [Future features](#future-implementations)
* [User stories](#user-stories)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Libraries and frameworks](#libraries-and-frameworks)
  * [Hosting, deployment and testing](#hosting-deployment-and-testing)
* [Deployment](#deployment)
  * [Local deployment](#local-deployment)
* [Testing and validation](#testing-and-validation)
* [Credits](#credits)
  * [Content](#content)
  * [Acknowledgements](#acknowledgements)

## Demo

The live demo is hosted by Heroku. Click [here](http://fsd-project.herokuapp.com/) to open the web application.

## UX

### Strategy plane

> What was I aiming to achieve in the first place, and for whom?

The project is for the teachers, the pupils, and their parents. It has three main parts.

The first one is the communication between the teachers and their pupils.

The second main part is the shop application. The parents can pay for book rental, art & craft, stationery, etc. It is also useful to pay for the school tour or summer camps. The shop accepts a convenient and secure card payments using stripe and it sends an email about the order in case of a successful payment.

The third main part is the admin dashboard. The products/services can be added to the shop on that page. The orders and the items are easy to track in the admin dashboard too.

The registration is fully automated and there is a password recovery option via email. While the students and the teachers have an account to log into, the parents don't have any account. Also, the admin is responsible for tracking the orders and managing the shop in this project. It is a future plan to create an account for the parents to order more conveniently and for the school secretary to maintain the shop.

### Scope plane

> What features did I want to include in my design?

The following features were implemented:

* teachers can login to the teacher dashboard
* teachers can view the uploaded content by their students (only one student account at a time)
* teachers can upload content for their pupils (for all students in the class)
* teachers can send messages to their pupils (only the pupil who the message was sent to can see it)
* teachers can receive messages from their students
* teachers can only get in touch with the students in the same class (e.g. students in the junior infant class, if the teacher is teaching in the junior infant class)

* students can login to the student dashboard
* students can upload their homework in digital format (e.g. pictures, documents, etc.)
* students can view the uploaded content by their teacher
* students can send messages to their teacher
* students can receive messages from their teacher

* parents can browse the school products/services and put the desired quantity in the shopping cart
* parents can change the quantity of the selected products/services in the shopping cart
* parents can remove the selected products/services in case of necessity
* parents can fill out the order form and card details to buy the selected products/services
* parents get a confirmation email to the given email address about the order number to keep it as a reference

* admins can log into the admin account
* admins can view every model in the database in the django built-in admin dashboard
* admins can add, edit or delete an entry in the database in the django built-in admin dashboard
* admins can add, edit or delete a product/service

* admins, teacher and students can change or recover the password for their account in case of necessity

### Stucture plane

> How is the information structured?

The landing page contains every information. The users can decide if they either want to shop, register for an account, or log into an existing one. The backend redirects the authenticated users to the correspondent dashboard. The teacher dashboard looks very similar to the student one. The only difference is the extra page where the teachers can view the selected student's content and messages. A structure of the pages is very simple and straightforward. It is easy to find everything that the user may look for.

### Skeleton plane

> How is the information implemented, and how will the user navigate through the features?

On the landing page, the navigation bar is responsible to guide the user to the right direction. The mobile view has a simple navigation bar that opens a side bar on click. The shop, the login, the registration, and the cart view is only available when the user is not logged in. The change password and the logout navitems are only visible on the navigation bar after the successful authentication. The views in non-authenticated mode have buttons on the bottom of the page to go forward or go back in the process to fix something or simply start over. The dashboards are a small bit different again. There are buttons to select the task that the users wish to do on the website. Every view that opens from the dashboard has the buttons on the bottom of the page for the navigation. The exception from this is the edit product view where also a red-coloured delete button can be found at the bottom of the page.

### Surface plane

> What will the product actually look like?

The mobile-first approach design was implemented on this website to maintain the user experience from mobile devices to desktop computers. The Materialize CSS framework is responsible for the responsiveness.

Each page is divided into three sections: the navbar, the actual page that contains the information, and the footer.

The footer remains hidden until the user scrolls down to the bottom of the page. It does not have a much use in this project but it may display contact information, map, social site icons and other useful information.

The navbar is simple. The colours are light but clearly separated from each other. There is not much typography on the website yet. The default font was used for this reason. There is an accordion on the teacher and the student dashboards. Although it displays only one information at a time (teacher content, student content or the messages), it is simple to use and it keeps the page tidy.

I chose Material CSS for the frontend design. I wanted to try another framework and I like the "materialized" input fields. Certainly, every design element, the framework or the way of displaying the information can be changed to meet the customers' expectations.  

## Features

I already mentioned some visible features in the UX Scope plane section. There are also few hidden ones. The backend is the heart of the project. It gathers all the information for the views and stores all the information that comes from the frontend. It is connected to a free Postgres database hosted by Heroku. The dj-database-url and the psycopg2-binary applications are connecting the database to the backend. The gunicorn application is responsible for running the Django website on the Heroku server. The static files and media content are hosted by the Google Cloud Storages API. I used the whitenoise app for static file hosting in debug mode but the project stopped working with internal server error after it switching to production mode. I have tried a lot of solutions to fix the problem but they did not work. The fastest and easiest way to get the project working again was to move the static file hosting to GCS too. The stripe application ensures smooth, secure and convenient card payment. A short JavaScript code guarantees the real-time connection to [stripe.com](https://stripe.com/ie) for the enhanced user experience and the immediate card data validation.

## Future implementations

I am planning to implement the following features in the future:

* to create webhooks for stripe to ensure that every order is stored in the database after a successful payment
* to add more unit tests for the dashboard view to cover more code
* to write more code for the backend to strengthen the defensive design
* to add a short JavaScript code to refresh the page after the session expires
* pagination

## User stories

## Technologies

### Languages

Required technologies:

* HTML 5
* CSS 3
* JavaScript
* Python
* Django
* Relational database (MySQL or Postgres)
* Stripe payment
* Additional libraries and APIs

Technologies used in the project:

* HTML5
* CSS3
* JavaScript
* Python (3.6)
* Django 3
* Google Cloud Storage API

### Libraries and frameworks

* [Materialize CSS (1.0.0)](https://materializecss.com/) framework for developing responsive websites
* [jQuery (3.5.1)](https://jquery.com/) library to use JavaScript easier on the website
* [django-materializecss-form](https://pypi.org/project/django-materializecss-form/) Materialize CSS style for Django forms
* [django-storages](https://pypi.org/project/django-storages/) static and media file hosting by Google Cloud Storage API
* [dj-database-url](https://pypi.org/project/dj-database-url/) to use database URL in Django applications
* [Pillow](https://pypi.org/project/Pillow/) for Python Imaging Library
* [stripe](https://pypi.org/project/stripe/) to handle secure card payments
* [coverage](https://pypi.org/project/coverage/) code coverage measurement for Python
* [gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) Python-PostgreSQL Database Adapter

### Hosting, deployment and testing

* [Git](https://git-scm.com/) for version control
* [Github](https://github.com/) for code hosting
* [Heroku](https://heroku.com) for app deployment and relational database hosting
* [Travis-CI](https://travis-ci.com/) for test deployment  

## Deployment

### Local deployment

## Testing and validation

## Credits

### Content

### Acknowledgements

I'd like to thank

* Code Institute for the tutorials, and
* Mentor Brian Macharia for his advice and guiding me through this project.
