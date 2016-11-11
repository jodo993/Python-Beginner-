# This program specifiy how many clicks can be clicked before a limit is reached
from tallyMaximum import Tally      # Get the Tally class from file

tally = Tally()     # Create object of class Tally

tally.reset()       # Reset to 0
tally.setlimit(2)   # Set max to 2
tally.click()       # Simulate a click
tally.click()

result = tally.getValue()   # Get current value
print(result)               # Display

tally.click()
result = tally.getValue()
print(result)
