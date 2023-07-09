# Pinball Lottery Simulator
This Python code simulates the Pinball Lottery, a fictional lottery game. It generates random numbers for each drawing and checks for winning combinations based on player-selected numbers. The simulation continues until a player hits the jackpot, which is a match of all five white numbers and the red number.

## Code Overview
The code begins by importing necessary libraries and defining variables. It sets up a list of possible white and red numbers, the number of tickets per drawing, the total number of drawings, and variables to track spending and earnings.

The `times_won` dictionary keeps track of the number of times each prize category is won. It has keys representing different categories, such as '5+P' (5 white matches + power match), '5' (5 white matches without power match), '4+P', '4', '3+P', '3', '2+P', '1+P', 'P' (power match without white matches), and '0' (no matches).

The `calc_win_amt` function calculates the win amount based on the player's winning numbers and the drawn winning numbers. It takes two dictionaries as input, `my_winning_nos` (player's numbers) and `winning_nos` (drawn winning numbers). It returns an integer representing the win amount.

The simulation loop starts with an initial `hit_jackpot` flag set to `False` and initializes variables `drawings`, `years`, `total_spent`, and `earnings`. The loop continues until the jackpot is hit.

Within each iteration, a set of white numbers and a red number are randomly chosen as the winning numbers. For each ticket in the drawing, the code randomly selects the player's white and red numbers. It then calls the `calc_win_amt` function to determine the win amount based on the player's numbers and the winning numbers. The total spent and earnings are updated accordingly.

If a jackpot win occurs (matching all numbers), the `hit_jackpot` flag is set to `True`, and the simulation loop breaks. The number of years and drawings taken to hit the jackpot is also tracked and displayed after each year.

Finally, the code outputs the total amount spent, total earnings, and the `times_won` dictionary, which shows the count of wins in each category.

## Running the Code
To run the code, ensure that you have Python installed on your system. Copy the code into a Python file, such as `simulator`.py, and save it.

Open a command prompt or terminal window and navigate to the directory containing the Python file. Run the following command to execute the code:

```
python3 simulator.py
```

The code will run the simulation and display the output, including the total spent, total earnings, and the count of wins in each category.

Please note that the simulation may take a significant amount of time to hit the jackpot, depending on the probability of winning and the number of tickets per drawing.




