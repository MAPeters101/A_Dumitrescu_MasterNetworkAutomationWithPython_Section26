
def add(x, y=10):
    print(f'x is {x} and y is {y}')
    print(f'{x} + {y} is {x + y}')
    print()

add(2, 3)
add(6)


# def add2(x, y=10, z):
#     print(f'x is {x} and y is {y} and z is {z}')
#     print(f'{x} + {y} + {z} is {x + y + z}')
#     print()
#
# add2(2, 3)


def add2(x, y=10, z=20):
    print(f'x is {x} and y is {y} and z is {z}')
    print(f'{x} + {y} + {z} is {x + y + z}')
    print()

add2(2, 3)
add2(4)
add2(6, 7, 8)
add2(x=9, z=7)




