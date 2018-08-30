from .snakes_cafe import parse_user_input, get_order, show_menu


# greeting() only has a print output. No additional testing.
# show_menu() only does a print of output. No additonal testing.
# display_order() only has print output. No additional testing.
# goodybye only() has print output. No additonal testing.
# get_menu() is for future features.


def test_alive():
    """ Is our test file able to run
    """
    pass


# get_menu is for future features
# def test_get_menu_exists():
#     """get_menu allows us to import a cvs file that holds the data of our menu.
#     """
#     assert get_menu

def test_show_menu_exists():
    """ Can we see the show_menu function
        menu order remove
    """
    assert show_menu


def test_show_menu_default():
    """ Testing what is he first, and common way to call this command
    """
    assert show_menu('menu')


def test_parse_user_input_exists():
    """ Do we see Parse_user_input function
    """
    assert parse_user_input


def test_parse_user_input_quit():
    """ On quit it should just return the string back to us
    """
    input = 'quit'
    output = parse_user_input(input)
    assert input == output


def test_parse_user_input_menu():
    """ On quit it should just return the string back to us
    """
    input = 'menu'
    output = parse_user_input(input)
    expected = 'show_menu | menu'
    assert output == expected


def test_parse_user_input_order():
    """ On quit it should just return the string back to us
    """
    input = 'order'
    output = parse_user_input(input)
    expected = 'display_order'
    assert output == expected


def test_parse_user_input_remove():
    """ On quit it should just return the string back to us
    """
    input = 'remove'
    output = parse_user_input(input)
    result = output.split(' ')
    expected = 'remove_item'
    assert result[0] == expected


def test_get_order_exists():
    """ get_order function is needed for adding items to user's order
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



