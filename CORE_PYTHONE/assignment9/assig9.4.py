def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)


n = int(input("Enter a number: "))

res = sum_numbers(n)

print("Sum =", res)