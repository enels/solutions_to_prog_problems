# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# get the number of shows
n_shoes = int(input())

# counter to store a count of each show sizes
sizes_counter = Counter()

# get the sizes
sizes = input().split(" ")

# count the sizes
for s in sizes:
    sizes_counter[int(s)] += 1

# get the number of customers
customers = int(input())

# total cost
total_cost = 0

# get the shoe size and the prize from each customer
for customer in range(customers):
    shoe_to_buy = input().split(" ")
    
    # checks if shoe is still available
    if sizes_counter[int(shoe_to_buy[0])] != 0:
        
        # reduce the number of shoe size count by 1
        sizes_counter[int(shoe_to_buy[0])] -= 1
        
        # add the cost of the shoe
        total_cost += int(shoe_to_buy[1])

# print the total cost
print(total_cost)
