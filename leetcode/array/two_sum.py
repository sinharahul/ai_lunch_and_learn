nums = [2,7,11,15]
#https://leetcode.com/problems/two-sum/
def two_sum(arr,target):
    res=()
    dict={}
    for idx,elem in enumerate(arr):
      te=target-elem
      if te in dict:
          eidx=dict[te]
          return (eidx,idx)
      else:
          dict[elem]=idx
    return res

print(two_sum(nums,9))
