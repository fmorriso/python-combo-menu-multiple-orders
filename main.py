import sys

from restaraunt import *
from single_order import SingleOrder

# define the list that will hold multiple multiple_orders
order = []
multiple_orders = []


def new_order():

    order[IDX_TOTAL_COST] = 0

    order[IDX_SANDWICH_TYPE] = "None"
    order[IDX_SANDWICH_COST] = 0

    order[IDX_BEVERAGE_SIZE] = "None"
    order[IDX_BEVERAGE_COST] = 0

    order[IDX_FRIES_SIZE] = "None"
    order[IDX_FRIES_COST] = 0

    order[IDX_DISCOUNT_APPLIED] = False


def get_sandwich() -> list:
    if not get_yes_no_answer("Would you like a sandwich?>"):
        return

    # create prompt
    prompt = "Which sandwich would you like to order: ("
    for idx in range(IDX_SANDWICH_CHICKEN, IDX_SANDWICH_TOFU + 1):
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += ") ?>"

    idx = -1
    while idx == -1:
        choice = input(prompt)
        if choice is None or len(choice) == 0:
            choice = "unknown"
        choice = choice[:1].lower()
        match choice[:1]:
            case 'c':
                idx = IDX_SANDWICH_CHICKEN

            case 'b':
                idx = IDX_SANDWICH_BEEF

            case 't':
                idx = IDX_SANDWICH_TOFU

            case _:
                print('Invalid sandwich choice. Try again.')

    order[IDX_SANDWICH_TYPE] = descrs[idx]
    order[IDX_SANDWICH_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]

    sandwich = [descrs[idx], prices[idx]]
    return sandwich


def get_beverage():
    if not get_yes_no_answer("Would you like a beverage?>"):
        return

    # create prompt
    prompt = "Which beverage size you like to order: ("
    for idx in range(IDX_BEVERAGE_SMALL, IDX_BEVERAGE_LARGE + 1):
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += ") >"

    idx = -1
    while idx == -1:
        choice = input(prompt)
        if choice is None or len(choice) == 0:
            choice = "unknown"
        choice = choice[:1].lower()

        match choice[:1]:
            case 's':
                idx = IDX_BEVERAGE_SMALL

            case 'm':
                idx = IDX_BEVERAGE_MEDIUM

            case 'l':
                idx = IDX_BEVERAGE_LARGE

            case _:
                print('Invalid beverage size. Try again.')

    order[IDX_BEVERAGE_SIZE] = descrs[idx]
    order[IDX_BEVERAGE_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]


def get_fries():
    if not get_yes_no_answer("Would you like fries?>"):
        return

    # create prompt
    prompt = "Which fries size you like to order: "
    for idx in range(IDX_FRIES_SMALL, IDX_FRIES_LARGE + 1):
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += " ?>"

    idx = -1
    while idx == -1:
        choice = input(prompt)
        if choice is None or len(choice) == 0:
            choice = "unknown"
        choice = choice[:1].lower()
        match choice[:1]:
            case 's':
                idx = IDX_FRIES_SMALL
                yesno = get_yes_no_answer('Do you want to super-size to large size?>')
                if yesno:
                    idx = IDX_FRIES_LARGE

            case 'm':
                idx = IDX_FRIES_MEDIUM

            case 'l':
                idx = IDX_FRIES_LARGE

            case _:
                print('Invalid fries size. Try again.')

    order[IDX_FRIES_SIZE] = descrs[idx]
    order[IDX_FRIES_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]


def get_ketchup_packets():
    if not get_yes_no_answer("Would you like any ketchup packets?>"):
        return

    per_each_cost = prices[IDX_KETCHUP_PACKETS]
    n = get_quantity(f"How many ketchup packets would you like at ${per_each_cost:.2f} each", 1, 10)

    order[IDX_NUM_KETCHUP_PACKETS] = n
    order[IDX_KETCHUP_PACKETS_COST] = n * per_each_cost
    order[IDX_TOTAL_COST] += order[IDX_KETCHUP_PACKETS_COST]


def check_for_discount():
    if order[IDX_SANDWICH_COST] > 0 and order[IDX_BEVERAGE_COST] > 0 and order[IDX_FRIES_COST] > 0:
        order[IDX_DISCOUNT_APPLIED] = True
        order[IDX_TOTAL_COST] -= 1


def display_order():
    output = 'Your order:'

    # add sandwich information
    item_name = 'Sandwich:'
    output += f'\n\t{item_name:12}'
    if order[IDX_SANDWICH_TYPE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_SANDWICH_TYPE]:10} ${order[IDX_SANDWICH_COST]:6.2f}'

    # add beverage information
    item_name = 'Beverage:'
    output += f'\n\t{item_name:12}'
    if order[IDX_BEVERAGE_SIZE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_BEVERAGE_SIZE]:10} ${order[IDX_BEVERAGE_COST]:6.2f}'

    # add fries information
    item_name = 'Fries:'
    output += f'\n\t{item_name:12}'
    if order[IDX_FRIES_SIZE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_FRIES_SIZE]:10} ${order[IDX_FRIES_COST]:6.2f}'

    # show ketchup packets, if any were requested
    item_name = 'Ketchup Packets:'
    if order[IDX_KETCHUP_PACKETS_COST] > 0:
        output += f'\n\t{item_name:17} {order[IDX_NUM_KETCHUP_PACKETS]:-4} ${order[IDX_KETCHUP_PACKETS_COST]:6.2f}'
    else:
        output += f'\n\t{item_name:17} none'

    # show discount if applied
    if order[IDX_DISCOUNT_APPLIED]:
        item_name = 'Discount:'
        item_value = -1.0
        output += f'\n\t{item_name:22} ${item_value:6.2f}'

    # total cost
    output += f'\n{"Total:":26} ${order[IDX_TOTAL_COST]:6.2f}'

    print(output)


def get_yes_no_answer(question: str) -> bool:
    while True:
        answer = input(question)
        if answer is None or len(answer) == 0:
            print("please respond with y, n, Yes, yes, No or no")
        else:
            answer = answer.lower()[:1]
            match answer:
                case 'y':
                    return True

                case 'n':
                    return False

                case _:
                    print("please respond with y, n, Yes, yes, No or no")


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_quantity(question: str, min: int = 0, max: int = 10) -> int:
    """Prompt for a number between min and max"""
    question = f'{question} (between {min} and {max})?>)'
    count: int = min - 1
    while count < min or count > max:
        try:
            count = int(input(question))
            if count < min or count > max:
                print(f'Please enter a number between {min} and {max}.')
            else:
                return count
        except ValueError:
            print(f'Please enter a value between {min} and {max}')


def get_order() -> None:
    global multiple_orders, order
    new_order()
    get_sandwich()
    get_beverage()
    get_fries()
    get_ketchup_packets()
    check_for_discount()

    # strange "TRICK" needed to keep multiple_orders list from getting corrupted
    multiple_orders.append([])
    print(f'DEBUG 1 multiple_orders: {multiple_orders}')
    # CORRUPTS: multiple_orders.append(order)
    multiple_orders[len(multiple_orders) - 1] = order
    print(f'DEBUG 2 multiple_orders: {multiple_orders}')
    display_order()
    print(f'DEBUG 3 at the bottom of get_order(), multiple_orders = {multiple_orders}')


def display_multiple_order(i):
    single_order = multiple_orders[i]
    print(single_order)


if __name__ == '__main__':
    print(f'Combo Menu with multiple multiple_orders and python version {get_python_version()}')
    get_order()

    print(f'DEBUG: after first order, multiple_orders = {multiple_orders}')
    while get_yes_no_answer("Do you want to make another order?>"):
        get_order()
        print(f'DEBUG: after next order, multiple_orders = {multiple_orders}')

    if get_yes_no_answer("Do you want to view all multiple_orders?>"):
        print(f'DEBUG: Before for loop, multiple_orders = {multiple_orders}')
        for i in range(len(multiple_orders)):
            display_multiple_order(i)
