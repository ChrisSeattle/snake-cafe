from textwrap import dedent
import uuid
import sys

# USER_TOTAL = 0
CURRENCY = '$'
SALES_TAX = 0.096
WIDTH = 78
MENU_FILE = 'menu_file.csv'
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
# any future sections of the menu should be added to COURSES list


class Order(object):
    """ A user's orders will stored using this class.
    """
    def __init__(self, currency, menu):
        """ For this order instance, we need to know what the cafe
            has set for the currency symbol, and which menu is used
            We also initialize some properites to track the order
            as well as create a UUID for this user's order.
        """
        self.currency = currency  # currency symbol for this order
        self.menu = menu  # which menu is user currently ordering from
        self._total_items = 0
        self.user_cost = 0
        self.uid = str(uuid.uuid4())
        self.orders = dict()
        # orders name: key is item/name: count of ordered
        # for each item user has ordered from MENU list
        # MENU list has dict of item/name, category, price, avail stock

    def __len__(self):
        return self._total_items

    def __str__(self):
        return self.display_order()

    def __repr__(self):
        return f'''<Order {self.uid} | Items: {self._total_items} | Total: {self.currency} {self.user_cost}>'''

    def add_item(self, select, quantity=1):
        """ Takes in a value that exists in our MENU item names (this has been
            checked before this was called). Also takes in a quantity of how many
            the user wants to add (often 1, but could be any integer). We need to
            check if going to exceed the total stock we have of that item. In here
            we will deal with output if their order is exceeding our stock. It
            then adds this item to the user's order.
        """
        MENU = self.menu
        log = 'no items'  # over-written later
        for option in MENU:
            if select == option['item'].lower():
                # user is ordering this item, so make sure it's in orders
                if select not in self.orders.keys():
                    self.orders[select] = 0  # count 0 for now
                # Account for how much the cafe has in stock
                if self.orders[select] + quantity > option['stock']:
                    print("I'm sorry but we don't have enough of those left to add that to your order")
                    log = f'bad stock | user.add_item | {select} | {quantity}'
                    return log
                self.orders[select] += quantity
                self._total_items += quantity
                # item_cost = option['price'] * self.orders[select]
                add_cost = option['price'] * quantity
                self.user_cost += add_cost
                print('** You added', quantity, 'order(s) of', option['item'], 'adding', CURRENCY, '{:.2f}'.format(add_cost), 'for your meal **')
                log = f'user.add_item | {select} | {quantity}'
                # if we don't actually have any of this item, remove from keys
                if self.orders[select] == 0:
                    del self.orders[select]
        return log

    def remove_item(self, select, quantity=1):
        """ This will decrease the quantity of the given menu item from the
            user's current selection. We have already made sure the input is a
            valid menu item. However, we have not yet checked if the user
            actually has any selected to purchase, or they are not trying to
            remove more than they actually have ordered (be careful not to
            decrease below zero).
        """
        MENU = self.menu
        lg = 'start'  # over-written later
        for food in MENU:
            if food['item'].lower() == select:
                # make sure user actually has some in orders
                if select not in self.orders.keys() or self.orders[select] == 0:
                    print("Oh, it seems you don't have any", select, "so I don't need to remove anything")
                    lg = f'user.remove_item | had none | {select}'
                    return lg
                if quantity > self.orders[select]:
                    print("You don't actually have that many of", select)
                    print("Since you only have", self.orders[select], "I'll remove all of them")
                    quantity = self.orders[select]
                self.orders[select] -= quantity
                self._total_items -= quantity
                print('I have removed', quantity, 'of', select, 'from your order')
                self.user_cost -= quantity * food['price']
                lg = f'user.remove_item | {select} | '
                if self.orders[select] == 0:
                    print('You have no', select, 'in your order')
                    del self.orders[select]
                    lg += '0'
                    return lg
                print('** You have', self.orders[select], 'order(s) of', food['item'], 'for your meal **')
                lg += str(self.orders[select])
                return lg
        lg = f'bad item | user.remove_item | {select}'
        return lg

    def display_order(self):
        """ This displays to the user's terminal the current state of what the
            user is ordering and current total cost of that order (incl tax)
        """
        long_string = ''
        for line in self._prep_order():
            long_string += line + '\n'
            print(line)
        return long_string

    def _prep_order(self):
        """ This prepares the text lines for both the display_order
            and print_receipt methods.
        """
        MENU = self.menu
        user_cost = 0
        line1 = 'Here is your current order.'
        line2 = "Choose: 'quit', 'remove <item>', view 'menu', 'order', or 'print'"
        content = []
        content.append('*' * WIDTH)
        content.append('** ' + ' ' * ((WIDTH - len(line1)) // 2 - 3) + line1 + ' ' * (((WIDTH - len(line1)) // 2 - 3) + len(line1)%2) + ' **')
        content.append('-' * WIDTH)
        content.append('** ' + ' ' * ((WIDTH - len(self.uid)) // 2 - 3) + self.uid + ' ' * (((WIDTH - len(self.uid)) // 2 - 3) + len(self.uid) % 2) + ' **')
        content.append('-' * WIDTH)
        content.append(' Item' + ' ' * ((WIDTH - 44) // 2 + 6) + 'Quantity' + ' ' * (WIDTH // 2 + (WIDTH - 44) % 2 - 3) + 'Price')
        for options in MENU:
            # yes, refactor MENU as dict would be better. Get working for now
            item = options['item'].lower()
            if item in self.orders.keys():
                item_cost = self.orders[item] * options['price']
                # maybe aim for 25-30 for item, 5-6 for quantity, 8 for money
                line = '{:30}'.format(options['item']) + '{:^5}'.format(self.orders[item]) + ' ' * (WIDTH - 42) + CURRENCY + '{:>6}'.format('{:.2f}'.format(item_cost))
                content.append(line)
                user_cost += item_cost
        if self.user_cost != user_cost:
            content.append('Somehow our order tracking has an error')
            content.append(f'Running ttl: {self.user_cost}, Computed ttl: {user_cost}')
            content.append('We are giving you the lower computation')
            user_cost = min(self.user_cost, user_cost)
            self.user_cost = user_cost
        content.append(f'''Your order comes to: {CURRENCY} {'{:>6}'.format('{:.2f}'.format(user_cost))}''')
        content.append(f'''Plus tax: {CURRENCY} {'{:>6}'.format('{:.2f}'.format(user_cost * SALES_TAX))}''')
        content.append(f'''Total Bill: {CURRENCY} {'{:>6}'.format('{:.2f}'.format(user_cost + user_cost * SALES_TAX))}''')
        content.append(f'''{'-' * WIDTH}''')
        content.append(f'''{'** ' + ' ' * ((WIDTH - len(line2)) // 2 - 3) + line2 + ' ' * (((WIDTH - len(line2)) // 2 - 3) + len(line2)%2) + ' **'}''')
        content.append(f'''{'*' * WIDTH}''')
        content.append(f'''What would you like to do now?''')
        return content

    def print_receipt(self, path=None):
        """ This will create a file so that we have a record of this order
            The created file name will be the order uuid.txt
            The output will look the same as display_order
        """
        content = self._prep_order()
        filename = f'{self.uid}.txt'
        if path is not None:
            filename = path + filename
            # put in for testing if somehow we can't create file at a location
            # do we want to throw away a given path?
        try:
            with open(filename, "w+") as f:
                for line in content:
                    f.write(line + '\n')
                # f.close()
                # Not neccassary to 'close()' a file when using 'with'
        except IOError:
            print("File not found or path is incorrect")
            return f'<bad user.print_receipt | {filename}>'
        return f'<user.print_receipt | {filename}>'

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
                print('** ', option['item'], ' ' * (WIDTH - len(option['item']) - 17), CURRENCY, '{:>5}'.format('{:.2f}'.format(option['price'])), ' **')
    ask = 'What would you like to order?'
    instructions = "You can view your 'order', or type the food you want to add"
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(ask)) // 2 - 3) + ask + ' ' * ((WIDTH - len(ask)) // 2 - 3 + len(ask) % 2) + ' **'}
        {'** ' + ' ' * ((WIDTH - len(instructions)) // 2 - 3) + instructions + ' ' * ((WIDTH - len(instructions)) // 2 - 3 + len(instructions) % 2) + ' **'}
        {'*' * WIDTH}
    '''))


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


def parse_user_input(select, user, MENU):
    """ Gets an input from the user. Determines if it is a special command,
    and if so, calls the appropriate function. This is first called after
    the user initially sees the menu. In our program this is called inside
    of a loop so that we can continue to get user commands. This will continue
    until the user selects 'quit'. The user can request to see all, or some
    sections of the menu, to remove 1 or multiple of a certain item in their
    order, to add 1 or multiple of an item, to view their current order with
    total (including tax), to print a receipt, or to quit.
    """
    # Valid Inputs: quit, print, order, menu, <menu-section>,
    # remove <item> [quantity], <item> [quantity]
    # the [quantity] parts are optional integer inputs.
    quantity = 0
    log = ''
    if select == 'quit' or select == '':
        return select
    if select == 'print':
        log = user.print_receipt()
        return log
    if select == 'menu' or select.capitalize() in COURSES:
        show_menu(select.capitalize(), MENU)
        log = f'show_menu | {select}'
        return log
    if select == 'order':
        user.display_order()  # disply their current order and total
        log = f'user.display_order'
        return log
    if select in [elem['item'].lower() for elem in MENU]:
        user.add_item(select)
        log = f'user.add_item | {select} | 1'
        return log
    # we need to try to split the command to see if it is remove, item
    # pair or if it is add_item. Also deal with optional quantity of each
    if select.split()[0] == 'remove':
        command, *input_split = select.split()
        try:
            quantity = int(input_split[-1])
        except ValueError:
            quantity = 1
            input_split.append(1)
        item_name = ' '.join(input_split[:-1])
        if item_name in [elem['item'].lower() for elem in MENU]:
            # check for removing an invalid amount.
            if quantity < 1:
                log = f'bad remove not_positive_int | {quantity}'
                return log
            user.remove_item(item_name, quantity)
            log = f'user.remove_item | {item_name} | {quantity}'
            return log
        log = f'bad | user.remove_item | {item_name}'
        return log
    lst = select.split()
    try:
        quantity = int(lst[-1])
    except ValueError:
        log = f'bad not_int | {lst[-1]}'
        return log
    if quantity < 1:
        log = f'bad not_positive_int | {lst[-1]}'
        return log
    item_name = ' '.join(lst[:-1])
    if item_name in [elem['item'].lower() for elem in MENU]:
        user.add_item(item_name, quantity)
        log = f'user.add_item | {item_name} | {quantity}'
        return log
    log = f'bad | user.add_item | {item_name} | {quantity}'
    return log


def get_menu(new_menu):
    """This will pull up the menu in the csv file noted in the constant declares.
    If for some reason this file cannot be opened, we will ask the user again.
    The order of data in MENU_FILE is 'item', 'category', 'price', 'stock'
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
    # we will throw away the file path when calling get_menu
    file = file_structure[len(file_structure)-1].split('.')
    extension = file[len(file)-1]
    if extension != 'csv':
        print('Oops, we can only accept a CSV file.')
        return select_menu()
    return get_menu(file[0])


def run():
    """This is the main function, called when this file is ran.
    """
    global MENU
    MENU = select_menu()
    greeting()
    show_menu('menu', MENU)
    user = Order(CURRENCY, MENU)
    select = ''
    while select != 'quit':
        select = str(input('<: ')).lower()
        select = parse_user_input(select, user, MENU)
        if select.split(' ')[0] == 'bad':
            print('** Sorry, I am not sure I understood what you wanted **')
        print('Current Sub-Total: ', CURRENCY, '{:.2f}'.format(user.user_cost))
    goodbye()


if __name__ == '__main__':
    """ If this file was called directly, go to the run() function.
    """
    try:
        run()
    except(KeyboardInterrupt):
        goodbye()
