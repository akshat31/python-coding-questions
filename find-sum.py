def twoSum(arr, sum):
    arr.sort()
    left=0
    right= len(arr) - 1
    while left<=right:
        if arr[left] + arr[right] > sum:
            right = right - 1
        elif arr[left] + arr[right] < sum:
            left = left + 1
        elif arr[left] + arr[right] == sum:
            print("Value of pair are", arr[left], "&", arr[right])
            right= right + 1
            left = left + 1

arr = [4, 5, 3 ,2, 9, 5, 7, 3, 4, 6, 9, 0, 7, 1, 22, 33, 12, 56]
sum = 17
twoSum(arr, sum)