# sum of n natural nos without recursion
def sum_nnos(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum
print(sum_nnos(4))
#using recursion
def recursive_sum(n):
    if n<=1:
        return n
    return n+recursive_sum(n-1)

print(recursive_sum(4))


#print 1 to n using recursion

def print_till_n(i,n):
    if n==0:
        return
    print(i)
    print_till_n(i+1,n-1)
print_till_n(1,5)