import heapq

def find_kth_smallest(nums,k):
  nums = heapq.nsmallest(k,nums)
  result = nums[-1]
  return result

nums=[10,5,3,7,8]
k=int(input("k번째 숫자를 입력해주세요 : "))
print(k,"번째로 작은 수 :",find_kth_smallest(nums,k))