#!python3
# A program to calculate how many tiles of food need to be grown based on total colony size.
import math

# Simple and Fine Meals both require 0.5 nutrition to produce. They only differ in work efficiency, which we are not concerned with
mealInput = 0.5
corn = {"value": 0.05, "period": 20.86, "yield": 21.903}
rice = {"value": 0.05, "period": 5.54, "yield": 5.9832}
# Included for potential future use, but not currently used.
# potatoes = {"value": 0.05, "period": 10.71, "yield": 11.0313}

# Crops should be roughly evenly split between corn and rice. Rice will provide stability while corn will minimize labor cost.
def growSize(numPawns):
    # A standard pawn will eat 1.6 nutrition per day. Most meals provide roughly 1 nutrition, but due to rounding, pawns will consume 2 meals per day.
    nutritionReq = numPawns * 2
    cornTiles = (nutritionReq / 2) / ((corn["yield"] / corn["period"]) * corn["value"])
    riceTiles = (nutritionReq / 2) / ((rice["yield"] / rice["period"]) * rice["value"])
    return f"You need {math.ceil(cornTiles)} tiles of corn and {math.ceil(riceTiles)} tiles of rice."


print(growSize(int(input("How many pawns are in your colony?\n"))))
