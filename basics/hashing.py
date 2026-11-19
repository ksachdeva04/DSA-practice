n=[5,3,6,6,5,3,9,1]
m=[10,3,4,9,6]
#check the freq of each element in m in n
# 1<=n[i]<=10
#brute force
def check_freq(n,m):
    for num in m:
        count=0
        for nums in n:
            if nums==num:
                count+=1
        print(count)
check_freq(n,m)

#using hashing
def hash_freq(n,m):
    hash_list=[0]*11
    for i in n:
        hash_list[i]+=1
    for i in m:
        if i<1 or i>10:
            print(0)
        else:
            print(hash_list[i])
hash_freq(n,m)

# using dictionary
def dict_frequency(n,m):
    freq_dict={}
    for i in n:
        if i in freq_dict:
            freq_dict[i]+=1
        else:
            freq_dict[i]=1
    for i in m:
        if i in freq_dict:
            print(freq_dict[i])
        else:
            print(0)
dict_frequency(n,m)
        
