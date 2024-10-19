# A fast algorith to check for the occurrence of an integer in a list
# worst case running time O(n)

s = ""
sample_list = [1, 2, 3, 4, 2, 6, 7]
l_len = len(l)

for i in range(1, l_len + 1):
    if str(l[i-1]) in s:
        print(l[i-1])
        break
    else:
        s += str(l[i-1])