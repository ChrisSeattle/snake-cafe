from .snakes_cafe import parse_user_input, get_menu, Order
import pytest



def test_alive():
    """ Is our test file able to run
    """
    pass

@pytest.fixture
def user():
    """ We need to initialize a user for many tests
    """
    currency = '$'
    MENU = get_menu('menu_file')
    user = Order(currency, MENU)
    return user


def test_order_class_exists():
    """ Can we see the Order class
    """
    assert Order


def test_order_add_item_exists():
    """ Do we see the Order.add_item function
    """
    assert Order.add_item


def test_order_add_item_one_item(user):
    """ Does Order.add_item return expected log on given item ordered
    """
    item = 'pizza'
    # add_item method assigns quantity = 1 if none declared
    expected = 'user.add_item | pizza | 1'
    actual = user.add_item(item)
    assert actual == expected


def test_order_add_item_item_few(user):
    """ Does Order.add_item work when user adds multiple of an item
    """
    item = 'flan'
    quantitity = 3
    expected = 'user.add_item | flan | 3'
    actual = user.add_item(item, quantitity)
    assert actual == expected


def test_order_remove_item_exits():
    """ Can we see the function
    """
    assert Order.remove_item


def test_order_remove_item_when_item_not_in_current_order(user):
    """ If we don't add an item in advance, test our response on remove attempt
    """
    input = 'Blood of the Innocent'.lower()
    expected = f'user.remove_item | had none | {input}'
    actual = user.remove_item(input)
    assert actual == expected


def test_remove_the_recently_added_single_item(user):
    """ Add a single item from MENU, then do we remove it
    """
    input = 'fries'.lower()
    expected = f'user.remove_item | {input} | ' + '0'
    quantitity = 1
    user.add_item(input, quantitity)
    actual = user.remove_item(input)
    assert actual == expected


def test_remove_the_recently_added_multiple_item(user):
    """ Add a single item from MENU, then do we remove it
    """
    input = 'wings'.lower()
    quantitity = 5
    expected = f'user.remove_item | {input} | ' + str(quantitity - 1)
    user.add_item(input, quantitity)
    actual = user.remove_item(input)
    assert actual == expected


def test_order_remove_item_that_is_not_in_menu(user):
    """ Does test_remove manage when asked to remove an item
        that isn't even a valid item for our MENU
    """
    input = 'asdfghkl'.lower()
    expected = f'bad item | user.remove_item | {input}'
    actual = user.remove_item(input)
    assert actual == expected


def test_order_user_cost_increase_on_add_item(user):
    """ On sucessful add_item, user.user_cost increases
    """
    start = user.user_cost
    input_a = 'wings'.lower()
    quantitity_a = 2
    user.add_item(input_a, quantitity_a)
    step1 = user.user_cost
    assert step1 > start
    input_b = 'pizza'.lower()
    quantitity_b = 3
    user.add_item(input_b, quantitity_b)
    step2 = user.user_cost
    assert step2 > step1


def test_order_user_cost_decrease_on_remove_item(user):
    """ On sucessful remove_item, user.user_cost decreases
    """
    input_a = 'wings'.lower()
    quantitity_a = 5
    user.add_item(input_a, quantitity_a)
    step1 = user.user_cost
    quantitity_b = 3
    user.remove_item(input_a, quantitity_b)
    step2 = user.user_cost
    assert step2 < step1


def test_order_uuid_is_set_for_each_user_order():
    """ For each user session they get a UUID for their order
    """
    currency = '$'
    MENU = get_menu('menu_file')
    user = Order(currency, MENU)
    other_user = Order(currency, MENU)
    assert user.uid
    assert other_user.uid


def test_order_uuid_is_unique_for_each_user_order():
    """ For each user session they get a UUID for their order
    """
    currency = '$'
    MENU = get_menu('menu_file')
    user = Order(currency, MENU)
    other_user = Order(currency, MENU)
    assert user.uid != other_user.uid


def test_order_total_items_exists(user):
    """ Order has a _total_items property intialzed at 0
    """
    expected = 0
    actual = user._total_items
    assert expected == actual


def test_order_length(user):
    """ Order has a defaul len property that returns _total_items
    """
    expected = 0
    actual = len(user)
    assert expected == actual


def test_order_length_increments_on_add_item(user):
    """ On sucessful add_item, len result of Order increments
    """
    input_a = 'wings'.lower()
    quantitity_a = 2
    user.add_item(input_a, quantitity_a)
    step1 = len(user)
    input_b = 'pizza'.lower()
    quantitity_b = 3
    user.add_item(input_b, quantitity_b)
    step2 = len(user)
    assert step1 == 2
    assert step2 == 5


def test_order_length_decrements_on_remove_item(user):
    """ On sucessful remove_item, len result of Order decrements
    """
    input_a = 'wings'.lower()
    quantitity_a = 5
    user.add_item(input_a, quantitity_a)
    step1 = len(user)
    quantitity_b = 3
    user.remove_item(input_a, quantitity_b)
    step2 = len(user)
    assert step1 == 5
    assert step2 == 2


def test_order_str(user, capsys):
    """ Order has a default str property calling self.display_order
    """
    user.display_order()
    expected, err1 = capsys.readouterr()
    str(user)
    actual, err2 = capsys.readouterr()
    assert expected == actual


def test_order_repr(user):
    """ Order has a default repr property and returns expected results
    """
    expected = f'''<Order {user.uid} | Items: 0 | Total: $ 0>'''
    actual = repr(user)
    assert expected == actual


def test_order_print_receipt_success(user):
    """ Order.print_receipt returns expected log when successful
    """
    expected = f'<user.print_receipt | {user.uid}.txt>'
    output = user.print_receipt()
    assert output == expected


def test_order_print_receipt_error(user):
    """ Order.print_receipt returns expected log when failed
    """
    path_error = '../../this/path/does/not/exist/'
    file_error = path_error + user.uid
    expected = f'<bad user.print_receipt | {file_error}.txt>'
    output = user.print_receipt(path_error)
    assert output == expected


# ========== End of methods in the Order class ============= #


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


def test_parse_user_input_quit(user):
    """ On 'quit' it should just return the string back to us
    """
    input = 'quit'
    output = parse_user_input(input, user, user.menu)
    assert input == output


def test_parse_user_input_menu():
    """ On 'menu' it should call show_menu and returns a log
    """
    input = 'menu'
    expected = 'show_menu | menu'
    MENU = get_menu('menu_file')
    user = Order('$', MENU)
    output = parse_user_input(input, user, MENU)
    assert output == expected


def test_parse_user_input_order():
    """ On 'order', it calls display_order and returns a log
    """
    input = 'order'
    expected = 'user.display_order'
    MENU = get_menu('menu_file')
    user = Order('$', MENU)
    output = parse_user_input(input, user, MENU)
    assert output == expected


def test_parser_user_input_print(user):
    """ On 'print' it calls the Order.print_reciept and returns a log
    """
    input = 'print'
    expected = f'<user.print_receipt | {user.uid}.txt>'
    output = parse_user_input(input, user, user.menu)
    assert output == expected
