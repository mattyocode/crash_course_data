from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.

results = []
for d_roll in range(1000):
    result = die.roll()
    results.append(result)

# Analyse the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)