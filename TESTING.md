# Testing

[return to README.md](https://github.com/Leefarmer83/Translate-It)

# Validation
### Websites used
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [PEP8 Validator](http://pep8online.com/)

HTML Validation message are below, under each feature.

# base.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
When not logged in | Log in and Register links should display | pass
When logged in | A link to my profile page add words show| pass
Clicked Log In | Display login.html | pass
Clicked Register | Display register.html | pass
Clicked  Profile page | Display my profile page. Profile.html/<username> | pass
Clicked Home | Display index.html | pass
When logged in as admin | Manage categories shows | pass
When viewing on mobile | Burger menu shows | pass
Click on burger menu | Mobile side menu comes in from right | pass
Check all links | All links take user to desired location | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

There is three warning messages: "Warning: Empty heading." this is due to fontawsome icons taking the place of text.

# index.html (Home)
action taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on search word now | Navigates to words.html | pass
Clicked on every category (9) | Taken to the category and only words that belong to that category show | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

# register.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Only used 1 to 4 letters for username  | Section turns red and message states please match requested format| pass
Did not enter letters/numbers in the username section | Section turns red and message states please fill out field when trying to submit| pass
Used 5 to 15 letters for username  | Section turns green | pass
Tried to enter same username that has already been registered | Flash message stating already in use | pass
Tried to use more than 15 letters for username  | Section does not allow | pass
Only used 1 to 4 letters for password  | Section turns red and message states please match requested format| pass
Did not enter letters/numbers in the password section | Section turns red and message states please fill out field when trying to submit| pass
Used 5 to 15 letters for password  | Section turns green | pass
Tried to use more than 15 letters for password  | Section does not allow | pass
Clicked on Log In | Takes you to login page| pass
Enter a successful username and password | Flash message stating successful registration| pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

Corrected error = The element a must not appear as a descendant of the button element. Took out the button, it was not needed.

# login.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Only used 1 to 4 letters for username  | Section turns red and message states please match requested format| pass
Only used 1 to 4 letters for password  | Section turns red and message states please match requested format| pass
Enter a wrong username or password | Flash message stating wrong username or password | pass
Enter a successful username and password | Flash message stating successful log in| pass
Clicked on Register button | Takes you to Register page| pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

Corrected error = The element a must not appear as a descendant of the button element. Took out the button, it was not needed.

# profile.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Log in | Username shows | pass
Log in | Created words from user shows | pass
Clicked on add words | Taken to word creation page| pass
Clicked on search | Taken to word page| pass
Clicked on edit | Allows user to edit words| pass
Clicked on delete | Pop up message asking for confirmation| pass
Clicked on confirm deletion | Word is deleted from profile and library| pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

# words.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Search for a word that is in the library | Only that word shows and/or same word (good as an example) | pass
Search for a word that is not in the library | No words message shows | pass
Search for a word and then hit reset | All words searched for are removed and shows all words | pass
Scroll down the page | All words show in alphabetical order| pass
Words created by user | Delete and Edit button shows| pass
Words not by user | Delete and Edit button do not show| pass
Click on the tabs on each card to show individual data | Correct information is under desired tab| pass
Click on register and log in links on page | Taken to the correct location| pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

# word_cat.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on each category on home.html | Object id passed category name and created words under category | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

# add_words.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on add word | Taken to add word form | pass
Clicked on select category| All categories show for selection | pass
No category selected| section error message and section turns red | pass
No English word added| section error message and section turns red | pass
No Lithuanian word added| section error message and section turns red | pass
No Useful Information added| section error message and section turns red | pass
No Example of word used in a sentence added| section error message and section turns red | pass
All words entered correctly | Word is added to library and flash message shown| pass
Successful word added | word added to profile page | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

# add_category.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on add category | taken to add category page| pass
Add new category | New category shows on manage category page and index.html page | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

## Important - To test category functionality you must be logged in as admin, please use the following credentials:
**Username: admin**

**Password: Budnlee5**

Here you can test; adding, deleting and editing categories. 
## This will be deleted after the project is assessed by code institute.

# edit_category.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on edit category | taken to edit category page| pass
Edit category | Category is edited and shows on manage category page and index.html page | pass
Clicked on cancel | Taken back to manage category page | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

## Important - To test category functionality you must be logged in as admin, please use the following credentials:
**Username: admin**

**Password: Budnlee5**

Here you can test; adding, deleting and editing categories. 
## This will be deleted after the project is assessed by code institute.


**Bug Fix**
I was having problems deleting words and Categories, every time i deleted, it always deleted the first word. This was down to the ID not being unique, I added {{ loop.index }} in the ID to fix this.


# edit_words.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
If the user created the word, click on edit word | taken to edit word page| pass
Edit word | word is edited and shows on words page | pass
Clicked on cancel | Taken back to word  page | pass
If the user created the word, click delete word | Pop up message shows| pass
Confirm delete word | word is deleted from words page | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

**Bug Fix**
I was having problems deleting words and Categories, every time i deleted, it always deleted the first word. This was down to the ID not being unique, I added {{ loop.index }} in the ID to fix this.


# manage_categories.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Only Admin can see this section | Only shown to admin user | pass
Clicked on edit category button | User taken to edit category | pass
Clicked on delete category button | User taken to pop up message | pass
Clicked on add category button | User taken to add category | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

## Important - To test category functionality you must be logged in as admin, please use the following credentials:
**Username: admin**

**Password: Budnlee5**

Here you can test; adding, deleting and editing categories. 
## This will be deleted after the project is assessed by code institute.

# Pronunciation.html
action taken | expected result | pass/fail
------------ | --------------- | ---------
Mobile view | alphabetical view is scrolling | pass

**HTML validator:**
Errors are seen, this is expected due to the validator not handling Flask inside the HTML

# CSS file
W3C CSS Validator results for TextArea (CSS level 3 + SVG)
**Congratulations! No Error Found.**
This document validates as CSS level 3 + SVG !

# Java Script file
There are 7 functions in this file.

Function with the largest signature take 0 arguments, while the median is 0.

Largest function has 7 statements in it, while the median is 3.

The most complex function has a cyclomatic complexity value of 3 while the median is 2.

Two warnings
19	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
20	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
**This code was copied from Code Institute as a work around**

# Python file
Code has been given the "All right". 