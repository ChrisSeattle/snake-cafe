# snake_cafe

**Author**: Chris L Chapman
**Version**: 1.4.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview

Create a menu and food ordering program to help learn some Python.

## Features

Program uses an Order class to track the user's number of items ordered, running sub-total, and current list of item names and quanitites. The program can use the default menu hard coded in it, or take in an external menu which is selected at the beginning of running the program. The user is greated with a message and can view the selected menu. All user inputs are case-insensitive. Throughout the user's usage of the application they will see a running sub-total of their order.

Menu options:
Besides inital menu setup, the user has a few options for the running menu. They select to see the full menu with an input of 'menu'. They can also select to see a section of the menu by typing the section heading.

User adding and removing items from order:
The user can type the name of valid menu item or they can type 'remove' followed by  valid menu item to remove a previously added item. Both adding and removing item command can be appended with an optional quantitity at the end of the command. If no quantity is given on adding or removing, the program assumes a quantitity of 1. At any time the user attempts to add or remove an item, the program checks to make sure it is a valid item from the current menu, and check if the user alrady has some quantity in their order and operates accordingly. If the user attempts to remove more of an item than they have ordered so far, the application will assume they want to remove all of the ones they have ordered. The program is also aware of the quantity the cafe has on stock, and will not allow the user to add more of a given item than they can provide.

Order Display and Print:
The user can choose to see the curent state of their order with an input of 'order'. The order display will show the quantitiy of each item, how much they are paying for all of those items. This will also give the user their sub-total, cost of tax, and total after including the tax. The user's order will have a unique user id. The user can update after viewing this order, and when selecting to view the order it will reflect these updates keeping this same UUID.

On selecting 'print' as a user input, the current state of the order will be printed to a text file and stored on the machine. If the user later updates their order, they can update this printed receipt by selecting 'print' again. The updated file will continue to have the same name, which is set to the unique user id that has been persistent for this user's order process.

## Getting Started

git clone https://github.com/ChrisSeattle/snake-cafe.git
unsure what else we should put in here.

## Architecture

Python 3.6, uuid, sys, dedent. Pytest used for testing.

## API

Currently no external API is needed (I believe).
