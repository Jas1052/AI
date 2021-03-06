import numpy as np
import itertools
import copy

#classes defined: Percept and Input(extends Percept)
#parameters: the weights (w_ij) and thresholds (t_j)

target = [0, 1, 1, 0]

class Percept:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
        self.percepts = None
    def set_inputs(self, percepts):
        self.percepts = percepts
    def actuator(self, val):
        return 1 if val > self.threshold else 0
    def evaluate(self):
        total = 0
        for index in range(len(self.percepts)):
            total += self.weights[index] * self.percepts[index].evaluate()
        return self.actuator(total)

class Input(Percept):
    def __init__(self):
        self.value = None
    def set_value(self, val):
        self.value = val
    def evaluate(self):
        return self.value
"""
w13 = -1
w23 = -1
w14 = 1
w24 = 1
w35 = 1
w45 = 1
w36 = -1
w46 = -1

t3 = -1.5
t4 = 0.5
t5 = 1.5
t6 = -0.5

x1 = Input()
x2 = Input()

node_3 = Percept([w13,w23],t3, "nand") # nand
node_4 = Percept([w14,w24],t4, "or") # or
node_5 = Percept([w35,w45],t5, "and") # and 
node_6 = Percept([w36,w46],t6, "nor") # nor
"""

x1 = Input()
x2 = Input()

values = [[-0.5, -0.5, -1.5],
[ 0.5,  0.5, -0.5],
[ 1.5, -2.5, -0.5],
[ 1.5,  0.5, -0.5],
[-1.5,  1.5, -0.5],
[-0.5,  1.5, -0.5],
[ 1.5,  1.5, -0.5],
[-0.5, -0.5,  0.5],
[ 0.5, -1.5,  0.5],
[ 1.5, -0.5,  0.5],
[-2.5,  0.5,  1.5],
[-0.5,  1.5,  0.5],
[-2.5, -1.5,  3.5],
[ 0.5,  0.5,  0.5]]

nodes = []
for value in values:
    output = Percept([value[0], value[1]], -1 * value[2])
    nodes.append(output)
    
counter = 0

for a in nodes:
    first = copy.copy(a)
    for b in nodes:
        second = copy.copy(b)
        for c in nodes:
            third = copy.copy(c)
            first.set_inputs([x1,x2])
            second.set_inputs([x1,x2])
            third.set_inputs([first, second])
            xor = third
            # print(first.name, second.name, third.name)
            result = []
            for a in range(2):
                for b in range(2):
                    x1.set_value(a)
                    x2.set_value(b)
                    endEval = xor.evaluate()
                    result.append(endEval)
                    # print(a, b, endEval)
            # print(result)
            if result == target:
                counter += 1
            # print('\n')

print(counter)
print("done")
