import pandas as pd

# read data from file
data = pd.read_csv("flights-small.csv")
# sort by 'Distance'
data = data.sort_values(by='DISTANCE', ascending = False)
# the largest three filghts
theLongestThreeFlights = data[:3]

print(theLongestThreeFlights)