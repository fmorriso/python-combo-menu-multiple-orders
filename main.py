import sys

# define a list to hold a single order
order = []

# define and populate portions of the order based on ordinal position
IDX_TOTAL_COST = 0
order.append(0.0)

IDX_SANDWICH_TYPE = 1
order.append("None")

IDX_SANDWICH_COST = 2
order.append(0.0)

IDX_BEVERAGE_SIZE = 3
order.append("None")

IDX_BEVERAGE_COST = 4
order.append(0.0)

IDX_FRIES_SIZE = 5
order.append("None")

IDX_FRIES_COST = 6
order.append(0.0)

IDX_DISCOUNT_APPLIED = 7
order.append(False)

IDX_NUM_KETCHUP_PACKETS = 8
order.append(0)

IDX_KETCHUP_PACKETS_COST = 9
order.append(0.0)

# NOTE: indexes for descriptions and prices must be kept in sync with each other
descrs = []
prices = []

IDX_SANDWICH_CHICKEN = 0
descrs.append('Chicken')
prices.append(5.25)

IDX_SANDWICH_BEEF = 1
descrs.append('Beef')
prices.append(6.25)

IDX_SANDWICH_TOFU = 2
descrs.append('Tofu')
prices.append(5.75)

IDX_BEVERAGE_SMALL = 3
descrs.append('Small')
prices.append(1.0)

IDX_BEVERAGE_MEDIUM = 4
descrs.append('Medium')
prices.append(1.5)

IDX_BEVERAGE_LARGE = 5
descrs.append('Large')
prices.append(2.0)

IDX_FRIES_SMALL = 6
descrs.append('Small')
prices.append(1.0)

IDX_FRIES_MEDIUM = 7
descrs.append('Medium')
prices.append(1.5)

IDX_FRIES_LARGE = 8
descrs.append('Large')
prices.append(2.0)

IDX_KETCHUP_PACKETS = 9
descrs.append('Ketchup Packets')
prices.append(0.25)


# define the list that will hold multiple orders
orders = []


def new_order():
    global order
    # print(f'DEBUG: top of new_order: len(order) = {len(order)}')
    size: int = len(order)
    order = []
    for i in range(size):
        order.append(0)

    order[IDX_TOTAL_COST] = 0

    order[IDX_SANDWICH_TYPE] = "None"
    order[IDX_SANDWICH_COST] = 0

    order[IDX_BEVERAGE_SIZE] = "None"
    order[IDX_BEVERAGE_COST] = 0

    order[IDX_FRIES_SIZE] = "None"
    order[IDX_FRIES_COST] = 0

    order[IDX_DISCOUNT_APPLIED] = False


def get_sandwich() -> None:
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


def get_beverage():
    if not get_yes_no_answer("Would you like a beverage?>"):
        return

    # create prompt
    prompt = "Which beverage size you like to order: ("
    for idx in range(IDX_BEVERAGE_SMALL, IDX_BEVERAGE_LARGE + 1):
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += ")? >"

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
    prompt = "Which fries size you like to order: ("
    for idx in range(IDX_FRIES_SMALL, IDX_FRIES_LARGE + 1):
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
    """If customer orders a sandwich, a beverage and fries, give them the combo discount"""
    if order[IDX_SANDWICH_COST] > 0 and order[IDX_BEVERAGE_COST] > 0 and order[IDX_FRIES_COST] > 0:
        order[IDX_DISCOUNT_APPLIED] = True
        order[IDX_TOTAL_COST] -= 1


def display_order(i: int = -1) -> None:
    """Display a specific order from the orders list or just the current orde (when i is -1)"""
    global order
    output = ''
    if i == -1:  # current order only
        output += 'Your order:'
    else:
        output += f'Order number {i + 1}'
        order = orders[i]
    
    # width for printing category
    w_category = 17

    # width to use when printing item type or size
    w_name = 8
    
    # cost format
    w_cost = '6.2f'

    # add sandwich information
    item_name = 'Sandwich:'
    output += f'\n\t{item_name:{w_category}}'
    if order[IDX_SANDWICH_TYPE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_SANDWICH_TYPE]:{w_name}}${order[IDX_SANDWICH_COST]:{w_cost}}'

    # add beverage information
    item_name = 'Beverage:'
    output += f'\n\t{item_name:{w_category}}'
    if order[IDX_BEVERAGE_SIZE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_BEVERAGE_SIZE]:{w_name}}${order[IDX_BEVERAGE_COST]:{w_cost}}'

    # add fries information
    item_name = 'Fries:'
    output += f'\n\t{item_name:{w_category}}'
    if order[IDX_FRIES_SIZE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_FRIES_SIZE]:{w_name}}${order[IDX_FRIES_COST]:{w_cost}}'

    # show ketchup packets, if any were requested
    item_name = 'Ketchup Packets:'
    if order[IDX_KETCHUP_PACKETS_COST] > 0:
        output += f'\n\t{item_name:{w_category}}{order[IDX_NUM_KETCHUP_PACKETS]:<{w_name}}${order[IDX_KETCHUP_PACKETS_COST]:{w_cost}}'
    else:
        output += f'\n\t{item_name:{w_category}}none'

    # show discount if applied
    if order[IDX_DISCOUNT_APPLIED]:
        item_name = 'Combo discount:'
        item_value = -1.0
        output += f'\n\t{item_name:25}${item_value:{w_cost}}'

    # total cost
    w = 29
    # print(f'{w=}')
    output += f'\n{"Total:":{w}}${order[IDX_TOTAL_COST]:{w_cost}}'

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


def get_quantity(question: str, min_value: int = 0, max_value: int = 10) -> int:
    """Prompt for a number between min_value and max_value"""
    question = f'{question} (between {min_value} and {max_value})?>'
    count: int = min_value - 1
    while count < min_value or count > max_value:
        try:
            count = int(input(question))
            if count < min_value or count > max_value:
                print(f'Please enter a number between {min_value} and {max_value}.')
            else:
                return count
        except ValueError:
            print(f'Please enter a value between {min_value} and {max_value}')


def get_order() -> None:
    new_order()
    get_sandwich()
    get_beverage()
    get_fries()
    get_ketchup_packets()
    check_for_discount()
    display_order(-1)

    # print(f'DEBUG 1 orders: {orders=}')
    orders.append(order)
    # print(f'DEBUG at end of get_order(), {orders=}')


def display_all_orders():
    for i in range(len(orders)):
        display_order(i)


if __name__ == '__main__':
    print(f'Combo Menu with multiple orders using python version {get_python_version()}')
    # env_HOME = os.environ['HOME']
    # print(f'{env_HOME=}')
    # print(os.environ)
    # for e in os.environ:
    #     print(e)

    get_order()

    # print(f'DEBUG: after first order, orders = {orders}')
    while get_yes_no_answer("Do you want to make another order?>"):
        get_order()
        # print(f'DEBUG: after next order, orders = {orders}')

    if get_yes_no_answer("Do you want to view all orders?>"):
        # print(f'DEBUG: Before for loop, orders = {orders}')
        display_all_orders()
