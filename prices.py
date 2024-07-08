# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:05:34 2024

@author: NilesThompson
"""
#Initilize the sum variable to 0
sum = 0

#Initilize the count variable to 0 
count = 0 

fullName = input("What is your full neme?: ") #input for users full name
print("Hello", fullName)

#input the minimum price
minPrice = float(input("What is the mininum price?: "))

#This is a created list of prices
priceList = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]

#review the price list
for price in priceList:
    #add curent price to sum
    sum += price
    if price > minPrice:
        count += 1


# the output of the results
print("Hello",fullName,"the minimum price is",minPrice)
print("There are",count,"prices greater than the minimum price")
print("The total price is",sum)