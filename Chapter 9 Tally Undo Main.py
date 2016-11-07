from tallyUndoClass import Tally

tally = Tally()

tally.reset()
tally.click()
tally.click()

result = tally.getValue()
print(result)

tally.click()
result = tally.getValue()
print(result)

tally.undo()
tally.undo()
result = tally.getValue()
print(result)

tally.undo()
tally.undo()
result = tally.getValue()
print(result)

