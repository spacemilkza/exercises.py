#the fibonacci series program
#author: malesela
#company: spacemilk


def fibonacci():

    series_lim = int(input("Fabonacci Series Limit(max): "))
    series_start = int(input("Fabonacci Series Start(start): "))
    fib_list = []
    a, b = series_start, series_start + 1

    while a < series_lim:
        fib_list.append(a)
        a, b = b, a+b

    print(fib_list)

fibonacci()
