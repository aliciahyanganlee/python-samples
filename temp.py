def print_swap(x, y):
    temp = x
    # x = 10 y = 20 temp = 10
    x = y
    # x = 20 y = 20 temp = 10 
    y = temp
    print('{} {}'.format(x,y))

print_swap(10, 20)
print_swap('창식, 정은'))