# Level -3

# Euclidian_ distance(d) =√[(x2 – x1)2 + (y2 – y1)2]

import math

x_1, y_1 = 2, 3
x_2, y_2 = 10, 8

# diffs = ((x_2 - x_1)**2) + ((y_2 - y_1)**2)
# print(diffs)

d = math.sqrt(((x_2 - x_1)**2) + ((y_2 - y_1)**2))
print(round(d, 3))