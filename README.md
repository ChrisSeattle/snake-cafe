# snake_cafe

**Author**: Chris L Chapman
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
Create a menu and food ordering program to help learn some Python.

###Features:

- When run, the program should print an intro message and the menu for the restaurant.

- The restaurant’s menu should include appetizers, entrees, desserts, sides, and beverages. At least 6 in each category

- The program should prompt the user for an order

- All input is case-insensitive

- When a user enters an item, the program should print an acknowledgment of their input

- The program should tell the user how to exit

- When user types "order", their current entire order is listed

- If user types "menu", reprint the entire menu

- If user types any category name, print items in that category

- Each item has a price

- We are able to get the user's total order cost for all items added

- Sales tax (stored in constant) is computed and displayed for the user

- Ability to provide a seperate file as a menu with help text

- alert user if inported file is not .csv file.

- When user adds items to their order, they can also give a quantity, but if no quantity given, assume add 1

- Alert user if they are attempting to order more than we have in stock.

- Alert user if they try to remove or add an item not on current menu

- Alert user if they try to remove an item they don't have in their order

- [inpcomlete]  Many key traceback messages from user,
        but not yet including keyboard interupt

- [Not done] (day 02) Every order gets a universally unique identifier

- [Not done] (day 02) User can remove 1 item they had previously added.

## Getting Started
git clone https://github.com/ChrisSeattle/snake-cafe.git
unsure what else we should put in here.

## Architecture
Python 3.6

## API
Currently no external API is needed (I believe).

## Change Log
2018-08-13 20:59:53 - Setup default settings files as given from Code 401 class. Create the repo, clone it, create a new branch to edit.

2018-08-14 [unsure] - Add prices and sales tax, ability to view order with costs, user can also show the full menu or sub-sections of the menu.

2018-08-15 [unsure] - program can inport a csv file and use that for the menu instead of the default hard coded on in the file. User can delete one item (and alert is given if input is not currently in the user's order). The user can also select multiples for
