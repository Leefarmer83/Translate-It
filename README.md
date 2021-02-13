# Translate It!

This is a website designed to teach children from the age of 6 years and over how to build their vocabulary and conversation skills in Lithuanian through the creation of a library of English words that are then translated into Lithuanian. 

The site features an individual word search, categories of words, the meaning of a word, helpful information related to a word, as well as how to use them in a sentence, to support their use in conversation. 


The website is deployed live at [https://my-translate-it.herokuapp.com/](https://my-translate-it.herokuapp.com/)



# Table of Contents

- [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Project Wireframe and Design Process](#Project-Wireframe-and-Design-Process)
- [Features](README.md#features)
    - [base.html](README.md#basehtml)
    - [index.html (Home)](README.md#indexhtml-home)
    - [register.html](README.md#registerhtml)
    - [login.html](README.md#loginhtml)
    - [profile.html](README.md#profilehtml)
    - [words.html](README.md#wordshtml)
    - [word_cat.html](README.md#word_catshtml)
    - [add_words.html](README.md#addwordshtml)
    - [my_words.html](README.md#mywordshtml)
    - [pronunciation.html](README.md#pronunciationhtml)
    - [add_category.html](README.md#add_categoryhtml)
    - [edit_category.html](README.md#edit_categoryhtml)
    - [edit_words.html](README.md#edit_wordshtml)
    - [manage_categories](README.mdmanage_categorieshtml)
    - [Future Features](README.md#future_features)
- [Technologies Used](README.md#technologies-used)
- [Testing](README.md#testing)
- [Deployment](README.md#deployment)
    - [Live Deployment](README.md#live_deployment)
    - [Local Deployment](README.md#local_deployment)
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
- Build a English to Lithuanian translation library, including helful information, example sentances and pronouncing tips.


# User Stories
- [1] As a user, I want to have a library of words that are translated into Lithuanian so that I can learn to use them in a conversation. 
- [2] As a user, I want to be able to add more words with Lithuanian translation to a library as my English vocabulary expands. 
- [3] As a user, I want to be able to add useful information to any word I create, and show know how to use the word when speaking. 
- [4] As a user, I want to be able to find a guide that shows me  how to pronounce a Lithuanian word. 
- [5] As a user, I want to be able to find related words easily. 
- [6] As a parent, I want to be able to find a collection of words that are age appropriate for my child to learn to translate into Lithuanian.
- [7] As a parent, I want to be able to have some control over the words my child learns, so that I can focus their learning.

# Project Wireframe and Design Process
- [wireframe design](https://github.com/Leefarmer83/Translate-It/tree/master/static/wire_frames)
    - [Home](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/home.png)
    - [word](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/words.png)
    - [add_word](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/add_word.png)
    - [add_category](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/add_category.png)
    - [catagory_information](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/category_information.png)
    - [login](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/login.png)
    - [register](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/register.png)
    - [word_information](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/word_information.png)

This was my inital design for the website. During development the flow of data and website design changed for the better. 
The biggest change was the information on the translation, materilize had a great card feture that helpped with selecting data.

### Design
The strategy for the design was to create an easy using website that naturally took the user on a seamless journey to first find a word, via word search or category search. If a word was not found they are then asked to log in and add it themself. If the user adds a word their profile page will host only their words and the word is also added to the library for other users.

### Database design
The thought process behind adding words was to have the user stick to a template that would naturally add words to the existing library. Users will need to select a category, state the word, the translation of that word, useful information, and an example of the word in a sentence.
[Database collection structure in MongoDB](https://github.com/Leefarmer83/Translate-It/blob/master/static/wire_frames/mongoDB_data_stucture.png)

### User structure
Anyone visiting the site can search words and categories.
Users can only add words once they are registered and logged in. 
Users can only delete their created words.
Users can only edit their own created words.
The Admin can only add, delete and edit categories.
User with access to database can delete, add and edit all.

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

# base.html
All pages will inherit html from base.html. The website header contains the website navbar and footer, flash messaging. User rulstructurees is set in the base.html.

# index.html (Home)
The home page features a search function where users can search for an individual word by clicking on the search button. There is also a Categories section that features 9 prepopulated categories of words for users to search on.

# register.html
On the Register page, users create a username and password that must be alpha-numeric and between 5 and 15 characters long for successful registration. 
This guidance is noted on the page to reduce friction for the user when registering. Once the user has chosen a username and password, they click the login button to enter the library. If a user chooses a username that already exists in the system, a banner message loads to let them know that username is not available. Users who may already have registered can click the login button at the bottom of the page to be taken to the login screen.

# login.html
On the Log In page, users can input their username and password, and select the Log In button to login. If a user enters an incorrect username or password, a banner pops up at the top of the page to let them know they have entered an incorrect credential. Unregistered users who land on this page are directed to register by clicking the register button. When a user logs out, a banner message pops up at the top of the page to let them know they have logged out successfully.

# profile.html
Once a user has registered, they land on the Profile page. The first time a user lands on this page, the page is empty, as the user has not added any words. Once a user has added words, they can see all of their words that they have added to the library. These words are displayed in the same card format as words on the Words page, with the translation, helpful information, and how the word is used in a sentence. Users can edit or delete these words. Users can add words or search for words using the buttons at the bottom of the page.

# words.html
When a user clicks on individual word search on the home page, they land on the Words page. Here the user can enter a word, reset the search to start again, or search for the word if they are happy with the entry they made. If a user opts to reset, the search bar clears and they are free to input another word. 
If a user inputs a word into search, and it is not in the prepopulated library, the user can add it themself if they are logged in. 
On the Words page, users will also find all the words from the prepopulated categories listed in alphabetical order, with its translation, and the option to select useful information, and how the word is used in a sentence. Users can also choose to edit or delete the words, if they created the word. 
Users also have the option to register or login from this page, as words can only be added once logged in.

# word_cat.html
When a user clicks on a category on the home page, they land on the Categories page. Here all the prepopulated words from the selected category are listed in alphabetical order, with the word’s translation, and the option to select useful information, and how the word is used in a sentence. Users can also use the return button at the bottom of the page to return to the main categories.

# add_words.html
If logged in, users are able to add a word to Translate It! To do this, they select a category using the drop down menu. They then add the English word, the Lithuanian translation, useful information, and how the word is used in a sentence. To have the entry added, users click the Add Word button at the bottom of the form.

# my_words.html
Once a user has added words, they can see all of their words that they have added to the library. These words are displayed in the same card format as words on the Words page, with the translation, helpful information, and how the word is used in a sentence. Users can edit or delete these words. Users can add words or search for words using the buttons at the bottom of the page.

# pronunciation.html
When a user selects Pronunciation from the toolbar, they land on the Pronunciation page. The table on this page lists the letters from the Lithuanian alphabet, how that letter sounds in English, together with an English word to illustrate an example of the sound in an English word.

# add_category.html
Once logged in as Admin, users can Manage Categories. Users click on the Add Category button, and are taken to a form where they can input the name of a new category. Users click on the Add Category button to have the category added. The new category appears under the prepopulated categories. The new category can be edited. Users can cancel the edit, or enable their changes by clicking on the Edit_Category button. The new category can be deleted by clicking on the delete button. A warning pop up message appears to notify the user that this cannot be undone. Users can opt to cancel by clicking on the cancel button, or complete the delete by clicking the delete button.

# edit_category.html
Admin can edit the pre-populated categories, and any categories they have added, by clicking on the edit button. In the Edit Category form, admin can edit the category name. admin can opt to cancel by clicking on the cancel button, or complete the edit by clicking on the Edit_Category button.

# edit_words.html
When a user searches for a word, and the word is returned, they have the option to edit the word. The edit function allows the user to change the category, English word for example the spelling, the Lithuanian translation, useful information, and how the word is used in a sentence. To complete the editing, users click the Edit Word button at the bottom of the form. 

Users can also delete the word by clicking on the delete button. If a user opts to delete, a pop up appears with a warning message, reminding the user that the action cannot be undone. Users can then click delete or opt to cancel.

# manage_categories
Once logged in as admin, users can Manage Categories. Users can add a category by clicking on the Add Category button. Existing categories can be deleted or edited. If a user opts to delete the category by clicking on the delete button, a pop up message warning tells the user that this action cannot be undone. Users can choose to delete, or cancel the deletion. If a user opts to edit a category, they click on the edit button and are taken to  the Edit Category form where users can edit the category name. Users can opt to cancel by clicking on the cancel button, or complete the edit by clicking on the Edit_Category button.

# Future Features
contact for adding categories
Click to hear function on words and pronunciation
Capture email addresses if website goes public 
forgot/reset password functionality 







Colour and font
Colour and font were taken into account in order to make the interface simple to navigate and use, but also incorporated best practices in terms of accessibility, in order to cater for users of all learning abilities. 

Features

Technologies Used

Link to Websites

Testing

Deployment

Credits

Content

Media

Acknowledgements