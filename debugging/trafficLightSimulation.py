# Using an Assertion in a Traffic Light Simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'red'
        elif intersection[key] == 'yellow':
            intersection[key] = 'green'
        elif intersection[key] == 'red':
            intersection[key] = 'yellow'

    assert 'red' in intersection.values(), 'Neither light is red!' # This assertion checks if there is at least one red light in the intersection. If there isn't, it raises an AssertionError with the message 'Neither light is red!'.
    return intersection

print(switchLights(market_2nd)) # Output: {'ns': 'red', 'ew': 'yellow'}
print(switchLights(mission_16th)) # Output: {'ns': 'yellow', 'ew': 'red'}