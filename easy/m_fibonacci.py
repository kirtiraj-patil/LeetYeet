# fibonacci series: previous two numbers add to find the current
# 1,1,2,3,5,8,13...

# find nth fib num
def fib(n):
    if(n == 1 or n == 2):
        return 1

    series = [1,1]
    current = 2 # 3rd fib num
    while current < n:
        series.append(series[current - 1] + series[current - 2])
        current += 1

    return series[-1]

n = int(input('enter which fib no to find: '))
print(fib(n))