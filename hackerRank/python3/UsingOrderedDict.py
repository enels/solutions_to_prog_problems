# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

# get number of items
n_items = int(input())

# container to store the itmes
item_dict = OrderedDict()

for _ in range(n_items):
    
    # get item from user, splitting each value keyed in
    item_name_and_price = input().split()
    
    # get item price which is the last index in the list
    item_price = int(item_name_and_price[-1])
    
    # get item name by concatenating the first and last
    item_name = item_name_and_price[:-1]
    
    # stringify the name from list
    str_name = ""
    for name in item_name:
        str_name += name
        str_name += " "
    
    # strip off the right most spacd left after concatenating it
    str_name = str_name.rstrip()
    
    # check if item already exists
    if str_name in item_dict.keys():
        item_dict[str_name] += item_price
    else:
        item_dict[str_name] = item_price

for item, price in item_dict.items():
    print(item, price)



