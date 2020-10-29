:joy:

# Instagram-App
A clone of the website for the popular photo app Instagram 

#### By **Aoko Mercyline**

## Created on:
* 21/10/2020

## Description
This is an app that allows users to create their accounts,upload there profile,post any image with description, like post and comment on other people posts

## Project live site
  This is the live .[ Click for the demo](https://mercyinstag.herokuapp.com/)
 ![Image](static/images/instaclone.jpg)
    
## Features
* User can register and  log in to application using their own and unique credentials  and view other peoples posts.
* A user can like and comment on a post.
* A user can upload posts and edit their profile.
* A user can view profiles of people they follow.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.



## Behavior Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets redirected to the login page  | User logs in | Directed to the home page where they see posted photos | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |
|  Home page loads | Add comment  | Comment posted appears |
|  Homepage loads | Click `profile` | User's profile appears | 
| Homepage loads | Click `upload image` icon | User's redirected to a page where they can upload an image | 
| Homepage loads | Click `settings` icon | beside the profile user can change their password or logout | 
| Homepage loads | User inputs in the search form and presses enter | Searched results show |
| A list of users displays | Click `follow` button to follow(currently not working) | Reloaded to the homepage

## KNOWN BUGS

* Follow section is not working
* The app is still on development process


## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/AokoMercyline/Instagram-App

2. Activate virtual environment using python3 as default handler virtualenv -p /usr/bin/python3 venv && source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
- psql
- CREATE DATABASE instaclone;

4. Create .env file and paste  the following :

* SECRET_KEY = '<Secret_key(any)>'
* DBNAME = 'instaclone'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True
5. Run initial Migration
* python3 manage.py makemigrations instagram
* python3 manage.py migrate
6. Run the app
* python3 manage.py runserver
* Open terminal on localhost:8000

or run using the Markfile
* make migrations
* make migrate
* make serve

7. Running test

* Python manage.py test

## Technologies Used
* PYTHON 3
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRESS

## Prerequisite
* PYTHON 3
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRESS
## Support and contact details
contact me @ aokomercyline34@gmail.com
### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2020.All rigths reserved