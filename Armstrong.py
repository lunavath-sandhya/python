def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit ** num_digits
        temp_num //= 10
        return sum_of_powers == num
for n in [153, 370, 9474, 123]:
    if is_armstrong(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
