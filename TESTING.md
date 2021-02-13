# Testing

[return to README.md](https://github.com/Leefarmer83/Translate-It)

# base.html


# index.html (Home)
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on search word now | Navigates to words.html | pass
Clicked on every category (9) | Taken to the category and olny words that belong to that category show | pass


# register.html
## Testing
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
Cliked on Log In | Takes you to login page| pass
Enter a successful username and password | Flash message stating succesful registration| pass

# login.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Only used 1 to 4 letters for username  | Section turns red and message states please match requested format| pass
Only used 1 to 4 letters for password  | Section turns red and message states please match requested format| pass
Enter a wrong username or password | Flah message stating wrong username or password | pass
Enter a successful username and password | Flash message stating succesful log in| pass
Cliked on Register button | Takes you to Register page| pass


# profile.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Log in | Username shows | pass
Log in | Created words from user shows | pass
Clicked on add words | Taken to word creation page| pass
Clicked on search | Taken to word page| pass
Clicked on edit | Allows user to edit words| pass
Clicked on delete | Pop up message aking for confirmation| pass
Clicked on confirm deletion | Word is deleted from profile and library| pass


# words.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Search for a word that is in the library | Only that word shows and/or same word (good as an example) | pass
Search for a word that is not inthe library | No words message shows | pass
Search for a word and then hit reset | All words searched for are removed and shows all words | pass
Scroll down the page | All words show in alphabetical order| pass
Words created by user | Delete and Edit button shows| pass
Words not by user | Delete and Edit button do not show| pass
Click on the tabs on each card to show ndividual data | Correct information is under desired tab| pass
Click on register and log in links on page | Taken to the correct location| pass


# word_cat.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on each category on home.html | Object id passed category name and created words under category | pass

# add_words.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on add word | Taken to add word form | pass
Clicked on select category| All categories show for selection | pass
No category selected| section error message and section turns red | pass
No English word added| section error message and section turns red | pass
No Lithuanian word added| section error message and section turns red | pass
No Useful Information added| section error message and section turns red | pass
No Example of word used in a sentence added| section error message and section turns red | pass
All words entered correctly | Word is added to library and flash messege shown| pass
Successful word added | word added to profile page | pass

# add_category.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on add category | taken to add category page| pass
Add new category | New category shows on manage category page and index.html page | pass

# edit_category.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Click on edit category | taken to edit category page| pass
Edit category | Category is edited and shows on manage category page and index.html page | pass
Clicked on cancel | Taken back to manage category page | pass

# edit_words.html
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
If the user created the word, click on edit word | taken to edit word page| pass
Edit word | word is edited and shows on words page | pass
Clicked on cancel | Taken back to word  page | pass
If the user created the word, click delete word | Pop up message shows| pass
Confirm delete word | word is deleted from words page | pass

# manage_categories
## Testing
action taken | expected result | pass/fail
------------ | --------------- | ---------
Only Admin can see this section | Only shown to admin user | pass
Clicked on edit category button | User taken to edit category | pass
Clicked on delete category button | User taken to pop up message | pass
Clicked on add category button | User taken to add category | pass