# covers the condition if n is odd
 if n % 2 != 0:
        print("Weird")
    # covers the entire conditions if n is even
    elif n % 2 == 0:
        # covers the entire "Not Weird" conditions if n is even
        if (n >= 2 and n <= 5) or n > 20:
            print("Not Weird")

        # covers the "Weird" condition if n is even
        elif n >= 6 and n <= 20:
            print("Weird")