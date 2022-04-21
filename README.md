## Group 1
# Dan's Bagel Shop ReadMe
## Organization and Name Scheme
We have the following folder organization so far:
- Archive
- DansDjango
- docs
- README.md

Archive/ holds folder and files we aren't currently using but want to save.
DansDjango/ is the Django project that we are running. Within it, we have Django specific folders and files.
docs/ holds all of our documenation.
README.md is the file you are currently reading.

## Version-control procedures
All members of our group have full admin privileges to the project. We handle merge requests when we need to and discuss conflicts.
We use Git and Github to manage version control.

## Tool Stack Description and Setup Procedure
Since this project is largely web-based, we will have a front-end web development stack of Django, which utilizes Python, and HTML, JavaScript, and CSS. For the database, we will use Django’s built-in SQLite, and interface all of these languages/tools using the model-view-controller software design pattern.
For the back-end of our web development stack, we will use Nginx and Gunicorn.
We will use VSCode and Vim as text-editors.
This is subject to change.

## Build Instructions
In order to run the project, you need to go to DansBagelShop/DansDjango within a terminal. That terminal needs to be able to run Python3 and Django. Once you are within the DansBagelShop/DansDjango folder you need to build migrations using "python manage.py migrate". After, you can run the project using "python manage.py runserver". This will run the server. Open your browser and go to 127.0.0.1:8000/login. 
Once the page comes up, click on register new account and put in the necessary information. If it's not put in correctly, you will be given an error. Once you have your account set up, you are able to login and when you login you will be redirected to the home page, where you will be able to navigate to the different pages. The Menu page will allow you to update the menu and the inventory page will allow you to update the inventory.

## Unit Testing Instructions
We mostly need to validate forms. Currently we have the role navigation turned off while we finish implementing placing orders in the system. Due to this feature turned off, most unit testing will not function as it should otherwise.

Security Testing:
All user account forms currently have all necessary validation in place. User's will need unique emails, and usernames in order to create an account. As seen in the register page, the user cannot input an invalid email address, username, or password and allow the form to submit. All necessary fields have input instructions implemented for user account creation, login, and account settings. Each field has been tested by numerous entries respective to their criteria. All new account roles currently default to 'customer' role and are validated in the admin page.

## System Testing Instructions
Look at the Build Instructions in this README.md. You can test the whole system using the build instructions and navigating to pages currently implemented.
## Other Development Notes
N/A
