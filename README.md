# Arcade

Group Members: Symone Houston, Rachana Chau, Jessica McDonald 

**Arcade Description:** 

We designed an arcade with three games: Tetris, Flappy Bird and Snake. The user is able to play any of these three classic games (with some extra design flairs). The arcade keeps track of the user's high scores locally, but these high scores can be reset to zero at any time.


**Getting Started:** 

*Opening the project on PyCharm*

- Add this repository as a project on PyCharm
- Open the "arcade" project on PyCharm
- Go to "PyCharm" --> "Preferences" in the top bar
- Open the "Project: arcade" tab in the "Preferences" box
- Click "Python Interpreter" and select the newest version of Python available (we used Python 3.8)
- While still in the "Python Interpreter" tab, click the "+" button on the bottom left
- Install "pygame" package
- Select the "OK" button

**Running the Code:**
- To create the high score dictionary object or reset the high scores to zero, run "highscoreinit.py"
- After running this script, run "arcade.py" to play
  - You do not need to run "highscoreinit.py" if you would like to play again
  - Running "highscoreinit.py" again will reset the high scores to zero; high scores are saved on your local device otherwise


**How to play:**

*Main Screen*
- Read the prompt on the screen and click the appropriate key to play a game

*Tetris*

*Flappy Bird*

- Read the prompts on the screen
  - Select (1) or (2) to choose a background
  - Select (1), (2), or (3) to choose a bird color
  - Select (1) or (2) to choose a pipe color
  - Press the space bar to begin
- Press the space bar during the game to keep the bird in the air
- Do not touch the pipes
- Do not hit the floor or ceiling
- After you lose, press "return" to replay or "esc" to return to the arcade main screen

*Snake*

- Read the prompts on the screen
  - Select (1), (2), (3), or (4) to choose a snake skin
  - Select (1), (2), (3), or (4) to choose a background
- Read instruction and press the space bar to begin
- Use the arrow keys to move the snake and collect food
- Do not touch the edges and do not run into yourself
- The end screen will automatically close after 5 seconds and bring you back to the main arcade


Packages Used: pygame, os, pickle, random


**HAVE FUN!!**
