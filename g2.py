# question 2

q=int(input("enter the no."))
def fizz_buzz(q):
    if q%3==0:
        return 'Fizz'
    elif q%5==0:
        return 'Buzz'
    else:
        return q
print(fizz_buzz(q))
