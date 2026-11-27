#divide 
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)


# merge 2 sorted arrays
def merge(left,right):
    n=len(left)
    m=len(right)
    i,j=0,0
    result=[]
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left(i))
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result
print(merge_sort([4,3,5,2,1,6]))

#TC->O(nlogn)
#SC->O(n)
