from textwrap import dedent
import uuid
import sys


# USER_TOTAL = 0
CURRANCY = '$'
SALES_TAX = 0.096
WIDTH = 78
SUB_TOTAL = 0
MENU_FILE = 'menu_file.csv'
# for future features.
# Change old default MENU to BACKUP_MENU, and have MENU variable assignable
DEFAULT_MENU = [
    {
        'item': 'Wings',
        'category': 'Appetizers',
        'price': 10.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Cookies',
        'category': 'Appetizers',
        'price': 5.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Spring Rolls',
        'category': 'Appetizers',
        'price': 9.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Sliders',
        'category': 'Appetizers',
        'price': 10.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Nachos',
        'category': 'Appetizers',
        'price': 8.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Rib Tips',
        'category': 'Appetizers',
        'price': 12.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Salmon',
        'category': 'Entrees',
        'price': 21.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Steak',
        'category': 'Entrees',
        'price': 31.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Meat Tornado',
        'category': 'Entrees',
        'price': 28.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'A Literal Garden',
        'category': 'Entrees',
         'price': 19.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Chicken Alfredo',
        'category': 'Entrees',
        'price': 14.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Pizza',
        'category': 'Entrees',
        'price': 41.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Ice Cream',
        'category': 'Desserts',
        'price': 7.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Cake',
        'category': 'Desserts',
        'price': 8.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Pie',
        'category': 'Desserts',
        'price': 6.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'ChocoTower',
        'category': 'Desserts',
        'price': 12.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Pudding',
        'category': 'Desserts',
        'price': 4.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Flan',
        'category': 'Desserts',
        'price': 7.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Coffee',
        'category': 'Drinks',
        'price': 14.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Tea',
        'category': 'Drinks',
        'price': 3.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Blood of the Innocent',
        'category': 'Drinks',
        'price': 6.66,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Soda',
        'category': 'Drinks',
        'price': 2.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Memosa',
        'category': 'Drinks',
        'price': 8.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Cocktail',
        'category': 'Drinks',
        'price': 0.50,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Fries',
        'category': 'Sides',
        'price': 4.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Onion Rings',
        'category': 'Sides',
        'price': 6.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Vegi',
        'category': 'Sides',
        'price': 3.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Potato',
        'category': 'Sides',
        'price': 4.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Bread',
        'category': 'Sides',
        'price': 2.00,
        'status': 0,
        'stock': 10,
    },
    {
        'item': 'Cheese',
        'category': 'Sides',
        'price': 8.00,
        'status': 0,
        'stock': 10,
    },
]
COURSES = ['Appetizers', 'Entrees', 'Desserts', 'Drinks', 'Sides',]
# USER_COMMANDS = {'menu', 'order', 'remove', 'quit', }
# perhaps we don't want USER_COMMANDS, reconsider when looking at future features


def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    line1 = 'Welcome to Snakes Cafe!'
    line2 = 'Please see our menu below.'
    line3 = 'To quit at any time, type "quit"'
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(line1)) // 2 - 3) + line1 + ' ' * (((WIDTH - len(line1)) // 2 - 3) + len(line1)%2) + ' **'}
        {'** ' + ' ' * ((WIDTH - len(line2)) // 2 - 3) + line2 + ' ' * (((WIDTH - len(line2)) // 2 - 3) + len(line2)%2) + ' **'}
        {'** ' + ' ' * ((WIDTH - len(line3)) // 2 - 3) + line3 + ' ' * (((WIDTH - len(line3)) // 2 - 3) + len(line3)%2) + ' **'}
        {'*' * WIDTH}
    '''))


def show_menu(selection, MENU):
    """Function can display all item on the menu, or all items
        in a specific category of the menu if requested by user input.
        The parameter it takes is for later features. Currently this
        appliation is set to load the default as expected at this stage.
    """
    display = [selection]
    if selection.lower() == 'menu':  # default setting used for early stages of this app
        display = COURSES
    for section in display:
        print('\n** ', section, '\n** ', '-' * 8)
        for option in MENU:
            if option['category'] == section:
                print('** ', option['item'], ' ' * (WIDTH - len(option['item']) - 17), CURRANCY, '{:>5}'.format('{:.2f}'.format(option['price'])), ' **')
    ask = 'What would you like to order?'
    instructions = "You can view your 'order', or type the food you want to add"
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(ask)) // 2 - 3) + ask + ' ' * ((WIDTH - len(ask)) // 2 - 3 + len(ask) % 2) + ' **'}
        {'** ' + ' ' * ((WIDTH - len(instructions)) // 2 - 3) + instructions + ' ' * ((WIDTH - len(instructions)) // 2 - 3 + len(instructions) % 2) + ' **'}
        {'*' * WIDTH}
    '''))


def get_order(select, quantity, MENU):
    """ Takes in a value that exists in our MENU item names (this has been
        checked before this was called). Also takes in a quantity of how many
        the user wants to add (often 1, but could be any integer). We need to
        check if going to exceed the total stock we have of that item. In here
        we will deal with output if their order is exceeding our stock. It
        then adds this item to the user's order.
    """
    # try:
    #     MENU
    # except NameError:
    #     MENU = get_menu('menu_file')

    log = ''
    for option in MENU:
        if select == option['item'].lower():
            # Aaccount for how much we have in stock
            if option['status'] + quantity > option['stock']:
                print("I'm sorry but we don't have enough of those left to add that to your order")
                log = f'get_order | stock | {select}'
                return log
            option['status'] += quantity
            item_cost = option['price'] * option['status']
            # perhaps we deal with total cost later on.
            print('** You have', option['status'], 'order(s) of', option['item'], 'adding', CURRANCY, '{:.2f}'.format(item_cost), 'for your meal **')
            log = f"{option['item']} | {option['status']} | {item_cost}"
    return log


def current_sub_total(MENU):
    """ We want to return cur   rent sub-total afer every command
    """
    user_cost = 0
    for options in MENU:
        if options['status'] > 0:
            user_cost += options['status'] * options['price']
    # [user_cost += food['status'] * food['price'] for food in MENU]
    return user_cost


def display_order(MENU):
    """ This displays the current state of what the user is ordering and
        the current total cost of that order.
    """
    user_cost = 0
    uid = str(uuid.uuid4())
    # The printout formatting maybe should be moved to an external function
    line1 = 'Here is your current order.'
    line2 = "You can 'quit', 'remove <item>', or view 'menu', 'order'"
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(line1)) // 2 - 3) + line1 + ' ' * (((WIDTH - len(line1)) // 2 - 3) + len(line1)%2) + ' **'}
        {'-' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(uid) ) // 2 -3) + uid + ' ' * (((WIDTH - len(uid) ) // 2 - 3) + len(uid)%2) + ' **'}
        {'-' * WIDTH}
        {' Item' + ' ' * ((WIDTH - 44) // 2 + 6 ) + 'Quantity' + ' ' * ( WIDTH // 2 + (WIDTH - 44) % 2 - 3 ) + 'Price'}
    '''))
    for options in MENU:
        if options['status'] > 0:
            user_cost += options['status'] * options['price']
            # remain_width = WIDTH - (len(options['items']) + len(options['status']) + 11)
            # 25 to 30 for item, 5 for status, 8 for money
            line = '{:30}'.format(options['item']) + '{:^6}'.format(options['status']) + ' ' * (WIDTH - 42) + CURRANCY + '{:>5}'.format('{:.2f}'.format(options['price']))
            print(dedent(f''' {line} '''))

            # print(line)
            # line = 'You have ' + str(options['status']) + ' orders of ' +  options['item'] + ' for ' + CURRANCY + str(options['price'] * options['status'])
            # print('** ' + ' ' * ((WIDTH - len(line)) // 2 - 3) + line + ' ' * (((WIDTH - len(line)) // 2 - 3) + len(line)%2) + ' **')
            # print(dedent(f'''
            #     {'** ' + ' ' * ((WIDTH - len(line)) // 2 - 3) + line + ' ' * (((WIDTH - len(line)) // 2 - 3) + len(line)%2) + ' **'}
            # '''))
    print(dedent(f'''
        Your order comes to: {CURRANCY} {'{:>6}'.format('{:.2f}'.format(user_cost))}
        Plus tax: {CURRANCY} {'{:>6}'.format('{:.2f}'.format(user_cost * SALES_TAX))}
        Total Bill: {CURRANCY} {'{:>6}'.format('{:.2f}'.format(user_cost + user_cost * SALES_TAX))}
        {'-' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(line2)) // 2 - 3) + line2 + ' ' * (((WIDTH - len(line2)) // 2 - 3) + len(line2)%2) + ' **'}
        {'*' * WIDTH}
        What would you like to do now?
    '''))
    # we are assuming user is given an input prompt after this function


def goodbye():
    """Function will display a nice little sign-off section after user gave
    the input of 'quit'.
    """
    line_a = 'Thanks for coming to Snakes Cafe.'
    line_b = 'We hope you enjoy your meal with us!'
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(line_a)) // 2 - 3) + line_a + ' ' * (((WIDTH - len(line_a)) // 2 - 3) + len(line_a)%2) + ' **'}
        {'** ' + ' ' * ((WIDTH - len(line_b)) // 2 - 3) + line_b + ' ' * (((WIDTH - len(line_b)) // 2 - 3) + len(line_b)%2) + ' **'}
        {'*' * WIDTH}
    '''))
    sys.exit()


def remove_item(select, MENU):
    """This will decrease the quantity of the given menu item from the
    user's current selection. We have already made sure the input is a
    valid menu item. However, we have not yet checked if the user
    actually has any selected to purchase (be careful not to decrease
    below zero).
    """
    # try:
    #     MENU
    # except NameError:
    #     MENU = get_menu('menu_file')
    lg = 'start'
    for food in MENU:
        if food['item'].lower() == select:
            if food['status'] == 0:
                print("Oh, it seems you don't have any", select, "so I don't need to remove anything")
                lg = f'bad none | remove_item | {select}'
                return lg
            food['status'] -= 1
            print('I have removed one', select, 'from your order')
            lg = f'remove_item | {select} | '
            if food['status'] == 0:
                print('You have no', select, 'in your order')
                lg += '0'
                return lg
            print('** You have', food['status'], 'order(s) of', food['item'], 'for your meal **')
            lg += str(food['status'])
            return lg
    lg = f'bad item | remove_item | {select}'
    return lg


def parse_user_input(select, MENU):
    """ Gets an input from the user. Determines if it is a special command,
    and if so, calls the appropriate function. This is first called after
    the user initially sees the menu. It can handle the 'quit' command to
    exit, and otherwise it keeps looping asking and handling the user's request.
    The user can request to see all, or some sections of the menu, to remove
    1 item in their order, to view their current order and total, or to quit
    """
    # try:
    #     MENU
    # except NameError:
    #     MENU = get_menu('menu_file')
    quantity = 0
    log = ''
    if select == 'quit' or select == '':
        return select
    if select == 'menu' or select.capitalize() in COURSES:
        show_menu(select.capitalize(), MENU)
        log = f'show_menu | {select}'
        return log
    if select == 'order':
        display_order()  # disply their current order and total
        log = f'display_order'
        return log
    if select in [elem['item'].lower() for elem in MENU]:
        get_order(select, 1, MENU)
        log = f'get_order | {select} | 1'
        return log
    # we need to try to split the command to see if it is remove, item
    # pair or if it is add-item, quantity
    if select.split()[0] == 'remove':
        command, *item_select = select.split()
        item_name = ' '.join(item_select)
        if item_name in [elem['item'].lower() for elem in MENU]:
            remove_item(item_name)
            log = f'remove_item | {item_name}'
            return log
        log = f'bad | remove_item | {item_name}'
        return log
    lst = select.split()
    try:
        quantity = int(lst[-1])
    except:
        log = f'bad not_int | {lst[-1]}'
        return log
    if quantity < 1:
        log = f'bad not_positive_int | {lst[-1]}'
        return log
    item_name = ' '.join(lst[:-1])
    if item_name in [elem['item'].lower() for elem in MENU]:
        get_order(item_name, quantity)
        log = f'get_order | {item_name} | {quantity}'
        return log
    log = f'bad | get_order | {item_name} | {quantity}'
    return log


def get_menu(new_menu):
    """This will pull up the menu in the csv file noted in the constant declares.
    If for some reason this file cannot be opened, we will ask the user again.
    MENU_FILE order is 'item', 'category', 'price', 'stock'
    """
    menu_made = []
    new_menu += '.csv'
    # data_order = ['item', 'category', 'price', 'stock']
    try:  # try-except allows us to hide the error stack from user
        with open(new_menu, 'r') as f:
            for line in f:
                food = {}
                i, c, p, s = line.split(', ')
                food['item'] = str(i)
                food['category'] = str(c)
                food['price'] = float(p)
                food['stock'] = int(s)
                food['status'] = 0  # Initialze the count for how many the user has selected
                menu_made.append(food)
        # Not neccassary to 'close()' a file when using 'with'
    except FileNotFoundError:
        print('There was an error locating the file resource. Try again.')
        return select_menu()
    return menu_made


def select_menu():
    """ The user can choose a different menu option
    """
    print(dedent(f'''
    {'Would you like to use our default menu, or use a custom menu?'}
    {'Input 1 for Backup Menu, 2 for New Menu, or type the path to the file.'}
    '''))

    menu_input = input('<: ')
    if menu_input == '1':
        return DEFAULT_MENU
    if menu_input == '2':
        menu_input = MENU_FILE
    file_structure = menu_input.split('/')
    file = file_structure[len(file_structure)-1].split('.')
    extension = file[len(file)-1]
    if extension != 'csv':
        print('Oops, we can only accept a CSV file.')
        return select_menu()
    return get_menu(file[0])


def run():
    """This is the main function, which calls the other functions to do the main work
    """
    global MENU
    MENU = select_menu()
    greeting()
    show_menu('menu')
    select = ''
    while select != 'quit':
        select = str(input('<: ')).lower()
        select = parse_user_input(select, MENU)  # This does most of our programs work
        if select.split(' ')[0] == 'bad':
            print('** Sorry, I am not sure I understood what you wanted **')
        print(select)
        print('Current Sub-Total: ', CURRANCY, '{:.2f}'.format(current_sub_total()))
    goodbye()


if __name__ == '__main__':
    """ If this file was called directly, go to the run() function.
    """
    try:
        run()
    except(KeyboardInterrupt):
        goodbye()
