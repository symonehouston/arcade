# 30 min working all together

"""
THIS FILE CREATE A HIGH SCORE DICTIONARY WITH 0 VALUES.
RUN SCRIPT BEFORE PLAYING FOR THE FIRST TIME OR TO RESET HIGH SCORES TO 0.
"""

import pickle

# Create score dictionary
score_dict = {}

# Add high score 0 for each game
score_dict['tetris'] = 0
score_dict['flappybird'] = 0
score_dict['snake'] = 0

# Create file that stores dictionary
pickle.dump(score_dict, open("score_dict.p", "wb"))
