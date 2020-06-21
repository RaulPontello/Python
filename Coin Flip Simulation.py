## Coin Flip Simulation ##
# Objective: Verify the Central Limit Theorem

# 1) Importing

import random
import pandas as pd
import matplotlib.pyplot as plt

# 2) Functions

def flip_coin(n, t):
    """
    Function used to determine the heads count
    Ex: n=2 and t=4 --> possible outcome: [H, H, T, T], [[H, T], [T, T], [H, T], [H, H]]
        n=3 and t=2 --> possible outcome: [H, H], [[H, T], [T, T]], [[H, T, T], [T, T, H]]
    :param n: number of coins
    :param t: number of times the coin will be flipped
    :return: list with the number of heads
    """
    one_flip = [] # one_flip has i elements, i = [1, 2,..., n]
    one_turn = [] # one_turn has t elements
    all_turns = [] # all_turns has n elements
    one_turn_heads = []
    all_turns_heads = []

    for i in range(1 , n + 1):
        for j in range(1 , t + 1):
            for k in range(1, i + 1):
                one_flip.append(random.randint(0 , 1)) # Heads = 1, Tales = 0
            one_turn.append(one_flip[:])
            one_turn_heads.append(one_flip.count(1)) # Counting heads in one_flip
            one_flip.clear() # Erase all data in one-flip
        all_turns.append(one_turn[:])
        all_turns_heads.append(one_turn_heads[:])
        one_turn.clear() # Erase all data in one_turn
        one_turn_heads.clear() # Erase all data in one-turn_heads

    return all_turns_heads

# 3) Main code

print('100 coins will be flipped !')
turn = int(input('How many times the coin will be flipped: '))
heads = flip_coin(100, turn)

# 3.1) Creation of dataframes

df1 = pd.DataFrame({'1 coin': heads[0]})
df2 = pd.DataFrame({'2 coins': heads[1]})
df3 = pd.DataFrame({'3 coins': heads[2]})

df4 = pd.DataFrame({'4 coins': heads[3]})
df5 = pd.DataFrame({'5 coins': heads[4]})
df6 = pd.DataFrame({'6 coins': heads[5]})

df18 = pd.DataFrame({'18 coins': heads[17]})
df19 = pd.DataFrame({'19 coins': heads[18]})
df20 = pd.DataFrame({'20 coins': heads[19]})

df48 = pd.DataFrame({'48 coins': heads[47]})
df49 = pd.DataFrame({'49 coins': heads[48]})
df50 = pd.DataFrame({'50 coins': heads[49]})

df98 = pd.DataFrame({'98 coins': heads[97]})
df99 = pd.DataFrame({'99 coins': heads[98]})
df100 = pd.DataFrame({'100 coins': heads[99]})

# 3.2) Plotting

fig, axes = plt.subplots(nrows=5 , ncols=3) # Plotting 12 graphs
df1.plot.hist(ax=axes[0][0], bins=50)
df2.plot.hist(ax=axes[0][1], bins=50)
df3.plot.hist(ax=axes[0][2], bins=50)

df4.plot.hist(ax=axes[1][0], bins=50)
df5.plot.hist(ax=axes[1][1], bins=50)
df6.plot.hist(ax=axes[1][2], bins=50)

df18.plot.hist(ax=axes[2][0], bins=50)
df19.plot.hist(ax=axes[2][1], bins=50)
df20.plot.hist(ax=axes[2][2], bins=50)

df48.plot.hist(ax=axes[3][0], bins=50)
df49.plot.hist(ax=axes[3][1], bins=50)
df50.plot.hist(ax=axes[3][2], bins=50)

df98.plot.hist(ax=axes[4][0], bins=50)
df99.plot.hist(ax=axes[4][1], bins=50)
df100.plot.hist(ax=axes[4][2], bins=50)

plt.show()








