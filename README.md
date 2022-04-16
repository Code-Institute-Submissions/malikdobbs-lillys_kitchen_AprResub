# Lilly's Kitchen
[View the live project here](https://lillys-kitchen.herokuapp.com/index)

[View the repo in GitHub](https://github.com/malikdobbs/lillys_kitchen)

* This is the promotional website for Lilly's Kitchen. Liily's Kitchen is a recipe finder website where users can find recipes created by other users and create their own to share with there friends, family and our online community. 

* This website has been devleoped with responsive design in mind and can be used on different devices and easy navigation throughout the web page for both new users and returning users who want to share their favourite recipes with others.

## User Experience (UX)

### User Stories

#### First time visitor goals

* As a first time visitor I want to easily understand the main purpose of this website and whether i wish to return to this website for future visits
* As a first time visitor I want to be able to find different recipes and guidance on how to make meals that may interest me
* As a first time visitor I want to be able to click on the meals through the click of 1 button
* As a first time visitor I want to have the ability to create an account if i wish to join your community

#### Returning visitor goals

* As a returning visitor I want to be able to log into my own account easily
* As a returning vistor I want to be able to log out of my own account
* As a returning visitor I want to be able to access information on how to make a specific recipe and what ingredients I need to make this meal etc
* As a returning visitor I want to be able to share my favourite recipes for others to try themselves
* As a returning visitor I want to be able to edit my recipes and update info such as ingredients, methods etc

#### Frequent visitor goals

* As a frequent visitor i want to be able to edit my recipes and update info such as ingredients, methods etc
* As a frequent visitor I want to be able to delete my recipes
* As a frequent visitor I want to be able to search recipes by either there name or description of that recipe

## Scope

Lilly's Kitchen is centered around the CRUD (create, read, update and delete) functionality and has been created using MongoDB management system and Flask for creating the application using jinja notation, HTML, CSS, JS and Python. The features I want to implement to this app, as follows:

* CRUD opeations to allow users interaction with the app
* Functionality to allow users to create a recipe
* Functionality to allow users to read there own and others recipes
* Functionality to allow users to edit/update recipes they have created
* Functionality to allow users to delete a recipe they have created
* Functionality to allow users to search for recipes
* Functionality to allow users to create an account
* Responsive design and beautiful looking application on all devices

## Structure

* Recipes will be stored in the app on the recipes page for all users to view
* Users will be able to search for recipes via either the name of a recipe or key words from the description of the recipe
* Users will be able to edit or delete recipes they have created via simple and easy to use buttons on the recipes page

## Skeleton

Find below links for my wireframes, showing how i planned for my web pages to be structured and layout on different device sizes such as laptop, tablet and mobile:

### Wireframes

The Wireframes have been creating using balsamiq:

* [Index Page](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/Home-Page.png)

* [Log In Page](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/Log-In-Page.png)

* [Register Page](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/Register-Page.png)

* [Recipes Page](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/Recipes-Page.png)

* [Add Recipes Page](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/Add-Recipe-Page.png)

* [Edit Recipes Page](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/Edit-Recipe-Page.png)

### Data Schema

* Lilly's Kitchen has used MongoDB to retain and retrieve data input by the user. [dbdiagram.io](https://dbdiagram.io/) was used to help illustrate my database schema. See below the database schema for Lilly's Kitchen:
[database schema](https://github.com/malikdobbs/lillys_kitchen/blob/main/static/images/database-schema.png)

My collection contains two collections which holds documents for users to input data into Lilly's Kitchen website:

* Users - This collection stores users data. When a user signs up and creates an account, their username and password will be saved and stored in the db which allows users access to log in to Lilly's Kitchen and in turn create, read, edit and delete recipes as they wish
* Recipes - This collections stores users recipes. When a user creates a recipe, the name, description, prep time, cooking time, ingredients, servings, image and method will be saved and stored in the db for visitors to see when they access. The user who creates the recipes will also have the functionality to edit or delete their recipes as they see fit.

## Surface

### Design

Lilly's Kitchen uses [Materialize](https://materializecss.com/) as a framework to help create a beautiful website that users will enjoy viewing and using. Materialize helped to create the layout of the web page using divs, cards, navbars and forms for a simple, easy to use and interactive website for users to create and share recipes. Also, Google Fonts has been imported into my CSS file for good looking typography. The colour scheme is simple and classic

* #3e2723 is the main colour used throughout the website. This has been used as the main colour throughout the whole website and on the navbars
* #fffff0 is used as the font colour for most of the font throughout the website
* Curvisive has been imported from Google for all headers and navbar elements
* Lato has been imported from Google to be used as my secondary font for all other information throughout the website.

## Features

* The navbar has a logo in the top left hand corner which if clicked, will take users back to the home page. The navbar also displays different links to the user depending on whether they're logged in or not.
If the user has an account and is logged in they will be able to view the following: profile page, add a recipe, view recipes, visit home page and log out. 
If the user is not logged into the website the links visible to them will show as follows: home, view recipes, log in and sign up.
* The website has been created to be visible and accessible on different device screens such as: Android, IOS, Windows, MacBooks and tablets.
* The footer displays copyright of Lilly's Kitchen and links to social media pages, as follows: Twitter, Pinterest, Google and Instagram
* All visitors can search for recipes on the website via the search box on the view recipes page
* Registered users can create recipes via the add recipe button in the nav bar
* Registered users can edit and delete their recipes, by clicking on the respective button which displays on the recipe card only for recipes created by that specific user

## Future Features

* Create a contact us form for users to get in touch with the owner of the website if they have any complaints or feedback to provide regarding their experience using Lilly's Kitchen
* I would like to implement a function that displays recipes based on what meal that is, such as a dinner, breakfast, lunch and dessert tab
* I would like to incorporate a newsletter feature for users where they will receive advice on nutritional information, ingredients that are in season and advice on healthy foods etc

## Technologies Used

### Langugages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

### Frameworks and Libraries

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - framework used in Python
* [Jinja](https://palletsprojects.com/p/jinja/) - templating language used in Python for advanced routing
* [Materialize](https://materializecss.com/) - used to add responsiveness and styling elements from the Materialize framework
* [Font Awesome](https://fontawesome.com/) - used to add icons on specific elements throughout webpage
* [Google Fonts](https://fonts.google.com/) - used to style fonts for the typography on the website
* [JQuery](https://jquery.com/) - used for DOM manipulation on navbar element and copyright formatting

### Database system

* [MongoDB](https://www.mongodb.com/)

### Other technologies

* [GitHub](https://github.com/)
* [Git](https://git-scm.com/)
* [Heroku](https://dashboard.heroku.com/)
* [Balsamiq](https://balsamiq.com/)

## Testing

* W3C HTML validator
* W3C CSS validator
* Esprima JavaScript validator

### Further Testing

* The website has been viewed on android mobile device and IOS phone and tablet devices
* The website has been viewed on Google Chrome, Safari and Firefox
* Friends and family tested the website on their phones, tablets and laptops and did not inform me of any issues regarding bugs or issues with the website

## Deployment

### Local Deployment

1. To clone this repository, copy and paste the following code into your terminal:
gh repo clone malikdobbs/lillys_kitchen
2. In the terminal window change directory (CD) to the correct file location (directory you created for your own repository)
3. Create your environment variables:
  * Create env.py file in the root directory
  * At the top of the env.py file add "import os"
  * In the env.py file set the connection to your MongoDB(MONGO_URI) database and a SECRET_KEY using the following syntax:
`os.environ.setdefault["MONGO_URI", "mongodb+srv":("enter your username and password here"]`
`os.environ.setdefault["SECRET_KEY"] = "Enter your Secret Key here"`
4. Install all requirements from the requirements.txt file by entering the following syntax into your terminal:
  * pip3 install -r requirements.txt
5. Create a new Database in MongoDB Atlas called "recipe_finder" 
* (if you dont have an account, sign up and create an account)
6. In "recipe_finder" Database create the following 2 collections:
* Recipes:
 `_id : <ObjectId>`,
 `recipe_name : <string>`,
 `prep_time : <string>`,
 `cook_time : <string>`,
 `serves : <string>`,
 `ingredients : <string>`,
 `recipe_description : <string>`,
 `image : <string>`,
 `method_1 : <string>`,
 `method_2 : <string>`,
 `method_3 : <string>`,
 `method_4 : <string>`,
 `method_5 : <string>`,
 `created_by : <string>`
* Users:
 `_id : <ObjectId>`,
 `username : <string>`,
 `password : <string>`
7. In the last line of app.py change `debug=False` to `debug=True`
8. To run the application type the following command in your terminal:
 `python3 app.py`

### Heroku Deployment

1. Create a requirement.txt file, which contains a list of dependencies. In the terminal type the following command:
  `pip3 freeze --local > requirements.txt`
2. Create a Procfile, which tells Heroku how to run the project. In the terminal type the following command:
  `echo web: python run.py > Procfile
3. `git add/commit and push` these files to GitHub
4. Create a new app in Heroku
5. Using the Heroku dashboard link your Heroku app to your GitHub repository by following these steps:
  * Select the "Deploy" tab, scroll down to "Deployment method" and choose the GitHub icon
  * Scroll down to "App connected to GitHub", then find and select your repository
6. Select the settings tab and scroll down to "Reveal Config Vars" and set the following config vars:
  * IP: 0.0.0.0
  * PORT: 5000
  * MONGO_URI: `<link to your MongoDB database>`
  * SECRET_KEY: `<your secret key>
  * MONGO_DBNAME: `<your collection name>`
  * DEBUG: FALSE
7. Enable "Automatic deploys"
8. Scroll down to "Manual deployment" and click "Deploy branch"
9. The app will be deployed. Click "Open app" to view the app

## Credits

The recipes used on Lilly's Kitchen has come from multiple different sources as referenced below:
* [Steak and Chips recipe](https://properfoodie.com/steak-and-chips/)
* [Jerk Chicken recipe](https://www.bbcgoodfood.com/recipes/jerk-chicken-rice-peas)
* [Shrimp Alfredo recipe](https://natashaskitchen.com/creamy-shrimp-alfredo-pasta-recipe/)
* [Sweet Potato Pie](https://www.allrecipes.com/recipe/12142/sweet-potato-pie-i/)
* [Korean Fried Wings](https://www.cakenknife.com/crispy-korean-bbq-chicken-wings/)
* [Fish and Chips](https://www.thespruceeats.com/best-fish-and-chips-recipe-434856)
* [Salmon and Sweet Potato Mash](https://www.bbcgoodfood.com/recipes/sesame-salmon-purple-sprouting-broccoli-sweet-potato-mash)
* [Chicken Madras](https://www.bbcgoodfood.com/recipes/chicken-madras)
* [New York Cheesecake](https://www.bbcgoodfood.com/recipes/new-york-cheesecake)
* [Pancakes](https://www.bbc.co.uk/food/recipes/fluffyamericanpancak_74828)

* Code Institute Task Manager App - Helped me to create the foundation of Lilly's Kitchen
* Code Institue Thorin & Co App - Helped me loop through the cards on how to display recipe card and images on screen

* Delete recipes button - Used W3Schools to help wire up delete recipes function (https://www.w3schools.com/python/python_mongodb_delete.asp)

## Media

* Images used for recipes were taken Google Images

## Acknowledgement

* My mentor, Gerard McBride for continous support, help and advice when necessary
* Code Institue - Task Manager walkthrough project
* Code Institue - Thorin & Co walkthrough project
