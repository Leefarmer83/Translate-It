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