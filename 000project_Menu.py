#! python3
# Using PyInputPlus by Al Sweigart al@inventwithpython.com 

import pyinputplus as pyip
import copy
totalCents = 0
totalDollars = 0
x = 0
#dictionary for the price of each ingredient
prices = {"wheat": {'dollars':1, 'cents':50}, "white": {'dollars':1, 'cents':25}, "sourdough": {'dollars':1, 'cents':75}, "chicken": {'dollars':2,'cents':50}, "turkey": {'dollars':2,'cents':45}, "ham":{'dollars':2,'cents': 30}, "tofu": {'cents':25}, "cheddar": {'cents':15}, "swiss": {'cents':20}, "mozzarella": {'cents':15}, "mayo": {'cents':5}, "mustard": {'cents':8}, "lettuce": {'cents':3}, "tomato": {'cents':1}}
order = {}
orderlist = []
#take order
def takeOrder():
    print('What bread?')
    order['bread'] = pyip.inputMenu( ['wheat','white','sourdough'], prompt = 'What kind of bread?: \n',numbered= True)
    order['meat'] = pyip.inputMenu( ['chicken','turkey','ham','tofu'], prompt = 'What kind of meat?: \n',numbered= True)
    cheese_choice = pyip.inputYesNo('Would you like some cheese? (yes/no)\n')
    if cheese_choice == 'yes':
        order['cheese'] = pyip.inputMenu( ['cheddar','swiss','mozzarella'],prompt = 'What kind of cheese: \n',numbered= True)
    sauce_choice = pyip.inputYesNo('Would you like some sauce? (yes/no)\n')
    if sauce_choice == 'yes':
        order['sauce'] = pyip.inputMenu( ['mayo','mustard', 'lettuce','tomato'],prompt = 'What kind of sauce: \n',numbered= True)      
    getOrder(order)
    calculation()
# Calculate the total price
def calculation():
    global totalCents, totalDollars
    for key in order.values():
        for k,v in prices.items():
            if key == k:
                totalDollars += int(v.get('dollars',0))
                totalCents += int(v.get('cents',0))
# Convert the cents in dollars and display the total price
def totalprice():
    global totalDollars, totalCents
    while totalCents >= 100:
        totalCents -= 100
        totalDollars += 1
    print(f'\nThe total price is {totalDollars} dollars {totalCents} cents')
# Remember each order 
def getOrder(order):
    global orderlist
    tmp = copy.deepcopy(order)
    orderlist.append(tmp)
# Display each order with their price using nested list and dictionary technique
def displayOrder():
    global orderlist, prices 
    for i in range(len(orderlist)):
        print('\nOrder number %s: ' % (i+1))
        for k,v in orderlist[i].items():
            price = prices.get(v)
            dollars = price.get('dollars', 0)
            cents = price.get('cents', 0)
            print(f'{k} = {v} {dollars},{cents}$')

takeOrder()
#ask for how many more orders customer would want. Calls the takeOrder function this amount of time.
ynmore = pyip.inputYesNo('would you like more? (yes/no)\n')
if ynmore == 'yes':
    more = pyip.inputInt('how many more orders of this would you like? \n', min = 1)
    for i in range(more):
        takeOrder()    
displayOrder()
totalprice()
