# snake_cafe_test_plan

The following functions will not have testing at this time, along with reasons.

- greeting() only has a print output. No additional testing.

- show_menu() only does a print of output. No additonal testing.

- Order.display_order() only has print output. No additional testing.

- goodybye() only has print output. No additonal testing.

- select_menu() Takes no inputs. prompts the user with option to use default, new, or typed in filename.

## Tested Functions

get_menu() called by select_menu, taking in a filename.
    does it exist
    if file found, does it return a properly formatted menu dataset.
    if file is not a csv, does it return notice and offer to re-select

parse_user_input() refactored to return a log.
    Does it exist
    Test valid inputs quit, order, menu, remove, [item] to add, print.
    Test if a non-valid input gives expected log

Order class
    Does it exist
    Does it hold the methods, add_item, remove_item, display_order, print_reciept
    Does it have an init property for total_items, user_cost (for sub-total)
    Does it track what the user has ordered keeping name & quantitity in orders property
    Does it assign a UUID to be used for displaying order and printing receipt
    Are the magic properties repr, str, and len set as expected.

Order.print_reciept()
    does it use the UUID for this order as the name for a .txt file for this users' order
    can it create that file if it does not exist.
    can it update that file if it does exist (was printed, then order updated, and printed again)
    does the content of that .txt file match what is seen from Order.display_order()
    if it has an error on creating or updating that file, does it fail gracefully & alert user

Order.add_item() refactored to return a log.
    Does it exist
    Can it add 1 of an item from MENU
    Can it add 3 of an item from MENU
    Do we get exected response when user attempts to order more than in stock
    Does the program manage when user attempts to add a non-existant item

Order.remove_item()
    Does it exist
    does it manage when a valid item (exists in menu) is not present in current order
    does it manage when passed an invalid item (does not exist in menu)
    can it remove the entire item of one that was recently added as a single quantity
    after a few of a certain item have been added, does this decrement the count
    can it remove multiple items when requested
    does it adjust when user attempt to remove more than they have ordered
    does it error check when requested to remove an invalid quantity (0 or less)

**Author**: Chris L Chapman
