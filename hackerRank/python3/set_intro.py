def average(array):
    # your code goes here
    
    set_arr = set(array)
    
    # get number of elements in set
    n_int = 0
    for i in set_arr:
        n_int += 1
    
    return sum(set_arr) / n_int
