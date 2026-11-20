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

# print fact of number using recursion

def factorial(n):
    if n == 0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

# reverse an array using recursion

def rev_array(num,l,r):
    if l>=r:
        return num
    num[l],num[r]=num[r],num[l]
    return rev_array(num,l+1,r-1)

print(rev_array([2,3,4,5],0,len([2,3,4,5])-1))

# check if string is palindrome

def palindrome(s,l,r):
    if l>=r:
        return "Palindrome"
    if s[l]==s[r]:
        return palindrome(s,l+1,r-1)
    else:
        return "Not a palindrome"
print(palindrome("abcd",0,len('abcd')-1))

# fibonacci usinh recursion

def fibonacci(n):
    if n==0:
        return 0
    if n ==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))