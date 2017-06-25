import random

NUM_ITERATIONS = 10000000
NUM_PLAYERS = 1000

strategy = [random.random() for i in range(NUM_PLAYERS)]
coffee = [0.0]*NUM_PLAYERS
fills = [0] * NUM_PLAYERS

pot = 1.0
for i in range(NUM_ITERATIONS):
    player = random.randint(0,NUM_PLAYERS-1)
    pot -=  strategy[player]
    if pot < 0:
        pot = 1.0
        fills[player] += 1
    else:
        coffee[player] += strategy[player]

scores = zip(strategy, coffee)
scores = sorted(scores, key=lambda x: x[0])

x = []
y = []
for a, b in scores:
    x.append(a)
    y.append(b)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.title("Five Thirty Eight Coffee Simulation over "+str(NUM_ITERATIONS)+" Iterations")
plt.xlabel("Strategy")
plt.ylabel("Amount of coffee consumed")
plt.savefig("fig.png")
#plt.show()
