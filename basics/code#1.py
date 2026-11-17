# extract digits 
def extract_digits(num):
    while num>0:
        last_digit=num%10
        print(last_digit)
        num=num//10
#extract_digits(1234)

# palindrome
def check_palindrome(n):
    num=n
    result=0
    while num>0:
        ld=num%10
        result=(result*10)+ld
        num=num//10
    return result
'''n=504
x=check_palindrome(n)
if x==n:
    print('palindrome')
else:
    print('not a palindrome')'''

#armstrong number
def check_armstrong(n):
    num=n
    nod=len(str(num))
    total=0
    while num>0:
        ld=num%10
        total=total+ld**nod
        num=num//10
    return total==n
print(check_armstrong(154))
        


