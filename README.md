[![Build Status](https://travis-ci.org/Neilfoster/eco-commerce.svg?branch=master)](https://travis-ci.org/Neilfoster/eco-commerce)

# Nádúr | Milestone Project 4

### Project Purpose

This is my fourth and final [Code Institute](https://codeinstitute.net/) project in my full stack software development diploma course.
The purpose of this project was to create a fully-fledged e-commerce website in which users can register
and avail of some of the sites services using stripe's API to process the payment side. I used all of the 
knowledge I had learned over the past year and used all technologies that had been covered on the course.
Nádúr is a fictional E-commerce site that allows users to buy natural Eco-friendly cleaning and self-care products as an 
alternative to the chemical-heavy versions sold in most supermarkets and stores. The site sells both household and self care
products. It also features a blog section where you can read posts about issues related to the site such as environmental
issues and opinions about natural products. Registered users of the site can also add their Own blog posts as part of a thriving
and dynamic online community of like-minded individuals. 

### Goals

* The main goal of the project is to create a website in which users can purchase our range of products and become life
  long consumers of the brand. 
* To engage the user and make them feel like a part of a community by offering a blog section to both read and add content to
* Products should be easy to find and easy to proceed to the checkout for payment

## UX

I wanted to create a site that is easy to use and intuitive allowing the user to browse casually and mindfully through the various sections.
To adhere to the theme of nature, I wanted to use a natural color palette and create an open space with plenty of breathing room to
browse without being overwhelmed by unnecessary information and clutter. 
As the site sells both household and self care products I wanted to separate these two sections from each other so the user browses through
each section individually but also have the option to browse through all products together if this was desired. I achieved this by diving the 
sections visually on the landing page and also having a "Shop" tab in the navbar to show all products together. 
I also thought it was important to showcase the blog section on the landing page to allow users to go straight to the blog section
this can also be achieved via the "Blog" link on the navbar. 
I deviated slightly from my original wireframes, initially I wanted the blog image on the landing page and the text to be nested side by side
but after viewing this I decided it looked much better placed above the text and it also kept the same theme as the product sections.
Also in the shop view, I added a light grey coloured border to allow for a visual separation of content and a much cleaner presentation. 


### User Stories

> As a user, I would like to be able to buy natural self-care products online rather 
than the chemical-heavy alternatives sold in most high street stores

> I need to an App where I can purchase natural cleaning products for my household as 
I have a young child with allergies 

## Features 

* The abiltity to create an account and purchase products via stripes API payment system.
* Registered users to be able to able to view their order history via the history tab on the navbar
* Registered users to be able to add a blog post to our blog section to allow both registered and non-registered users to read. 
* The site should be easy to use and responsive on mobiles, desktops and tablets.

## Wireframes
 Wireframes can be found in the **Wireframes** folder within the repo.

## Technology Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Bootstrap 4](https://getbootstrap.com/)
* [Javascript](https://www.javascript.com/)
* [Jquery](https://jquery.com/)
* [Django 1.11.24](https://docs.djangoproject.com/en/3.0/releases/1.11.24/)
* [Stripe](https://stripe.com/ie)
* [Amazon Web Services](https://aws.amazon.com/)


## Things I would improve if I had more time
I would have liked to create a market place for independent makers of any self care or household products
to sell their products. This could be then integrated into their profile page and could be reviewed by
other users via a rating system. 
I would also have liked to create a comment section underneath each blog post which could only be viewed
by registered users. 
Both these features would create an online community of people who are passionate about sustainable and 
natural products and establish the brand as a company that also adheres to these issues.

## Testing 
Testing is done using the Django testing framework, continuously integrated by Travis. 
There is also an extensive list of manual tests, which are included in the **testing.txt** folder in the repo.

### HTML & CSS
All my HTML and CSS are valid and checked with the following validators:

* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](https://jigsaw.w3.org/css-validator/)

### Deployment 

Getting my application ready for deployment included the following steps :
* Removing all my hard-coded variables and keys to Heroku's Config Vars for production
* Ensuring my application's requirements.txt is up to date with all the packages used
    in my application.
* Setting up a Procfile which is required by Heroku to know what command to
    run for my application to start.
* Setting Djangos debugging to false in settings.py 
* Adding to Heroku to Allowed Hosts in my settings.py 
* Pushing all my latest code to GitHub ready for deployment via Heroku's GitHub function
    where you can deploy from GitHub to the app.
* When you deploy your app successfully Heroku will give you the URL where your app is hosted
* If your deployment in unsuccessful Heroku will log the cause of the error, which you can
    see in the 'view log ' section on the Heroku site. Here you can find a detailed view of what 
    has caused your application not to work successfully.

## Acknowledgements
 I would like to give a huge thanks to my mentor Brian Macharia who helped me so much in getting 
 through this project while a huge global pandemic was taking part in the background. Also a 
 massive thank you to all the Code Institute's student support team who helped me so many times 
 to understand some of the concepts I had been stuck on.
