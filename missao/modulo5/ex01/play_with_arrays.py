#!/usr/bin/env python3

array_1 = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {array_1}")

array_2 = []
for i in range(len(array_1)):
   array_2.append(array_1[i]+2)
print(f"New array: {array_2}")

