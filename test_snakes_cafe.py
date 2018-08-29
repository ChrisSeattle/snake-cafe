from .snake_cafe import get_menu, parse_user_input, get_order
# from .snakes_cafe import get_menu
# from .snakes-cafe import get_order
# from .snakes-cafe import parse_user_input


# greeting() only has a print output. No additional testing.
# show_menu() only does a print of output. No additonal testing.
# display_order() only has print output. No additional testing.
# goodybye only() has print output. No additonal testing.

def test_get_menu_exists():
    """get_menu allows us to import a cvs file that holds the data of our menu.
    """
    assert get_menu


def test_parse_user_input_exists():
    """parse_user_input function does a lot of the work in this code
    """
    assert parse_user_input


def test_get_order_exists():
    """get_order function is needed for adding items to user's order
    """
    assert get_order


# def test_get_order_increases_count_of_item_ordered():
#     """input to function has already been cleaned to be all lowercase.
#     Also, this function is only called if input already matched item
#     name in the MENU.
#     """
#     MENU = [
#         {
#             'item': 'TestName',
#             'status': 0,
#         },
#     ]
#     start_count = [food['status'] for food in MENU]
#     [get_order(i.lower()) for i in [food['item'].lower() for food in MENU]]
#     end_count = [food['status'] for food in MENU]
#     assert start_count == end_count



