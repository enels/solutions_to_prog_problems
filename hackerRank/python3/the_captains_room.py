# Enter your code here. Read input from STDIN. Print output to STDOUT

# get the integer K size of each group
K = int(input())

# get the unordered elments of the room number list
room_number_list = list((map(int, input().split())))

# convert the room_number to set to get unique room numbers
room_number_set = set(room_number_list)

# get the dictionary to store the room number and the number of occurrences
room_count = dict()

# initialize each room count to zero
for i in room_number_set:
    room_count[i] = 0

# iterate through the room number list to get the room number values
for room_no in room_number_list:
    room_count[room_no] += 1

# find the captains room - room with value of 1
for k,v in room_count.items():
    if room_count[k] == 1:
        print(k)
        break

