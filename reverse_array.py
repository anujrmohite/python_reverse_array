def reverse(nums):
    #pointing to the first item
    start_index=0
    #index pointing to the last item
    last_index=len(nums)-1
    while last_index>start_index:
        #keep swapping an item
        nums[start_index],nums[last_index]=nums[last_index],nums[start_index]
        start_index=start_index+1
        last_index=last_index-1
if __name__=='__main__':
    n=[1,2,3,4,5]
    reverse(n)
    print(n)
