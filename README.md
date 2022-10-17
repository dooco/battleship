
# BATTLESHIP

- [BATTLESHIP](#battleship)
- [Goals](#goals)
  * [User Goals](#user-goals)
  * [Owner Goals](#owner-goals)
- [User Experience](#user-experience)
  * [User Stories](#user-stories)
    + [First Time User](#first-time-user)
    + [Returning User](#returning-user)
    + [Regular User](#regular-user)
- [User Manual](#user-manual)
- [Design](#design)
    + [Colours](#colours)
    + [Graphics](#graphics)
  * [Technical Design](#technical-design)
    + [Flow Diagram](#flow-diagram)
    + [Data Models](#data-models)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Libraries](#libraries)
    + [Built in Libraries](#built-in-libraries)
    + [Third Party Libraries](#third-party-libraries)
  * [APIs](#apis)
  * [Tools and Frameworks](#tools-and-frameworks)
- [Features](#features)
  * [Title](#title)
  * [Rules](#rules)
  * [Winners Table](#winners-table)
  * [Login](#login)
  * [Game](#game)
    + [Populate Boards](#populate-boards)
    + [Choose Co-ordintes](#choose-co-ordintes)
  * [Game progress](#game-progress)
  * [End Game](#end-game)
- [Deployment](#deployment)
  * [Heroku Set-up](#heroku-set-up)
- [Validation](#validation)
  * [PEP8](#pep8)
- [Testing](#testing)
- [Bugs](#bugs)
- [Limitations and further improvements](#limitations-and-further-improvements)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Goals

## User Goals
- User to play an interactive game of Battleship with computer as opponent.

- A user-friendly interface to navigate the game, with directions on how to play and prompts for user to interact with game.

## Owner Goals

- Present user with a challenging, interactive game of battleship.

# User Experience

## User Stories

### First Time User

1. As a first time user, I want to be able to play the game Battleship.

2. As a first time user, I want to be able to read the instructions of the game.

3. As a first time user, I want to navigate the game with ease.

4. As a first time user, I want to be guided on correct inputs to game.

### Returning User

5. As a returnng user, I want to play a game against the computer which has a different arrangement each time.

6. As a returning user, I want to have the choice to re-play the game.

7. As a returning user, I want to be visually stimulated by colours and graphics of game.

### Regular User

8. As a regular user, I want to view high score table.

9. As a regular user, I want to be able to log on and increase my score by winning game.

10. As a regular user, I want to save my user name and score.


# User Manual

# Design

### Colours

Colours used in game are implemented using Colorama third party library. The library provides a set of basic colours and styles. The game uses a basic set of three colours, Red, Blue and Magenta and uses the Bright style to intensify the imagery.

### Graphics

With a basic terminal as presented for this project the graphics for headers and messages was created with an ascii art generator. An option for future development would investigate the use of features from the 'Textual' third party library.

## Technical Design

### Flow Diagram

![Flow Chart](/images/battleship_flow_chart.png)

### Data Models

The board layout consisted of a list of list. As the board was configures as 8 x 8 the strings consisted of eight space characters in each row and with eight rows on start up. This list of lists was used for four boards used in the game: player_board, player_board_guess, computer_board, computer_board_guess. Each board are populates with hit or miss characters "X" or "@" as the game progresses. Each of the guess boards are printed on teminal (in user friendly output) throughout game to give palyer feedback.


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

GSpread, a library that interfaces wit google sheets, allowing program to read and write to google sheets.
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

- Lucidchart for generating code flow chart

- cloudconvert.com Used to convert numbers spreadsheet to jpg format 

# Features

## Title

The title, or header, consists of the word 'BATTLESHIP' created by an ascii art generator in bright blue. The text fills the 80 pixel wide terminal and is held in position at the top of the screen by sending a clear screen cypher, followed by the header, when a new table is to be displayed. 

![Battleship header](/images/battleship_header.png)

## Rules

There is a brief set of instruction displayed below the header. 

![Instructions](/images/instructions.png)

## Winners Table

At game start the winning table of most recent wins is displayed outlining stages of game and how to play.

![Winner's recent table](/images/win_table.png)

## Login
The player is prompted with option to login as new player or an existing player. On selection, of either N or E, the playere is prompted to enter an access code which ensures that the player's information is not accessable to other players. On completion of new player details the player name, access code and score of zero is posted to winning table google sheet.

## Game 

After player enters their details, whether new or existing player, the game progressses to the first stage oif the game - populating the game boards.

### Populate Boards

Every game starts with the computer randomly placing five ships on the computer board followed by the player being prompted for the direction ('V'ertical or 'H'orizontal) and start co-ordinates (digit, 1-8 followed by letter, a-h) of player's five ships. Each player has five ships, one of two spaces, two of three spaces, one of four spaces and one of 5 spaces on the board. The placing of ships on the board routine checks that each ship does not exceed the edge of the board or overlaps another ship. 

![Battleship-descriptors](/images/five_ships.png)


### Choose Co-ordintes

After the player has placed their five ships on the board, the process of seeking out the opposition's ships and hitting them starts. Player is prompted for co-ordinates (digit followed by letter) for strike to land. If the co-ordinates correspondsto one of the co-ordinates where the opposition's ship is located the program marks this with an 'X' on the board and an '@' where a miss occurs.

## Game progress

The program iterates through as many guesses as needed, making sure not to allow co-ordinates already guessed or out of range co-ordinates, until all the opposition ship's have been hit. Both the player's guess board and the computer's guess board are displayed, showing whether computer or player has had a hit or miss, after each iteration.

## End Game

The game loops through computer randomly selecting co-ordinates and player inputing co-ordinates, and checking for hit, until either player reaches 17 hits where the end of game routine displays PLAYER WINS or PLAYER LOOSES ascii to art graphic on screen. Player score is updated to google sheet and player is prompted to quit or start a new game.


# Deployment

## Heroku Set-up

- Register with email for a new account in Heroku.

- On welcome to heroku home page create a new application by clicking on 'Create new app'. On next page give your app a unique name and fill out where you are from (USA or Europe) and press 'create app'. 

- Go to gitpod and open 'creds.json' file and copy the entire document to clipboard.

- Go to settings tab and click on Reveal Config Vars and set key to 'CREDS'

- Paste contents of clipboard to value section of key.

- Stay with the Config Vars section and set the key to 'PORT', and the value to '8000'

- Scroll down to the build packs section and click on 'Add buildpack', add Python and NodeJS to the application, making sure Python is first of Python and NodeJS selection.

- Go to Deploy tab. Select GitHub as deployment method and enter 'battleship' in search in GitHub search box.

- Scroll down to automatic deploys and select 'Enable Automatic Deploys'.

- You should get a message indicating app was successfully deployed and a button linking to deployed app will appear.

- Clicking on button will bring you to deployed app where you press 'Run Program' to run your app.


# Validation


## PEP8

As the PEP8 format checker was not available the VS interpreter was used to validate code.

# Testing

Each section of code was tested manualy at the creation of each section of code entry.

The use of print statements was used to show different variable values and to see if code was working.

Print statements were also used as placeholders for functions and decision checks to show code was called.

![Code and user experience validation](/images/battleship_validation%20.jpg)

# Bugs
After testing it a bug became evident in that when deciding to play again the reset_boards function didnt clear boards.

# Limitations and further improvements

- For further improvements the introduction of computer intelligence where computer's make_move choice would have some next space algorithm built in instead of just random choice.

- Log in function where user can log their username and password and game would keep a record of scores securely.


# Credits

Fot insights on how to set up the game: Daniel F Moisset github account:dmoisset

The Code Institute's Portfolio Project 3 Scope video

# Acknowledgements

My Mentor, Ronan McClelland , for continuous helpful feedback.

Tutor support at Code Institute for their support.
