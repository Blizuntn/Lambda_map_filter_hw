
# Exercise 1
# Getting rid of the white space
from functools import reduce
places = [' ', 'Argentina', '  ', 'San Diego',
          '', '   ', '', 'Boston', 'New York']
true_places = filter(lambda x: str.strip(x), places)
new_places = list(true_places)
print(new_places)

# Exercise 2
authors = ["Connor Milliken", "Victor aNisimov",
           "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
oa = sorted(authors, key=lambda x: x.split()[-1].lower())
sort_lname = list(oa)
print(sort_lname)


# Exercise 3
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
new_temp = map(lambda x: x[1] * 9/5 + 32, places)
print(list(new_temp))

# Exercise 4


def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-2) + fib(i-1)
