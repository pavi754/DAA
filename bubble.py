def bubble_sort(arr):
  n=len(arr)
  for i in range(n-1):
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[int (x) for x in input("enter the elements of the array,separated by space:").split()]
bubble_sort(arr)
print("sorted array:",arr)
