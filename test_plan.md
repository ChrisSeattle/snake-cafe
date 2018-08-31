# snake_cafe_test_plan

The following functions will not have testing at this time, along with reasons.

- greeting() only has a print output. No additional testing.

- show_menu() only does a print of output. No additonal testing.

- current_sub_total() takes no inputs. Operates on current order state

- display_order() only has print output. No additional testing.

- goodybye() only has print output. No additonal testing.

- select_menu() Takes no inputs. prompts the user with option to use default, new, or typed in filename.

## Tested Functions ##

get_menu() called by select_menu, taking in a filename.
    does it exist
    test if filename not found
    if file found, does it return a properly formatted menu dataset. 

parse_user_input() refactored to return a log.
    Does it exist
    Test valid inputs quit, order, and menu.
    Test if a non-valid input gives expected log

get_order() refactored to return a log.
    Does it exist
    Can it add 1 of an item from MENU
    Can it add 3 of an item from MENU

remove_item()
    Does it exist
    does it manage when a valid MENU item is not present in current order
    can it remove the entire item of one that was recently added as a single quantity
    after a few of a certain item have been added, does this decrement the count
    does it manage when passed an invalid MENU item

**Author**: Chris L Chapman
