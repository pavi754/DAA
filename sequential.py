def sequential_search(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      return i
  return -1
arr=[int (x) for x in input("enter the elements of the array,separated by space:").split()]
target=int(input("enter the largest element:"))
result=sequential_search(arr,target)
if result!=-1:
  print("element",target,"fount at index",result)
else:
  print("element",target,"not found in the array:")
