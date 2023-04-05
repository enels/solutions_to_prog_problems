for i in range(my_list_len):
    try:
        my_list[my_list_len] = i
    except IndexError as e:
        print("Don't try buffer overflow attacks in Python!")