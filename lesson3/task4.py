def task4(p,n):
    i = 1
    while i ** p <= n:
        print(i ** p, end=',')
        i += 1

    print("\nПоследнее число,"
          " возведенное в степень:", i - 1)


p = int(input())
n = int(input())
task4(p,n)