# This program will allow user to click then undo the click
from tallyUndoClass import Tally

# Create an object of the class Tally
tally = Tally()

tally.reset()       # Reset the tally to 0
tally.click()       # Add one to click per call
tally.click()

result = tally.getValue()   # Find the current value of click
print(result)

tally.click()
result = tally.getValue()
print(result)

tally.undo()        # Subtract one to click per call
tally.undo()
result = tally.getValue()
print(result)

tally.undo()
tally.undo()
result = tally.getValue()
print(result)

