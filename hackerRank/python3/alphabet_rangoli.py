def print_rangoli(size):
    # your code goes here
    
    # get the full alphabet a-z
    for i in range(size):
        chars += chr(ord('a') + i)
        if i != size-1:
            chars += "-"
    
    # get the width of the pattern        
    width = len(chars)
    
    # get the height
    height = size * 2 - 1
    
    # get the mid line
    mid = size / 2
    
    # get the mid width
    mid_width = width / 2
    
    n_chars = 0
    for i in range(height):
        if i == 0 or i == height-1:
            for col in range(width):
                if col == mid_width+1:
                    print(chars[-1], end="")
                else:
                    print("-", end="")
        elif i < mid:
            letters = i + 2
            letters_dashes = letters + letters - 1
            for j in range(width):
                
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
