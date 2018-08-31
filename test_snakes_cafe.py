from .snakes_cafe import parse_user_input, get_order, remove_item, get_menu


def test_alive():
    """ Is our test file able to run
    """
    pass


def test_get_menu_exists():
    """ Can we see the function
    """
    assert get_menu


def test_get_menu_file_not_found():
    """ What if the user asked to use an unfound file
    """
    input = 'we_do_not_have_this_file_really'
    output = get_menu(input)
    expected = ''
    assert output == expected


def test_get_menu_file_found():
    """ What if the user asked to use an unfound file
    """
    global MENU
    input = 'menu_file'
    MENU = get_menu(input)
    output = get_menu(input)
    assert isinstance(output, list)


def test_get_order_exists():
    """ Do we see the get_order functioin
    """
    assert get_order


def test_get_order_one_item():
    """ Does get_order return expected log on given item ordered
    """
    global MENU
    MENU = get_menu(menu_file)
    item = 'pizza'
    quantitity = 1
    expected = 'Pizza | 1 | 41.0'
    actual = get_order(item, quantitity)
    assert actual == expected


def test_get_order_item_few():
    """ Does get_order work when user adds multiple of an item
    """
    MENU = get_menu(menu_file)
    item = 'flan'
    quantitity = 3
    expected = 'Flan | 3 | 21.0'
    actual = get_order(item, quantitity)
    assert actual == expected


def test_parse_user_input_exists():
    """ Do we see Parse_user_input function
    """
    assert parse_user_input


def test_parse_user_input_quit():
    """ On 'quit' it should just return the string back to us
    """
    input = 'quit'
    output = parse_user_input(input)
    assert input == output


def test_parse_user_input_menu():
    """ On 'menu' it should call show_menu and returns a log
    """
    input = 'menu'
    output = parse_user_input(input)
    expected = 'show_menu | menu'
    assert output == expected


def test_parse_user_input_order():
    """ On 'order', it calls display_order and returns a log
    """
    input = 'order'
    output = parse_user_input(input)
    expected = 'display_order'
    assert output == expected


def test_remove_item_exits():
    """ Can we see the function
    """
    assert remove_item


def test_remove_item_when_item_not_in_current_order():
    """ If we don't add an item in advance, test our response on remove attempt
    """
    input = 'Blood of the Innocent'.lower()
    expected = f'bad none | remove_item | {input}'
    actual = remove_item(input)
    assert actual == expected


def test_remove_the_recently_added_single_item():
    """ Add a single item from MENU, then do we remove it
    """
    input = 'fries'.lower()
    quantitity = 1
    get_order(input, quantitity)
    expected = f'remove_item | {input} | ' + '0'
    actual = remove_item(input)
    assert actual == expected


def test_remove_the_recently_added_multiple_item():
    """ Add a single item from MENU, then do we remove it
    """
    input = 'wings'.lower()
    quantitity = 5
    get_order(input, quantitity)
    expected = f'remove_item | {input} | ' + str(quantitity - 1)
    actual = remove_item(input)
    assert actual == expected


def test_remove_item_that_is_not_in_menu():
    """ Does test_remove manage when asked to remove an item
        that isn't even a valid item for our MENU
    """
    input = 'asdfghkl'.lower()
    expected = f'bad item | remove_item | {input}'
    actual = remove_item(input)
    assert actual == expected


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



