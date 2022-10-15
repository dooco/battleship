
# BATTLESHIP
# Table of  Contents
# Goals
## User Goals
## Owner Goals
# User Experience
## User Stories
### First Time User
### Returning User
### Regular User
## Owner Stories
# User Manual
# Design
## Technical Design
### Flow Diagram
### Data Models
### Colours
# Technologies Used
## Languages
- Python3
- HTML
- CSS
## Libraries

### Built in Libraries
- random
- 
### Third Party Libraries
- Google OAuth
Allows users to share specific data with an application while keeping usernames, passwords and other information private.

- GSpread
GSpread 
A python library that interfaces wit google sheets, allowing program to read and write to google sheets.
- Colorama 
This third party library features foreground and background colours and styles for highlighting elements on display. Introduction of colour augments the user experience.

## APIs
- Google Sheets API
- Google Drive API
## Tools and Frameworks
- Git
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- GitHub:
GitHub is used to store the projects code after being pushed from Git.

- Heroku
Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps.

- VS Code:
Integrated Development Environment used to develop the Python code for the project.

- Markdown Table of Contents
Table of contents generated: https://ecotrust-canada.github.io/markdown-toc

- ASCII Art Generator
Computer text art which is achieved by the smart placement of typed special characters or letters to make a visual shape that is spread over multiple lines of text.

# Features
## Title
## Rules
## Winners Table
## Login
## Game 
### Populate Boards
### Choose Co-ordintes
## Game progress
## End Game
# Deployment
## Heroku
# Validation
## PEP8
# Testing
# Bugs
# Credits
# Acknowledgements







* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!