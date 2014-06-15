# -*- coding: utf-8 -*-

 ''' Separate one string with 3 or 4 substring in 1+2 or 2+2 like first_name plus last_name '''
import sys
line = "Luis Miguel Cuende Fernandez"
first_name= " "
last_name = " "
arr = line.split()
last = arr.pop()
n = len(arr)+1
if n == 4:
    first = ' '.join(arr[:2])
    second = ' '.join(arr[2:])
elif n == 3:
    first, second = arr[0], ' '.join(arr[1:])
elif n == 2:
    first, second = arr
first_name = first
last_name = second + " " +last
