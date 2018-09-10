import urllib.parse
import urllib.request
import json
import yelpAPI



def obtain_location(parameters: []):
    location = input("Enter your address in this format: Street address, City, State Zip code\nEx: 1234 John, Los Angeles, CA 90001\n").replace(" ", "+")
    parameters.append(('location', location))


def obtain_radius(parameters: []): # check if 0 < radius < 40000
    radius = float(input("How far are you willing to go in miles?\n"))

    # If radius exceeds 40000 meters, automatically set radius to 40000 meters 
    if (radius * 1609.344 > 40000):
        parameters.append(('radius', 40000))
    # Else, convert entered miles to meters
    else:
        parameters.append(('radius', int(radius * 1609.344)))
    
    
def obtain_price(parameters: []):
    price = int(input("On a scale of 1-4, with 1 being cheapest, how much are you willing to spend?\n"))

    while (price < 1 or price > 4):
        if (price >= 1 and price <= 4):
            parameters.append(('price', str(price)))
        else:
            print("Please enter a number from 1-4.\n")


def randomize_again():
    answer = input("Would you like to randomize a different restaurant? (y / n) ")
    return answer

    
