# Translate It!

This is a website designed to teach children from the age of 6 years and over how to build their vocabulary and conversation skills in Lithuanian through the creation of a library of English words that are then translated into Lithuanian. 

The site features an individual word search, categories of words, the meaning of a word, helpful information related to a word, as well as how to use them in a sentence, to support their use in conversation. 


The website is deployed live at [https://my-translate-it.herokuapp.com/](https://my-translate-it.herokuapp.com/)



# Table of Contents

- [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Project Wireframe and Design Process](#Project-Wireframe-and-Design-Process)
- [Features](#features)
    - [base.html](#basehtml)
    - [index.html (Home)](#indexhtml-home)
    - [register.html](#registerhtml)
    - [login.html](#loginhtml)
    - [profile.html](#profilehtml)
    - [words.html](#wordshtml)
    - [word_cat.html](#word_catshtml)
    - [add_words.html](#addwordshtml)
    - [my_words.html](#mywordshtml)
    - [pronunciation.html](#pronunciationhtml)
    - [add_category.html](#add_categoryhtml)
    - [edit_category.html](#edit_categoryhtml)
    - [edit_words.html](#edit_wordshtml)
    - [manage_categories](#mdmanage_categorieshtml)
    - [Future Features](#future_features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](README.md#credits)
    - [Media Design](README.md#media_design)
    - [Content](README.md#content)
    - [Acknowledgements](README.md#acknowledgements)
   


# UX
The site is for children (and their parents) who would like to start building their vocabulary of useful words in Lithuanian through the creation of a word library to enhance their conversational skills. The easy to use interface features word search, words arranged by category, definitions and helpful information, as well as the ability to add a user’s own words. There is an Administrator’s Portal where additional categories can be added. 

# Project Goals
The **goals** of this project are:

- Create an **interactive app** where site visitors can **create, search, translate and learn Lithuanian words**
- The app allows the users to manage their content, such as **creating** words, **reading** words **updating** words and **Deleting** (CRUD).
- The app that has different content functionalities for **site visitors** and **users** and also includes a **search and pronunciation functions**.
- The app should also be able to store required data, which is available for access when required

### Site Owner Goals
- To provide a platform for a family of users to translate, add, read and pronounce Lithuanian words.
- Encourage users to learn words that have been added to the library and/or create words for learning.
- Build an English to Lithuanian translation library, including helpful information, example sentences and pronouncing tips.


# User Stories
- [1] As a user, I want to have a library of words that are translated into Lithuanian so that I can learn to use them in a conversation. 
- [2] As a user, I want to be able to add more words with Lithuanian translation to a library as my English vocabulary expands. 
- [3] As a user, I want to be able to add useful information to any word I create, and show know how to use the word when speaking. 
- [4] As a user, I want to be able to find a guide that shows me  how to pronounce a Lithuanian word. 
- [5] As a user, I want to be able to find related words easily. 
- [6] As a parent, I want to be able to find a collection of words that are age appropriate for my child to learn to translate into Lithuanian.
- [7] As a parent, I want to be able to have some control over the words my child learns, so that I can focus their learning.

# Project Wireframe and Design Process
- [wireframe design](https://github.com/Leefarmer83/Translate-It/tree/master/static/wire_frames)
    - [Home](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/home.png)
    - [word](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/words.png)
    - [add_word](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/add_word.png)
    - [add_category](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/add_category.png)
    - [category_information](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/category_information.png)
    - [login](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/login.png)
    - [register](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/register.png)
    - [word_information](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/word_information.png)

This was my initial design for the website. During development the flow of data and website design changed for the better. 
The biggest change was the information on the translation, materilize had a great card feature that helped with selecting data.

# Design
The strategy for the design was to create an easy using website that naturally took the user on a seamless journey to first find a word, via word search or category search. If a word was not found they are then asked to log in and add it themselves. If the user adds a word their profile page will host only their words and the word is also added to the library for other users.

### Database design
The thought process behind adding words was to have the user stick to a template that would naturally add words to the existing library. Users will need to select a category, state the word, the translation of that word, useful information, and an example of the word in a sentence.
[Database collection structure in MongoDB](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/mongoDB_data_stucture.png)

### Colour and font
Colour and font were taken into account in order to make the interface eye catching for children, but also incorporated best practices in terms of accessibility, in order to cater for users of all learning abilities. 

### Images
Images used are from a free image website: https://www.shutterstock.com/.

### User structure
Anyone visiting the site can search words and categories.
Users can only add words once they are registered and logged in. 
Users can only delete their created words.
Users can only edit their own created words.
The Admin can only add, delete and edit categories.
User with access to database can delete, add and edit all.

**Related user story addressed:**
[7] As a parent, I want to be able to have some control over the words my child learns, so that I can focus their learning.


# Technologies Used

- **Resources**
    -	[HTML5](https://www.w3schools.com/html/default.asp)
    -	[CSS3](https://www.w3schools.com/css/default.asp)
    -	[JavaScript](https://www.w3schools.com/js/default.asp)
    -	[Python](https://www.python.org/)
    -	[JQuery](https://jquery.com/)
    -	[Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/)
    -	[Gitpod](https://www.gitpod.io/)
    -	[Git](https://git-scm.com/) 
    -	[GitHub](https://github.com/) 
- **Framework**
    -   [Flask](https://flask.palletsprojects.com/en/1.1.x/) 
    -   [materialize](https://materializecss.com/)
- **Database & Platform**
    -   [MongoDB](https://www.mongodb.com/)
    -   [Heroku](https://www.heroku.com/) 
- **Styling**
    -   [Fontawsome](https://fontawesome.com/)
    -   [GoogleFonts](https://fonts.google.com/)
- **Wireframe**
    -   [Balsamiq](https://balsamiq.com/)
- **Database Diagram**
    -   [OmniGraffle](https://www.omnigroup.com/omnigraffle/ios/)

# Testing

All testing can be found here [View TESTING.md](TESTING.md)

# Features

## base.html
All pages will inherit html from base.html. The website header contains the website navbar and footer, flash messaging. User rule structure is set in the base.html.

## index.html (Home)
The home page features a search function where users can search for an individual word by clicking on the search button. There is also a Categories section that features 9 pre populated categories of words for users to search on.

## register.html
On the Register page, users create a username and password that must be alpha-numeric and between 5 and 15 characters long for successful registration. 
This guidance is noted on the page to reduce friction for the user when registering. Once the user has chosen a username and password, they click the login button to enter the library. If a user chooses a username that already exists in the system, a banner message loads to let them know that username is not available. Users who may already have registered can click the login button at the bottom of the page to be taken to the login screen.

## login.html
On the Log In page, users can input their username and password, and select the Log In button to login. If a user enters an incorrect username or password, a banner pops up at the top of the page to let them know they have entered an incorrect credential. Unregistered users who land on this page are directed to register by clicking the register button. When a user logs out, a banner message pops up at the top of the page to let them know they have logged out successfully.

## profile.html
Once a user has registered, they land on the Profile page. The first time a user lands on this page, the page is empty, as the user has not added any words. Once a user has added words, they can see all of their words that they have added to the library. These words are displayed in the same card format as words on the Words page, with the translation, helpful information, and how the word is used in a sentence. Users can edit or delete these words. Users can add words or search for words using the buttons at the bottom of the page.

## words.html
When a user clicks on individual word search on the home page, they land on the Words page. Here the user can enter a word, reset the search to start again, or search for the word if they are happy with the entry they made. If a user opts to reset, the search bar clears and they are free to input another word. 
If a user inputs a word into search, and it is not in the prepopulated library, the user can add it themselves if they are logged in. 
On the Words page, users will also find all the words from the prepopulated categories listed in alphabetical order, with its translation, and the option to select useful information, and how the word is used in a sentence. Users can also choose to edit or delete the words, if they created the word. 
Users also have the option to register or login from this page, as words can only be added once logged in.

**Related user story addressed:**
[1] As a user, I want to have a library of words that are translated into Lithuanian so that I can learn to use them in a conversation. 
[3] As a user, I want to be able to add useful information to any word I create, and show know how to use the word when speaking.
[5] As a user, I want to be able to find related words easily.

## word_cat.html
When a user clicks on a category on the home page, they land on the Categories page. Here all the prepopulated words from the selected category are listed in alphabetical order, with the word’s translation, and the option to select useful information, and how the word is used in a sentence. Users can also use the return button at the bottom of the page to return to the main categories.

**Related user story addressed:**
[6] As a parent, I want to be able to find a collection of words that are age appropriate for my child to learn to translate into Lithuanian.

## add_words.html
If logged in, users are able to add a word to Translate It! To do this, they select a category using the drop down menu. They then add the English word, the Lithuanian translation, useful information, and how the word is used in a sentence. To have the entry added, users click the Add Word button at the bottom of the form.

**Related user story addressed:**
[3] As a user, I want to be able to add useful information to any word I create, and show know how to use the word when speaking.

**Related user story addressed:**
[2] As a user, I want to be able to add more words with Lithuanian translation to a library as my English vocabulary expands. 

## my_words.html
Once a user has added words, they can see all of their words that they have added to the library. These words are displayed in the same card format as words on the Words page, with the translation, helpful information, and how the word is used in a sentence. Users can edit or delete these words. Users can add words or search for words using the buttons at the bottom of the page.

## pronunciation.html
When a user selects Pronunciation from the toolbar, they land on the Pronunciation page. The table on this page lists the letters from the Lithuanian alphabet, how that letter sounds in English, together with an English word to illustrate an example of the sound in an English word.

**Related user story addressed:**
[4] As a user, I want to be able to find a guide that shows me  how to pronounce a Lithuanian word.

## add_category.html
Once logged in as Admin, users can Manage Categories. Users click on the Add Category button, and are taken to a form where they can input the name of a new category. Users click on the Add Category button to have the category added. The new category appears under the prepopulated categories. The new category can be edited. Users can cancel the edit, or enable their changes by clicking on the Edit_Category button. The new category can be deleted by clicking on the delete button. A warning pop up message appears to notify the user that this cannot be undone. Users can opt to cancel by clicking on the cancel button, or complete the delete by clicking the delete button.

**Related user story addressed:**
[6] As a parent, I want to be able to find a collection of words that are age appropriate for my child to learn to translate into Lithuanian.

## edit_category.html
Admin can edit the pre-populated categories, and any categories they have added, by clicking on the edit button. In the Edit Category form, admin can edit the category name. admin can opt to cancel by clicking on the cancel button, or complete the edit by clicking on the Edit_Category button.

## edit_words.html
When a user searches for a word, and the word is returned, they have the option to edit the word. The edit function allows the user to change the category, English word for example the spelling, the Lithuanian translation, useful information, and how the word is used in a sentence. To complete the editing, users click the Edit Word button at the bottom of the form. 

Users can also delete the word by clicking on the delete button. If a user opts to delete, a pop up appears with a warning message, reminding the user that the action cannot be undone. Users can then click delete or opt to cancel.

## manage_categories
Once logged in as admin, users can Manage Categories. Users can add a category by clicking on the Add Category button. Existing categories can be deleted or edited. If a user opts to delete the category by clicking on the delete button, a pop up message warning tells the user that this action cannot be undone. Users can choose to delete, or cancel the deletion. If a user opts to edit a category, they click on the edit button and are taken to  the Edit Category form where users can edit the category name. Users can opt to cancel by clicking on the cancel button, or complete the edit by clicking on the Edit_Category button.

# Future Features
- Contact for adding categories - I would like to add a contact form for users to request new categories.
- Click to hear pronunciation - I would like to add a feature where you have a 'listen event' on a word so you can hear the pronunciation.
- Capture email addresses - If I was to offer the website out to the world, I would capture email addresses when users register.
- Username/password reset functionality - I would like to include this feature for users to be self serving if they forget their log in details.
- Error message - My website does not have any error's but i will look to include 500/400 error messaging.

# Deployment
### Requirements for Deployment
- Gitpod
- Python3 to run application
- PIP to install all app requirements
- Database = MongoDB 
- Heroku account

### GitHub setup

Navigate to my Repository: https://github.com/Leefarmer83/Translate-It

Steps taken for setup:
1. Used template provided by [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Create new repository from template page
3. Install flask: pip3 install Flask
    - Details for env file:
            - import os
            - os.environ.setdefault("IP", "add here")
            - os.environ.setdefault("PORT", "add here")
            - os.environ.setdefault("SECRET_KEY", "add here")
            - os.environ.setdefault("MONGO_URI", "add here")
            - os.environ.setdefault("MONGO_DBNAME", "add here")

4. Create files: touch app.py, create gitignore and put in: env.py and __pycache__/
5. For Heroku create: pip3 freeze --local > requirements.txt
6. Then tell what file runs the app - echo web: python app.py > Procfile
7. Now we want Flask to communicate with MongoDB:
    - pip3 install flask-pymongo
    - pip3 install dnspython
    - pip3 freeze --local > requirements.txt (Make sure all requirements are called out in the file)
8. Now you can update heroku with Mongo URI

If you wish to clone my repository, information on how can be found [here.](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

## Deploy to Heroku

The project was connected to Heroku using automatic deployment from my GitPod repository:

**Note:** Please make sure you have already created your new repo in Github and have a env.py file to store your sensitive data.

1. In Gitpod create requirements.txt and Procfile files using the commands below (mentioned above):
   - $ pip3 freeze --local > requirements.txt
   - $ echo web: python app.py > Procfile

2. Log into Heroku and from your dashboard click create new app.

3. Enter your App name and choose the appropriate region, then click Create app.

4. From the Heroku deploy tab, select the Deployment method GitHub.

5. Connect to GitHub section make sure your GitHub profile is displayed.

6. Your repo should now be displayed below, click Connect.

7. Go to the Settings tab on Heroku, scroll to the Config Vars section, and click Reveal Config Vars. 

   Enter variables (key and value) contained in the env.py file.
    - IP
    - PORT
    - SECRET_KEY
    - MONGO_URI
    - MONGO_DBNAME

8. Push requirements.txt and Procfile to the repository.

9. Click Enable Automatic Deploys. Then under Manual deploy click Deploy Branch.



## Credits

### Content
- The concept, design and text for this project was created by the developer. 

### Media
- Images used are from a free image website: https://www.shutterstock.com/.

### Code
- Code was primarily inspired by the Task Manager mini project tutorials. 

# Acknowledgements

Special thanks to my Code Institute Mentor Gerard McBride for his support and time.
Also, thanks to Igor (tutor support), I have not used tutor support until this project, I had one issue that was driving me crazy, Igor helped me to understand where I was going wrong.