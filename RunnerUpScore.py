#Takes n(number of elements in array) and arr(array elements) as inputs and produces the second largest number from the input array
n = int(input())
arr = map(int, input().split())
new_arr = set(arr)
m=max(new_arr)
new_arr.remove(m)
print(max(new_arr))
