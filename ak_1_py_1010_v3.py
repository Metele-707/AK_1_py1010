# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:01:03 2026

@author: Metele-707. 
"""

#Showing the yearly cost of petrol car versus electric car. 
# 1 year defined at 365 days.

#Yearly km driven 10000 both cars
m = 10000

#Traffic insurance 8.38 pr.day both cars 
n = (8.38 * 365)

#Petrol car expenses.
#insurance yearly fee
a = (7500 * 1) 

# Rawr juice used pr/km.
b = (1.0 * m)

#toll fee
d = (0.3 * m) 

#Total cost petrol car
e = (n + a + b + d)

#Electric car expenses

# insurance yearly fee
f = (5000 * 1)

# Duracel but for cars
g = (0.2 * 2.00 * m) 

# Toll fee
h = (0.1 * m)

# total cost electric car
j = (n + f + g + h)

x = e-j
print('e =',e, 'and j =', j)
print('x =', x, 'er differanse mellom bensinbil', e, 'og elektrisk bil som er rimeligere', j)


#Differential between electric car and petrol car


# differential. Electric car is cheaper than petrol car. 

