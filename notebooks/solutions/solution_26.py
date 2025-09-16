# Exercise 2.6

canton_list = [
    "Zürich",
    "Bern",
    "Luzern",
    "Uri",
    "Schwyz",
    "Obwalden",
    "Nidwalden",
    "Glarus",
    "Zug",
    "Fribourg",
    "Solothurn",
    "Basel-Stadt",
    "Basel-Landschaft",
    "Schaffhausen",
    "Appenzell Ausserrhoden",
    "Appenzell Innerrhoden",
    "St. Gallen",
    "Graubünden",
    "Aargau",
    "Thurgau",
    "Ticino",
    "Vaud",
    "Valais",
    "Neuchâtel",
    "Geneva",
    "Jura",
]

# 1. Sort the list alphabetically
# *******************************
# Looking at `help(list)`, we can see that there is a `sort` method that
# does just this:
canton_list.sort()
print(canton_list)


# 2. Reverse the list
# *******************
canton_list.reverse()
print(canton_list)

# Alternatively, you can use the slicing trick seen earlier:
print(canton_list[::-1])

# Note an important difference between these two methods: the first one
# reverses the original list, while the second one returns a copy of the
# list.
