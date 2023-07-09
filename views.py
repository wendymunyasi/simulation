import json
import random  # convert to list comprehesnsion
from typing import Dict, Set

white_possibiles = list(range(1, 70))
red_possibiles = list(range(1, 27))
tckts_per_drawing = 100
num_drawings = 15600
total_spent = 0
earnings = 0

times_won = {
    '5+P': 0,
    '5': 0,
    '4+P': 0,
    '4': 0,
    '3+P': 0,
    '3': 0,
    '2+P': 0,
    '1+P': 0,
    'P': 0,
    '0': 0
}


def calc_win_amt(my_winning_nos: Dict[str, Set[int]], winning_nos: Dict[str, Set[int]]) -> int:
    """Calculate the win amount based on the winning numbers.

    Args:
        my_winning_nos (Dict[str, Set[int]]): The winning numbers picked by
        the player. Should contain the keys 'whites' and 'red' with
        corresponding sets of numbers.
        winning_nos (Dict[str, Set[int]]): The winning numbers.

    Returns:
        int: The win amount based on the matching numbers and power match.
    """
    win_amt = 0
    # access the whites from my numbers & whites from winning numbers
    # use a set method called intersection to find matching numbers
    # returns a set of values in both
    # wrap it in a length function to find how many matching numbers
    white_matches = len(
        my_winning_nos['whites'].intersection(winning_nos['whites']))

    # Check if the player's red number matches the winning red number
    power_match = my_winning_nos['red'] == winning_nos['red']
    # Determine the win amount based on the num of white matches & power match
    if white_matches == 5:
        if power_match:
            win_amt = 2_000_000_000
            times_won['5+P'] += 1
        else:
            win_amt = 1_000_000_000
            times_won['5'] += 1
    elif white_matches == 4:
        if power_match:
            win_amt = 50_000
            times_won['4+P'] += 1
        else:
            win_amt = 100
            times_won['4'] += 1
    elif white_matches == 3:
        if power_match:
            win_amt = 100
            times_won['3+P'] += 1
        else:
            win_amt = 7
            times_won['3'] += 1
    elif white_matches == 2 and power_match:
        win_amt = 7
        times_won['2+P'] += 1
    elif white_matches == 1 and power_match:
        win_amt = 4
        times_won['1+P'] += 1
    elif power_match:
        win_amt = 4
        times_won['P'] += 1
    else:
        times_won['0'] += 1

    return win_amt


# for drawing in range(num_drawings):
hit_jackpot = False
drawings = 0  # number of drawings it will take to hit jackpot
years = 0  # number of years it will take to hit jack pot

while True:
    drawings += 1
    white_drawing = set(random.sample(white_possibiles, k=5))
    # choice because it will be a single number
    red_drawing = random.choice(red_possibiles)
    winning_nos = {
        'whites': white_drawing,
        'red': red_drawing
    }
    for tckt in range(tckts_per_drawing):
        total_spent += 2
        my_whites = set(random.sample(white_possibiles, k=5))
        my_red = random.choice(red_possibiles)
        my_winning_nos = {
            'whites': my_whites,
            'red': my_red
        }
        win_amt = calc_win_amt(my_winning_nos, winning_nos)
        earnings += win_amt
        if win_amt == 2_000_000_000:
            hit_jackpot = True
            break
    if drawings % 156 == 0:  # 156 has been a year
        years += 1
        print(f'Years: {years}')
    if hit_jackpot:
        break

print(f'Spent: ${total_spent}')
print(f'Earnings: ${earnings}')

print(json.dumps(times_won, indent=2))
