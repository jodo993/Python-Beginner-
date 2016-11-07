from tallyMaximum import Tally

tally = Tally()

tally.reset()
tally.setlimit(2)
tally.click()
tally.click()

result = tally.getValue()
print(result)

tally.click()
result = tally.getValue()
print(result)
