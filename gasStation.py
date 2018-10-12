'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
otherwise return -1.
'''

def canCompleteCircuit(gas, cost):

    total = 0
    index = 0

    for i in range(0, len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            total = 0
            index = i + 1

    if index < len(gas) and sum(gas) >= sum(cost):
        return index
    else:
        return -1