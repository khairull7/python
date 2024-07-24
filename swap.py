def modify_array(L):
    if len(L) != 9:
        raise ValueError("Array length must be 9")
    
    last = L[8]
    first = L[0]
    middle = L[4]

    L[0] = last
    L[4] = first
    L[8] = middle

    return L

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]

modified_L1 = modify_array(L1)
modified_L2 = modify_array(L2)

print(modified_L1)
print(modified_L2)
