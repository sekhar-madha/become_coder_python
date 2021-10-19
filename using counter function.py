
from collections import Counter

# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))

