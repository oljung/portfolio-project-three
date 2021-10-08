# Mastermind Poker
Mastermind Poker is an app containing two logic based games, Mastermind where you guess a sequence of numbers, and poker where you play a 5-card poker hand against the AI.

Link to deployed site: https://mastermind-poker.herokuapp.com/

![responsiveness](assets/images/readme-images/responsive-start.png)


### Table of Contents
**[1. User Experience](#1-user-experience)**<br>
**[2. Features](#2-features)**<br>
**[3. Technologies Used](#3-data-model)**<br>
**[4. Testing](#4-testing)**<br>
**[5. Deployment](#5-deployment)**<br>
**[6. Credits](#6-credits)**<br>


## 1. User Experience

### 1.1 Project introduction

The goal of this app is to provide players with a logic based puzzle in the form of Mastermind, challenging players to use deduction to reach the target secret code. The other part is to have players using probability by asking them to swap cards in their poker hand in an attempt to get a better ranking hand, thus beating the AI. Here players will have to wiegh risk against reward in order to be successful.
### 1.2 Design guidelines

As the entire app is run in a terminal, the amount of information shown is important. There needs to be enough of it for the user to actually use the app, but not to much so that important information is missed. As a way to resolve this, empty ´´´print()´´´ calls where used to create space between lines.

### 1.3 Project goals

- Provide a challenging yet funny game that tests the players logic and probability thinking.

- Provide more than one type of game and challenge in the app.

- Allow players to store and view highscore in order to compete with themselves and other players.

### 1.4 Target audience

The main audience for this game is players who enjoy logic puzzles or the probability calculation of poker. Even though some players may have limited experience, many will likely have experience of similar games. The main types are therefore:

- User who have little experience with this type of game or little experience of games in general: <br>
**Needs:** Information about how to play the game that is sufficient and provides examples on what to do.<br>
**Goal:** Make every step of each game easily understandable  with only the information provided in the app.<br>
**How:** Make sure that whenever a user is asked for input, it is explained what the program is asking for and how to properly give said input.

- User who used to play similar games before and are looking for a logic challenge:<br>
**Needs:** A way to test their logic skills and compete against themselves or others.<br>
**Goal:** Have a fully functioning highscore system.<br>
**How:** Using google sheets and API to update a worksheet and get data from worksheet containing results so far.

### 1.5 User stories

- As an owner, I want to make sure new users are able to find sufficent information to play the game
- As an owner, I want to make sure that the game is logically consistent and that players get the expected results
- As an owner, I want to make sure the highscore is available and can be sorted using different keys
- As a user, I want to play a game of Mastermind
- As a user, I want to play a game of Poker
- As a user, I want a logic challenge that is consistent and understandable. I want the results to reflect how I play
- As a user, I want to be able to save my score
- As a user, I want to be able to view hoghscore and compare my own score against that

### 1.6 How To Play

- Mastermind:
    - You will be asked to chose the standard or custom game. Only the standard game will keep track of highscore. If you choose the custom game, you will get to select how many numbers to guess, and the range of numbers the game will use.
    - When you have selected game type, the game will randomly generate a secret code for you. You will now be asked to enter a 4 digit number containing your guess.
    - The game will tell you how you did by showing result, and it wil look like this: <br>
    ![mastermind guess](assets\readme-images\mastermind-guess.png)

### 2.1 Existing features



### 2.2 Features left to implement


## 3. Data Model

## 4. Testing

### 4.1 Validator testing


### 4.2 Bugs
There are currently no known unfixed bugs in the project

### 4.4 Testing user Stories

## 5. Deployment


## 6. Credits

