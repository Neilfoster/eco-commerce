[![Build Status](https://travis-ci.org/Neilfoster/eco-commerce.svg?branch=master)](https://travis-ci.org/Neilfoster/eco-commerce)

# Nádúr | Milestone Project 4

### Why I made this site

Nádúr is an App that allows users to buy natural Eco friendly cleaning 
and self care products as an alternative to the chemical heavy versions sold in
most supermarkets and stores. 
This is my final project at the end of [Code Institute's](https://codeinstitute.net/) Full
Stack Web Developer course. This site should showcase my hard work over the last year
to include both front-end and back-end development. This site is written in
HTML, CSS, JavaScript/jQuery, Python and Django.

### The purpose of this site

This site was created as a fully- fledged e-commerce website , using Stripe's API
to process the payment side.

### User Stories

> As a user I would like to be able buy natural self care products online rather 
that the chemical heavy alternatives sold in most high street stores

> I need to an App where I can purchase natural cleaning products for myhousehold as 
I have a yound child with allergies 

### UX

I wanted to create a simple and intuitive web site which users can browse through
both shop and blog features with ease. I wanted to use a natural color palatte and 
the design clean and un-cluttered to allow for a positive user experience 

## Features 

This site is primarily designed as an ecommerce site but also has a blog feature 
where only registered users can add a blog post

## Wireframes
 insert Wireframes here

## Technology Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Bootstrap 4](https://getbootstrap.com/)
* [Javascript](https://www.javascript.com/)
* [Jquery](https://jquery.com/)
* [Django 1.11.24](https://docs.djangoproject.com/en/3.0/releases/1.11.24/)
* [Stripe](https://stripe.com/ie)
* [Amazon Web Services](https://aws.amazon.com/)

 

## Database Data


## Things I would improve if I had more time


## Testing 
Testing is done using the Django testing framework, continuously integrated by Travis. 
There is also an extensive list of manual tests, which are included in the testing.txt folder in the repo.

## HTML & CSS
All my HTML and CSS are valid and checked with the following validators:

* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](https://jigsaw.w3.org/css-validator/)

## Deployment 
Getting my application ready for deployment included the following steps :
* Removing all my hard-coded variables and keys to Heroku's Config Vars for production
* Ensuring my applications requirements.txt is up to date with all the packages used
    in my application.
* Setting up a Procfile which is required by Heroku to know what command to
    run in order for my application to start.
* Setting Djangos debbuging to false in settings.py 
* Adding to Heroku to Allowed Hosts in my settings.py 
* Pushing all my latest code to GitHub ready for deployment via Heroku's GitHub function
    where you can deploy from GitHub to the app.

### When you deploy your app successfully Heroku will give you the URL where your app is hosted

* If your deployment in unsuccessful Heroku will log the cause of the error , which you can
    see in the 'view log ' section on the Heroku site. Here you can find a detailed view of what 
    has caused your application not to work successfully.

## Acknowledgements
