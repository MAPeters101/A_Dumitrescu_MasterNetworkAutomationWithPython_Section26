
def difference(a, b):
    result = a - b
    return result

#print(difference())
#print(difference(1))
#print(difference(1, 5, 6))
print(difference(1, 5))


def func1(x, y):
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')

func1('Python', 55)
func1(55, 'Python')
print()


def func2(x, y, z):
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')
    print(f'3rd parameter z is {z}')

func2(y=7, x=3, z=9)
print()
func2(10, 20, 30)
print()
func2(6, z=1, y=9)
print()
#func2(x=6, 1, z=9)
func2(x=6, y=1, z=9)




