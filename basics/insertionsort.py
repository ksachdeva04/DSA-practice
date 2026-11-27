# insertion sort makes use of 3 vars i,j and key to part list in unsorted and sorted category
#i is used for traversing the list j for comparison and key for storing the unsorted element 

def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
print(insertion_sort([3,7,4,2,1]))

# descending order

def insertion_sort_reverse(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]<key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
print(insertion_sort_reverse([3,7,4,2,1]))