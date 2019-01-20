def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result=add_sub(12,65)
print(result)


#By using lambda

f=lambda a,b: a+b
result=f(12,43)
print(result)

#using filter map to reduce
def is_even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,9]
even= list(filter(is_even, nums))
print(even)

#another way to use lambda without def


nums=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,even)) #mul by 2
print(doubles)
