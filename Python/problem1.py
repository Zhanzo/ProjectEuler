def main():
    sum_divisible = 0
    for i in range(3, 1000):
        if (i % 3 == 0 or i % 5 == 0):
            sum_divisible += i
    print(sum_divisible)

main()