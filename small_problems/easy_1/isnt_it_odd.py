def is_abs_odd(num):
    return bool(abs(num) % 2)

print(is_abs_odd(0)) # False
print(is_abs_odd(1)) # True
print(is_abs_odd(-33)) # True
print(is_abs_odd(44)) # False
print(is_abs_odd(-120)) # False
