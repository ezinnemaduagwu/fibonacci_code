fib = lambda x : x if x <2  else fib(x-1) + fib(x-2)
try:
    n = int(input('What is the value of fibonnacci you want to find'))
    result = map(fib,range(n+1))
    print(list(result))
except :
    print('Please input a integer')

