from .snakes_cafe import parse_user_input, get_menu, Order


def test_alive():
    """ Is our test file able to run
    """
    pass

# ========== In the Order class ============= #


def test_Order_class_exists():
    """ Can we see the Order class
    """
    assert Order


def test_order_add_item_exists():
    """ Do we see the Order.add_item function
    """
    assert Order.add_item


def test_order_add_item_one_item():
    """ Does Order.add_item return expected log on given item ordered
    """
    # global MENU
    # MENU = get_menu('menu_file')
    MENU = get_menu('menu_file')
    item = 'pizza'
    quantitity = 1
    expected = 'Pizza | 1 | 41.0'
    actual = Order.add_item(item, quantitity, MENU)
    assert actual == expected


def test_order_add_item_item_few():
    """ Does Order.add_item work when user adds multiple of an item
    """
    MENU = get_menu('menu_file')
    item = 'flan'
    quantitity = 3
    expected = 'Flan | 3 | 21.0'
    actual = Order.add_item(item, quantitity, MENU)
    assert actual == expected


def test_order_remove_item_exits():
    """ Can we see the function
    """
    assert Order.remove_item


def test_order_remove_item_when_item_not_in_current_order():
    """ If we don't add an item in advance, test our response on remove attempt
    """
    MENU = get_menu('menu_file')
    input = 'Blood of the Innocent'.lower()
    expected = f'bad none | Order.remove_item | {input}'
    actual = Order.remove_item(input, MENU)
    assert actual == expected


def test_remove_the_recently_added_single_item():
    """ Add a single item from MENU, then do we remove it
    """
    MENU = get_menu('menu_file')
    input = 'fries'.lower()
    quantitity = 1
    Order.add_item(input, quantitity, MENU)
    expected = f'Order.remove_item | {input} | ' + '0'
    actual = Order.remove_item(input, MENU)
    assert actual == expected


def test_remove_the_recently_added_multiple_item():
    """ Add a single item from MENU, then do we remove it
    """
    MENU = get_menu('menu_file')
    input = 'wings'.lower()
    quantitity = 5
    Order.add_item(input, quantitity, MENU)
    expected = f'Order.remove_item | {input} | ' + str(quantitity - 1)
    actual = Order.remove_item(input, MENU)
    assert actual == expected


def test_order_remove_item_that_is_not_in_menu():
    """ Does test_remove manage when asked to remove an item
        that isn't even a valid item for our MENU
    """
    MENU = get_menu('menu_file')
    input = 'asdfghkl'.lower()
    expected = f'bad item | Order.remove_item | {input}'
    actual = Order.remove_item(input, MENU)
    assert actual == expected


# def test_order_add_item_increases_count_of_item_ordered():
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
#     [Order.add_item(i.lower()) for i in [food['item'].lower() for food in MENU]]
#     end_count = [food['status'] for food in MENU]
#     assert start_count == end_count


# ========== End in the Order class ============= #


def test_get_menu_exists():
    """ Can we see the function
    """
    assert get_menu


def test_get_menu_file_found():
    """ What if the user asked to use an unfound file
    """
    input = 'menu_file'
    output = get_menu(input)
    assert isinstance(output, list)


def test_parse_user_input_exists():
    """ Do we see Parse_user_input function
    """
    assert parse_user_input


def test_parse_user_input_quit():
    """ On 'quit' it should just return the string back to us
    """
    MENU = get_menu('menu_file')
    input = 'quit'
    output = parse_user_input(input, MENU)
    assert input == output


def test_parse_user_input_menu():
    """ On 'menu' it should call show_menu and returns a log
    """
    MENU = get_menu('menu_file')
    input = 'menu'
    output = parse_user_input(input, MENU)
    expected = 'show_menu | menu'
    assert output == expected


def test_parse_user_input_order():
    """ On 'order', it calls display_order and returns a log
    """
    MENU = get_menu('menu_file')
    input = 'order'
    output = parse_user_input(input, MENU)
    expected = 'display_order'
    assert output == expected


