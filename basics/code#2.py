# factors of a number

# brute force
def find_factors(n):
    num=n
    result=[]
    for i in range(1,num//2+1):
        if num%i==0:
            result.append(i)
    result.append(num)
    return result
'''factors=find_factors(20)
for i in factors:
    print(i)'''

# optimal solution 
from math import sqrt
def optimal_factors(n):
    num=n
    result=[]
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if num//i!=0:
                result.append(num//i)
    return result
'''lst=optimal_factors(20)
lst.sort()
for i in lst:
    print(i)'''

# counting frequency
def count_frequency(lst):
    freq_map={}
    for i in range(0,len(lst)):
        if lst[i] in freq_map:
            freq_map[lst[i]]+=1
        else:
           freq_map[lst[i]]=1
    return freq_map
'''freq=count_frequency([1,1,4,2,4,1])
for k,v in freq.items():
    print(f"{k}:{v}")'''

# method 2 using get
def count_freq(nums):
    dict={}
    for i in range(len(nums)):
        dict[nums[i]]=dict.get(nums[i],0)+1
    return dict
freq=count_freq([1,1,4,2,4,1])
for k,v in freq.items():
    print(f"{k}:{v}")



