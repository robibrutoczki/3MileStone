# MyKitcheN

This project is a database-driven online recipe book. The project purpose is to  use MongoDB as a data storage.

I  used Flask to create the application, all functionality written in Python.

The project allowing a user to create, read, update and delete (full CRUD functionality) recipes that are stored in MongoDB.

### Table of Content :

[TOC]





## UX Design

My design was inspired by BBCgoodfood.com, where images rules the majority of the page. This creates a lively, more interesting website. I used the images to make the website more interactive with a "Netflix" like image chain. The purpose of a recipe book to help user to choose a recipe with multiple choices.

The homepage allows a user to hover over an image and by clicking on it ,it's taking user either to the shop or the recipes.(read)

The All recipe page shows all the recipes. Clicking on the images or the buttons will take us to the recipe's page.  That will show all the information about that recipe. User could edit this recipe or delete it or go back to the previous page.(edit,delete)

Creating a recipe is on the Add recipe page by using a  form. It allows a user to add many information regarding the recipe,from categories to ingredients etc. Than takes us to the All recipe page where user can see the added recipe.(create)  

Search recipe page offers a user the ability to narrow down the recipes on the website dependent on the user's requirements. I used a dropdown menu for that.

To return to the Home page use either the Logo or Home buttons, to go up to the top of the page use the **up arrow** on the right corner.

## Main features

#### Add Recipe

When the user is filling up the form and add a recipe to the database using **insert_one()** function. The rates section is on the form, where user can add it and later edit or modify it.(create)

#### Edit Recipe

A user is able to make edits to recipes found when opened one up . When a recipe inserted in MongoDB ,the database add a ID automatically to the entry,We can call on that when user want to make changes on the recipe. The user press edit button to get a similar form as the add recipe, when the necessary changes made they submit the form ,we using the  **update()** method to update the recipe.(edit, update)

#### Search Recipe

The user can select recipes from the MongoDB database by categories,difficulty,serving and by rate. Using **find_one()** method and **object ID** to find the requested recipes. Then rendering the chosen recipe on showOne.html where information from the database showing in a readable format to the user. On this page there are tree option to delete,edit a recipe or to go back to the All recipes page.

#### Delete Recipe

On the showOne.html the  'Delete' button found at the bottom of the page. Once clicked it uses the **remove()**  method to delete a recipe from MongoDB.

## Shop

This feature is added to the site to promote a "*Imaginary* Shop " .The user able to see all items or press a button to search/see items by category. This is in a other MongoDB collection ,not related to the recipes collection. User can't modify items or delete them. It is only to read or to add to a trolley(when log in/register added).

## Charts

This is a added information about  the MongoDB recipes collection. The charts are from MongoDB ,they're interactive and live with automatic update from MongoDB. User can see different information about recipes such as how many are in each category etc. 



### Features not in use :

#### Manage categories

Each recipe has a category, and the user is able to add, edit or delete categories . This is an  different collection that has a relationship with the recipes collection (category_name is the same for both collection). I decided NOT to use that on this website, until the login parts is not alive yet. The  function is perfectly in working order. User can add, delete or edit categories on the Manage categories page. When I finished the login part I just have to add a button/link to the navbar to make it usable.

The item from the Shop page will be added to the trolley, it's not working yet. Will be usable ,when Sign in/Register will be added.

## Technologies Used

- Python 3.7.7 (for the application)
- Flask (Python Microframework)
- Bootstrap 4 (to build the html pages)
- Google Fonts (' Jost ' for font family)
- JavaScript (to use the dropdown submenus)
- CSS (to make some changes on bootstrap's CSS)
- Git/GitHub (used for version control)
- [Typora](https://typora.io/)  (To edit the markdown files.)
- Logo Maker (for the logo and the favicon)

# How it is build ?

I did some research on the project. Looked on many online and paper recipe books. Asked many users, what do they looking for in a recipe book. 

Concluded the users want:

-  Lots of pictures to see what will be the outcome of the recipes.

- Easy use of functionality

- Simple,straight forward approach.

  

  ## Design 

  I used [Bootstrap 4](https://getbootstrap.com/) for the design ,because of the mobile first, responsive approach this was a logical choice.

  Bootstrap 4 provided a lot of useful  components, such as containers, jumbotrons( for the visible body of the site), cards,modals (to present the recipes in a responsive and visually appearing way ).

  Bootstrap using classes for  sizing and for basic CSS (built in), this made it easy to build for mobile.

  In addition I used external CSS to add nice colours and for the zoom on the "Netflix" pictures.

  CSS was used to change the scrollbar on the website.

  

  ### Base.html  (with  Python)

  Base.html is the frame of the other webpages, using Python-Flask on it .

  It's have links in the Header :

  - Favicon
  - Google fonts for the fonts of the website.
  - Bootstrap min.css (for bootstrap CSS)
  - External stylesheet called style.css
  - [Fontawesome icons](https://kit.fontawesome.com) 

  Bottom of the page there are some necessary  links and scripts,also there is a footer with social links.

  

  In the base.html I have this code in:

  <div class="container col-lg-8 col-sm-12 mt-1">
        {% block content %} {% endblock %}
  </div>

​      Every other HTML page refer to this and got the base.html as a frame, using all the links, scripts etc from it.

​      {% extends 'base.html'%}  This is the "reference" to base.html

​      {% block content %}

​      I put the content of each page here. It is a must to use the word "content " here . Instead "block " could be anything         else, but must be closed using the same word .

​      {% endblock %}

### Navbar

Every navbar item refers to a page using links like this :

```
href="{{url_for('get_recipes')}}"
```

It is the way to use Python in the HTML page. There are codes in the app.py to render HTML pages :

```
@app.route('/')
@app.route('/get_recipes')   # Starting point of the website
def get_recipes():
    return render_template("recipe.html",
                           recipes=mongo.db.recipes.find())

```

To use this to render HTML, redirect, request and use url_for we have to install/import :

```
from flask import Flask, render_template, redirect, request, url_for
```

In the navbar there is a sign in/register modal what is not used yet. It's not necessary to this project, but for the running website it is a must . User can't buy items without  sign in. Therefore in the future I have to add this function, there is a popup modal to inform users about this. 

###   JavaScript

For the dropdown menu(for search in recipes by a filter) and submenus I used JavaScript .

## Database 

MongoDB a non-SQL database , using collections.

The database is structured with two collections, recipes and categories. The two collections are related as recipes contains a 'category_name' key that corresponds the categories collection. In a collection any entry will get a ID ,automatically added by MongoDB and we can use that to find,modify data in the database.

/ When the sign in/register parts added ,it will have a collection for users too. /

The recipes have key/value pairs that make up a description of the recipe. Using that we can refer to that keys and show they values to the user in the Front-End.

An example of a recipe can be found in static/img/recipe.png

# Project

## Version control

Templates folder holding all the HTML files, static folder for the img folder including the pictures and css folder holding style.css. The rest of the files are in the root folder.   

I used GitHub for version control. Updated every time I made major changes on the project.

Project can be find here : https://github.com/robibrutoczki/3MileStone

To clone the project :

```
https://github.com/robibrutoczki/3MileStone.git
```

Note : to hide login details I used env.py where the details been saved. For that I imported:

```
from os import path
```

Then :

```
if path.exists("env.py"):
    import env
```

Added env.py  to .gitignore, however when I pushed to GitHub it was visible. So I had to delete them from GitHub.

Conclusion :In the beginning of any project, must set up .gitignore otherwise sensitive information could be seen by anybody. Therefore I changed my login password.

## Code

Code is written in Gitpod.



## Deployment

Project been deployed on Heroku.

To deploy a project on Heroku :

I needed to install all necessary libraries and micro frameworks first.

```
import os

from os import path
from datetime import datetime
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

from flask import Flask, render_template, redirect, request, url_for
```

To make a file of the dependencies we need a requirements.txt file:

```
pip3 freeze -- local > requirements.txt
```

We need a Procfile to show to Heroku what language we use :

```
echo web:python app.py > Procfile
/* result will be a file including a line of code: web: python app.py */
```

Those above should be enough to be able to deploy on Heroku ,however I run into a problem.

Heroku didn't recognise the language ,after a lengthy research I found the solution:

I hade to add a new text file : runtime.txt, I had to write only one line in it : python - 3.7.6.

That is let Heroku know, what version of Python we used to write our code.

To deploy ,we need to login to Heroku .

```
$ heroku login
```

After the login, it's like pushing to GitHub:

```

git init
git add .
git commit -m "My first commit"
git push heroku master
```

Deploying in Heroku we need to set some variables (the first is the key, the second is the value :

- IP = 0.0.0.0
- PORT = 5000
- MONGO_URI (login to the database) Some link
- MY_DB (this is to show to Heroku where to look for the database) Name of the database.

There are no differences between the development and deployed versions, but there will be some update on it later(sign in and working shop) .

This project is written in Python 3.

Link to the deployed app : https://my-recipes-ms.herokuapp.com/



## Tests

### 

### Tested for

- Navlogo link is working

- Navbar working as it should

- Links in the carousel's modal  works(home page)

- Links in footers are working

- Clicking on pictures on top takes us to the shop 

- Clicking on pictures on bottom takes us to the recipes 

- Responsiveness works on all size of screens

  

###    All recipes

- All recipes are showing 
- Links on the cards pictures and buttons are working and takes us to the right recipe

####    Search recipes

- Dropdown menu working well and its hidden on smaller devices
- All the chosen options are deliver the right recipes

#### Add Recipe 

- The form works with all fields

- The fields are filled, can't save a empty recipe (for some field required added to the code)

- Add recipe button have icon and saves recipe to database 

- Cancel button returns us to All recipes

- Test that a new added recipe  appears on the All recipes page

  

####     Edit Recipe 

There are two ways to get to editing a recipe:

-over search recipe we choose one recipe

-from All recipes we choose one

Clicking on the Edit button we can change the recipe or click on Cancel button to go back to All recipes page.

- Make sure that the form is with the correct data from the MongoDB document when editing recipe.

- Ensure a recipe is able to be updated more than once without any problems 

- Fields are showing the correct options.

  

  When one recipe shown there is a delete button to delete a recipe from database. Tested it's working and after deleting the recipe it's return to All recipe page. 

  

  ### Shop

  Shop is almost the same as All recipe page ,showing all the items in the shop. User able to switch between categories by the group buttons.

  - Buttons are showing the right items
  - Clicking on the items picture or the button under ,shows the right item.
  - On showing one item ,Add to trolley button will bring up a modal (will be changed in the future to a real function)
  - The cancel button take us back to the Shop

#### Credits

The dropdown menu idea came from https://jqueryui.com/menu/.

The "Netflix" like picture-hover idea came from https://mdbootstrap.com/.

Both have been modified to the needs of the project.



## 

