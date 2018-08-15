from textwrap import dedent
import sys


CURRANCY = '$'
SALES_TAX = 0.101
WIDTH = 78
MENU = [
    {
        'item': 'Wings',
        'category': 'Appetizers',
        'price': 10.00,
        'status': 0,
    },
    {
        'item': 'Cookies',
        'category': 'Appetizers',
        'price': 5.00,
        'status': 0,
    },
    {
        'item': 'Spring Rolls',
        'category': 'Appetizers',
        'price': 9.00,
        'status': 0,
    },
    {
        'item': 'Sliders',
        'category': 'Appetizers',
        'price': 10.00,
        'status': 0,
    },
    {
        'item': 'Nachos',
        'category': 'Appetizers',
        'price': 8.00,
        'status': 0,
    },
    {
        'item': 'Rib Tips',
        'category': 'Appetizers',
        'price': 12.00,
        'status': 0,
    },
    {
        'item': 'Salmon',
        'category': 'Entrees',
        'price': 21.00,
        'status': 0,
    },
    {
        'item': 'Steak',
        'category': 'Entrees',
        'price': 31.00,
        'status': 0,
    },
    {
        'item': 'Meat Tornado',
        'category': 'Entrees',
        'price': 28.00,
        'status': 0,
    },
    {
        'item': 'A Literal Garden',
        'category': 'Entrees',
         'price': 19.00,
        'status': 0,
    },
    {
        'item': 'Chicken Alfredo',
        'category': 'Entrees',
        'price': 14.00,
        'status': 0,
    },
    {
        'item': 'Pizza',
        'category': 'Entrees',
        'price': 41.00,
        'status': 0,
    },
    {
        'item': 'Ice Cream',
        'category': 'Desserts',
        'price': 7.00,
        'status': 0,
    },
    {
        'item': 'Cake',
        'category': 'Desserts',
         'price': 8.00,
       'status': 0,
    },
    {
        'item': 'Pie',
        'category': 'Desserts',
        'price': 6.00,
        'status': 0,
    },
    {
        'item': 'ChocoTower',
        'category': 'Desserts',
        'price': 12.00,
        'status': 0,
    },
    {
        'item': 'Pudding',
        'category': 'Desserts',
        'price': 4.00,
        'status': 0,
    },
    {
        'item': 'Flan',
        'category': 'Desserts',
        'price': 7.00,
        'status': 0,
    },
    {
        'item': 'Coffee',
        'category': 'Drinks',
        'price': 14.00,
        'status': 0,
    },
    {
        'item': 'Tea',
        'category': 'Drinks',
        'price': 3.00,
        'status': 0,
    },
    {
        'item': 'Blood of the Innocent',
        'category': 'Drinks',
        'price': 6.66,
        'status': 0,
    },
    {
        'item': 'Soda',
        'category': 'Drinks',
        'price': 2.00,
        'status': 0,
    },
    {
        'item': 'Memosa',
        'category': 'Drinks',
        'price': 8.00,
        'status': 0,
    },
    {
        'item': 'Cocktail',
        'category': 'Drinks',
        'price': 0.50,
        'status': 0,
    },
    {
        'item': 'Fries',
        'category': 'Sides',
        'price': 4.00,
        'status': 0,
    },
    {
        'item': 'Onion Rings',
        'category': 'Sides',
        'price': 6.00,
        'status': 0,
    },
    {
        'item': 'Vegi',
        'category': 'Sides',
        'price': 3.00,
        'status': 0,
    },
    {
        'item': 'Potato',
        'category': 'Sides',
        'price': 4.00,
        'status': 0,
    },
    {
        'item': 'Bread',
        'category': 'Sides',
        'price': 2.00,
        'status': 0,
    },
    {
        'item': 'Cheese',
        'category': 'Sides',
        'price': 8.00,
        'status': 0,
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


def show_menu(selection):
    """Function can display all item on the menu, or all items
    in a specific category of the menu if requested by user input.
    """
    display = [selection]
    if selection.lower() == 'menu':
        display = COURSES
    for section in display:
        print('\n** ' , section, '\n** ', '-' * 8)
        for option in MENU:
            if option['category'] == section:
                print('** ', option['item'], ' ' * (WIDTH - len(option['item']) - 17), CURRANCY, '{:>5}'.format('{:.2f}'.format(option['price'])), ' **')
    ask = 'What would you like to order?'
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(ask)) // 2 - 3) + ask + ' ' * ((WIDTH - len(ask)) // 2 - 3 + len(ask) % 2) + ' **'}
        {'*' * WIDTH}
    '''))


def get_order(select):
    """Takes in a value that exists in our MENU item names.
    It then adds this item to the user's order.
    """
    for option in MENU:
        if select == option['item'].lower():
            option['status'] += 1
            # user_cost += option['price']
            # perhaps we deal with total cost later on.
            print('** You have', option['status'], 'order(s) of', option['item'], 'for your meal **')
            return


def display_order():
    """This displays the current state of what the user is ordering and
    the current total cost of that order.
    """
    # food_list = ''
    user_cost = 0
    # food_list = [food['item'] for food in MENU if food['status'] > 0]
    # for food in MENU:
    #     if food['status'] > 0:
    #         food_list += food['item']
    #         user_cost += food['price'] * food['status']
    # The printout formatting maybe should be moved to an external function
    line1 = 'Here is your current order.'
    line2 = "You can 'quit', 'delete <item>', or view 'menu', 'order'"
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(line1)) // 2 - 3) + line1 + ' ' * (((WIDTH - len(line1)) // 2 - 3) + len(line1)%2) + ' **'}
        {'-' * WIDTH}
    '''))
    for options in MENU:
        if options['status'] > 0:
            user_cost += options['status'] * options['price']
            line = 'You have ' + str(options['status']) + ' orders of ' +  options['item'] + ' for ' + CURRANCY + str(options['price'] * options['status'])
            print('** ' + ' ' * ((WIDTH - len(line)) // 2 - 3) + line + ' ' * (((WIDTH - len(line)) // 2 - 3) + len(line)%2) + ' **')
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


def parse_user_input():
    """ Gets an input from the user. Determines if it is a special command,
    and if so, calls the appropriate function. This is first called after
    the user initially sees the menu. It can handle the 'quit' command to
    exit, and otherwise it keeps looping asking and handling the user's request.
    The user can request to see all, or some sections of the menu, to remove
    1 item in their order, to view their current order and total, or to quit
    """
    select = ''
    while select != 'quit':
        select = str(input()).lower()
        if select == 'quit':
            return
        elif select == 'menu' or select.capitalize() in COURSES:
            show_menu(select.capitalize())
        elif select == 'order':
            display_order() #disply their current order and total
        elif select in [elem['item'].lower() for elem in MENU]:
            get_order(select)
        # we need to try to split the command to see if it is delete, item pair
        elif select == 'delete': #starts with delete
            # remove 1 item of this kind
            #display their current order and total
            pass
        else:
            #user input did not match any of the valid inputs.
            print('** Sorry, I am not sure I understood what you wanted **')


def run():
    """This is the main function, which calls the other functions to do the main work
    """
    greeting()
    show_menu('Menu')
    parse_user_input() #This does most of our programs work
    goodbye()


if __name__ == '__main__':
    run()
