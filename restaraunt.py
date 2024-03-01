# define the list that will hold multiple orders
orders = []

# define each individual order as a list
order = []

# define where in a multiple order where the pieces will be stored:
IDX_MULTIPLE_SANDWICHES = 0
IDX_MULTIPLE_BEVERAGES = 1
IDX_MULTIPLE_FRIES = 2

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
prices.append(1.5)

IDX_FRIES_MEDIUM = 7
descrs.append('Medium')
prices.append(1.5)

IDX_FRIES_LARGE = 8
descrs.append('Large')
prices.append(2.0)

IDX_KETCHUP_PACKETS = 9
descrs.append('Ketchup Packets')
prices.append(0.25)
