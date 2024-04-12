def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeNumbers(minimum, maximum):
    prime_list = []
    for num in range(minimum, maximum + 1):
        if prime(num):
            prime_list.append(num)
    return prime_list


min_num = 10
max_num = 30
print(primeNumbers(min_num, max_num))
