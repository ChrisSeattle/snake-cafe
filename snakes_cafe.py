from textwrap import dedent
import sys


WIDTH = 78
MENU = [
    {
        'item': 'Wings',
        'category': 'Appetizers',
        'status': 0,
    },
    {
        'item': 'Cookies',
        'category': 'Appetizers',
        'status': 0,
    },
    {
        'item': 'Spring Rolls',
        'category': 'Appetizers',
        'status': 0,
    },
    {
        'item': 'Salmon',
        'category': 'Entrees',
        'status': 0,
    },
    {
        'item': 'Steak',
        'category': 'Entrees',
        'status': 0,
    },
    {
        'item': 'Meat Tornado',
        'category': 'Entrees',
        'status': 0,
    },
    {
        'item': 'A Literal Garden',
        'category': 'Entrees',
        'status': 0,
    },
    {
        'item': 'Ice Cream',
        'category': 'Desserts',
        'status': 0,
    },
    {
        'item': 'Cake',
        'category': 'Desserts',
        'status': 0,
    },
    {
        'item': 'Pie',
        'category': 'Desserts',
        'status': 0,
    },
    {
        'item': 'Coffee',
        'category': 'Drinks',
        'status': 0,
    },
    {
        'item': 'Tea',
        'category': 'Drinks',
        'status': 0,
    },
    {
        'item': 'Blood of the Innocent',
        'category': 'Drinks',
        'status': 0,
    },
]
COURSES = ['Appetizers', 'Entrees', 'Desserts', 'Drinks']


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


def show_menu():
    # menu_categories = set()
    # for option in MENU:
    #     for key in option:
    #         if key == 'category':
    #             menu_categories.add(option[key])
    for section in COURSES:
        print('\n', section, '\n', '-' * 8)
        for option in MENU:
            if option['category'] == section:
                print(option['item'])
    print('\n')
    ask = 'What would you like to order?'
    print(dedent(f'''
        {'*' * WIDTH}
        {'** ' + ' ' * ((WIDTH - len(ask)) // 2 - 3) + ask + ' ' * ((WIDTH - len(ask)) // 2 - 3 + len(ask) % 2) + ' **'}
        {'*' * WIDTH}
    '''))


def get_order(select):
    if select == 'quit':
        return
        # this section is redundent

    for option in MENU:
        if select == option['item'].lower():
            option['status'] += 1
            print('** You have', option['status'], 'order(s) of', option['item'], 'for your meal **')
            return

    print('** Sorry, I am not sure I understood what you wanted **')


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


def run():
    greeting()
    show_menu()
    select = ''
    while select != 'quit':
        select = str(input()).lower()
        get_order(select)
    goodbye()


if __name__ == '__main__':
    run()
