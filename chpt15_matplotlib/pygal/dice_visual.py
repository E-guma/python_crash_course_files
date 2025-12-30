"""This module simulates the experiment of rolling two dice,
    and plotting their outcome frequencies on a bar chart.
    This is an attempt to investigate the probabilistic behaviour
    involved.
    """

import os
from random import randint
from itertools import product
from math import prod
import pygal
from die import Die


# Function to roll all dice and return outcomes in a list
def roll_ndice(dice : list[Die], nrolls : int, operation : str='sum') -> list[int]:
    """Roll a list of dice 'nrolls' times and return a list of outcomes

    Args:
        dice (list[Die]): list of Die instances to roll
        nrolls (int): number of rolls to perform
        operation (str, optional): operation to perform on dice rolls oustcomes ('sum' or 'prod'). Defaults to 'sum'.

    Returns:
        list[int]: list of outcomes from rolling the dice
    """
    rolls = []
    for _ in range(nrolls):
        if operation == 'sum':
            roll_sum = sum(die.roll() for die in dice)
            rolls.append(roll_sum)        
        elif operation == 'prod':
            roll_prod = prod(die.roll() for die in dice)
            rolls.append(roll_prod)
    return rolls

# Funtions to get die roll outcomes
def get_prod_outcomes(dice_sides : list[int]) -> list[int]:
    """Return a list of all product outcomes in rolling a list of dice sides
    Args:
        dice_sides (list[int]): list of sides for each die
    Returns:
        list[int]: list of all possible product outcomes
    """    
    side_ranges = [range(1,sides+1) for sides in dice_sides]
    roll_comb = list(product(*side_ranges))
    outcomes = sorted(list(set(prod(comb) for comb in roll_comb)))
    return outcomes
def get_sum_outcomes(dice_sides : list[int]) -> list[int]:
    """Return a list of all sum outcomes in roll a list of dice sides
    Args:
        dice_sides (list[int]): list of sides for each die
    Returns:
        list[int]: list of all possible sum outcomes
    """
    outcomes = list(range(len(dice_sides), sum(dice_sides)+1))
    return outcomes
    
# Check outcomes frequencies
def list_frequencies(rolls : list[int], outcomes : list[int]) -> list[int]:
    """"Return a list of each outcome frequency
    Args:
        rolls (list[int]): list of die rolls outcomes
        outcomes (list[int]): list of all possible outcomes
    Returns:
        list[int]: list of each outcome frequency
    """
    frequencies = []
    for outcome in outcomes:
        frequency = rolls.count(outcome)
        frequencies.append(frequency)
    return frequencies

# Create dice instances
dice_sides = [6,8]    
dice = [Die(sides) for sides in dice_sides]

# Roll dice and store a list of rolls
rolls = roll_ndice(dice, 5000, 'prod')
# Get a list of all possible outcomes
outcomes = get_prod_outcomes(dice_sides)
# List the frequencies of roll outcomes
frequencies = list_frequencies(rolls, outcomes)

# Calculate probabilities
# prob = [freq/nrolls for freq in frequencies]

# Create Bar Object with local js script
js_file = os.path.join(os.getcwd(), 'pygal-tooltips.min.js')
hist = pygal.Bar(js=[js_file])

# Add bar elements
hist.title = 'Roll 2 dice experiment'
hist.x_labels = outcomes.copy()
hist.x_title = 'Outcome'
hist.y_title = 'Frequency of Outcome'
hist.add(" + ".join(f'D{sides}' for sides in dice_sides), frequencies)

hist.render_to_file('dice_visual.svg')


