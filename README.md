# Mastermind Poker
Mastermind Poker is an app containing two logic based games, Mastermind where you guess a sequence of numbers, and poker where you play a 5-card poker hand against the AI.

Link to deployed site: https://mastermind-poker.herokuapp.com/

![responsiveness](assets/images/readme-images/responsive-start.png)


### Table of Contents
**[1. User Experience](#1-user-experience)**<br>
**[2. Features](#2-features)**<br>
**[3. Data Model](#3-data-model)**<br>
**[4. Testing](#4-testing)**<br>
**[5. Deployment](#5-deployment)**<br>
**[6. Credits](#6-credits)**<br>


## 1. User Experience

### 1.1 Project introduction

The goal of this app is to provide players with a logic based puzzle in the form of Mastermind, challenging players to use deduction to reach the target secret code. The other part is to have players using probability by asking them to swap cards in their poker hand in an attempt to get a better ranking hand, thus beating the AI. Here players will have to wiegh risk against reward in order to be successful.
### 1.2 Design guidelines

As the entire app is run in a terminal, the amount of information shown is important. There needs to be enough of it for the user to actually use the app, but not to much so that important information is missed. As a way to resolve this, empty ```print()``` calls where used to create space between lines.

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
- As a user, I want to be able to view highscore and compare my own score against that

### 1.6 How To Play

- Mastermind:
    - You will be asked to chose the standard or custom game. Only the standard game will keep track of highscore. If you choose the custom game, you will get to select how many numbers to guess, and the range of numbers the game will use.
    - When you have selected game type, the game will randomly generate a secret code for you. You will now be asked to enter a 4 digit number containing your guess.
    - The game will tell you how you did by showing result, and it wil look like this: <br>
    ![mastermind guess](assets\readme-images\mastermind-guess.png)
    - A number will mean that the number is correct, in this picture none of the guesses were correct.
    - A 'C' will mean that the number is in the code, but in the wrong position
    - A '-' means that the number is not included in the code.
    - Evaluate your result and make a new guess, and continue until you beat the code, the game will then tell you how you did and ask if you want another round, like this:<br>
    ![mastermind win](assets\readme-images\mastermind-won.png)
- Poker:
    - At the start of the game, you will be dealt 5 random cards, and the goal is to get the best poker hand.
    - You will be shown you hand, and asked to if you want to swap any cards. Here you can give a number between 0 (no cards will be swapped) and 5, swapping all cards.
    - Next you will enter a number, the lenght of the amount of cards you want to swap. If you want to swap card to, enter 2. If you want to swap card 1 and 4, enter 14. It will look like this:<br>
    ![poker swap](assets\readme-images\poker-swap.png)
    - As you can see, I decided to swap 2 cards, cards 1 and 3. After that new cards are dealt and the hand is sorted again.
    - After you swap the game will compare your hand against the hand of the AI and display both hands and declare a winner. It will look like this:<br>
    ![poker game over](assets\readme-images\poker-won.png)
    - Now you can decide to play another game or return to the main menu.
    - The winner of a hand is determined by who has the best ranking. If both hands are equal, say both have a pair, the best pair will win. If the pairs are also equal, the player with the best highcard wins. The rankings are as follows:
        - Highcard
        - Pair
        - Trips
        - Straight
        - Flush
        - Full House (trips and a pair)
        - Quads
        - Straight Flush
    - When both players have a highcard of equal rank, say both players have an ace, the card with the best suit will win. Suits are ranked as follows:
        - Clubs (lowest)
        - Diamonds
        - Hearts
        - Spades (highest)
- Both games will allow you to update highscores. If you play more than 5 rounds, you can compare your score against the top players of each game.

## 2. Features

### 2.1 Existing features
- Welcoming menu
    - Will welcome players and give short information about how to play the game<br>
    ![welcome menu](assets\readme-images\menu.png)
- Two seperate games, providing unique challenges to the player
- Mastermind menu and how to play
    - When you run the game mastermind, it will display a menu and let the player choose between two game modes<br>
    ![mastermind menu](assets\readme-images\mastermind-menu.png)
- Two game modes of Mastermind, one standard with 4 numbers in range 0-9, and one custom where the player can set the rules
- Poker menu and how to play
    - Running the game of poker will inform the player of how it is played, and link to further reading on what hand beats what<br>
    ![poker menu](assets\readme-images\poker-menu.png)
- Highscores for both games, with a menu for sorting based on different keys
    - The highscore table can be sorted based on rounds played, best score, top 5 averages and show games by only a specific player<br>
    ![highscore](assets\readme-images\highscore.png)


### 2.2 Features left to implement
- AI behavoir for the poker game
    - At this point, the AI doesn't try to improve its hand. In the future, an AI that swaps cards best on the highest probability to win should be a development goal. This is outside of the score for this project however


## 3. Data Model
Early on in the project I realized that there would be a lot going on, and many classes would be needed to handle the many different tasks of the app. I decided to break the app up into seperate modules, where one module contains one or more classes for one of these tasks. For instance, the mastermind module contains the class and methods needed for running one round of Mastermind, and the mastermindgame module then handles everything needed to run multiple rounds and saving score to use for highscore talbe. The modules and what they do:
- run.py
    - This module is the "main" program and is used to run the app. It imports menu.py and instanciates an object of the Menu class contained within. The constructor for the Menu class then does the rest
- menu.py
    - This module is the main menu of the app and handles the player choices and then runs the games or displays the highscore the user wants. It has one class, Menu and uses the modules mastermindgame.py, pokergame.py, worksheethandler.py, inputhandler.py and highscore.py
- inputhandler.py
    - This module contains one class used to handle user inputs. All methods of this class are static, and can thus be called without instanciating an object of the class. The methods validate user input before returning a value.
- worksheethandler.py
    - This module contains one class that handles imports and credentials needed to connect to the google sheet that contains the two worksheets with the highscore data. It has methods for getting the data from a worksheet and updating a worksheet with a new row of data. Like InputHandler class, the WorksheetHandler class use static methods.
- mastermindgame.py
    - This module imports inputhandler.py for handling user inputs and mastermind.py for running a round of the game. The module has one class, RunMastermind which handles game modes, player information and score. Using a ```prepare_highscore_item()``` method it can return the results of several rounds to the menu module for saving highscore
    - mastermind.py Contains the class Mastermind and also uses inputhandler.py for handling user inputs. It aslo imports random in order to generate a random sequence of numbers to be guessed. As long as some important conditions are met, the numbers will be unique.
- pokergame.py
    - Module for running a game of poker, storing player information and scores. The game uses inputhandler.py to handle user inputs and imports poker.py to run poker rounds. The module has one class, RunPoker and just as mastermindgame.py it has a ```prepare_highscore_item()``` it can use to return highscore item
    - poker.py Contains several classes needed to run a round of poker. Apparently, some rather complex logic is needed to determine the better poker hand. We won't be going in to too much detail here, but give a short rundown of what is what. The poker.py module imports inputhandler.py as well shuffle from the random module and the operator and copy modules provided by python. The classes in poker.py are:
        - Card: This class is represents a playing card in a deck of cards. It has a list of 4 suits and 13 ranks. The card.suite is a integer 0-3 and card.rank from 1-13. Using a ```__str__``` method you can print out 'Ace of Clubs' by using ```print(card)```, in a unshuffled deeck this would be
        ```
        print(deck[0])
        ```
        - Deck: This class creates a deck using the Card class, creating 52 instances of the class and placing them in a list. It has a method for shuffling the deck and one for dealing a card from the deck
        - Hand: This class uses the Deck class to deal 5 cards and placing in a list, the players set of cards. It has methods for dealing new cards, sorting hand based on rank and a method for overwriting default print, using the print(card) in order to print the contents of the entire hand in a readable way
        - Ranking: This class handles the value of a poker hand. It has a list of rankings, from highcard to straight flush. The ```rank(hand)``` method will check if the hand is a flush using the ```flush()``` method. Then it will check for a straight using that method. If both return 0, the method will call the ```two_three_four(hand)``` method to find of there is a pair, trips or quads in the hand. The method ```determine_winner(player_hand, AI_hand)``` method will then compare the value of the hands, and call a tiebreaker method if needed.
- highscore.py
    - This module contains classes for handling the highscore from the two games. It is used by the Menu class to update highscore and display highscore. The module contains two classes:
        - HighscoreManager: This class holds a list of highscore items and has methods for printing a table of highscore and sorting the list based on certain keys
        - Highscore: This class is used to transform each row in a worksheet containing highscore data into an instance of a Highscore object for use in HighscoreManager to display highscore


## 4. Testing
The app was tested extensively in the terminal, where many games of Mastermind were played, and the custom rules were tried in many different ways to make sure the game does not break. The poker game was tested by manually setting poker hands and thus being able to make sure all hand rankings are calculated correctly and all tiebreaks are resolved in a manner that is consistent. The entire app was then tested with all options tried in the online terminal to make sure that all text is displayed the way it was intended.

### 4.1 Validator testing
All modules were run through the [PEP8 online checker](http://pep8online.com/) and the only errors that were returned were that lines were above 80 columns in lenght. However, according to [this](https://hg.python.org/peps/rev/fb24c80e9afb) post lines can be up to 99 columns long if it improves readability, and I would argue that the cases still present fall into that cathegory.

### 4.2 Bugs
There are currently no known unfixed bugs in the project.<br>
Solved bugs:
- There used to be a bug when displaying highscore that the 2nd option did not show any information. This was due to a missing method call and was resolved by adding it to the corresponding option
- There was a major bug regarding the ranking of poker hands where aces were not counted as the highest pair, trips or quads. This was sorted by calling the ```determine_first_card(hand)``` and checking if any player hand an ace (the first set of same rank will always be an ace if there is one)
- A similar bug then persisted in the cases where both players had a two pair or a full house. To determine the winner there, the player with the highest pair/trips will win, but it was always checking the "highest" ranked pair/trips meaning an ace would lose. This was solved by again calling the ```determine_first_card(hand)``` and checking for pair/trips of aces and first after that check comparing the highest pair/trips

### 4.4 Testing user Stories
- As an owner, I want to make sure new users are able to find sufficent information to play the game
    - Every part of the game where an input is asked for has a short information, and both games have a welcome text with rules for the game
- As an owner, I want to make sure that the game is logically consistent and that players get the expected results
    - The game has been tested in multiple ways in the terminal for any bug in logic, testing every possible poker hand against each other to make sure winner is declared in a logically consistent way
- As an owner, I want to make sure the highscore is available and can be sorted using different keys
    - The highscore.py module provides the app with all the classes and methods needed for an extansive highscore menu where players can view highscore based on different keys
- As a user, I want to play a game of Mastermind
    - The app provides a functioning game of Mastermind, where the player is also able to set certain custom rules, should they prefer
- As a user, I want to play a game of Poker
    - The app has a poker game that allows the player to be involved in the game and influence the outcome thanks to the option to swap cards
- As a user, I want a logic challenge that is consistent and understandable. I want the results to reflect how I play
    - The game displays results and explains to the user why the results are the way they are. Testing all possible outcomes ensures that the game is logically consistent
- As a user, I want to be able to save my score
    - After every game played the player is given the option to upload their highscore to save and be viewed by others
- As a user, I want to be able to view highscore and compare my own score against that
    - Every user can view the entire list of highscores and sort them in different ways. It is also possible to see only your own results, or the top 5 results for each game

## 5. Deployment


## 6. Credits

