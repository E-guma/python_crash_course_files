import os
import pygal
from die import Die

# Create a D6
die = Die()

# Roll die and store outcome in a list
rolls = []
for _ in range(60):
    roll = die.roll()
    rolls.append(roll)
    
# print(rolls)

# Get outcome frequency
frequencies = []
for i in range(1, die.nsides+1):
    frequency = rolls.count(i)
    frequencies.append(frequency)

# Instantiate Bar object with local js script
js_file = os.path.join(os.getcwd(), 'pygal-tooltips.min.js')
local_js = [js_file]
hist = pygal.Bar(js=local_js)

# Add bar elements
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
# Render bar
hist.render_in_browser()
