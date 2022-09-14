def solution(arr):
    k = 2
    n = len(arr)
    # sort the array
    arr.sort()
 
    if (k == 1 and arr[n - 2] != arr[n - 1]):
        # print( arr[n - 1] )
        return arr[n]

    count = 1
 
    for i in range(n - 2, -1, -1) :
        if (arr[i] == arr[i + 1]):
            count += 1
        else:
            count = 1

        if (count == k and (i == 0 or (arr[i - 2] != arr[i] ))):
            print(arr[i])
            return arr[i]
 
    # if there is no such element
    print(arr[i])
    return arr[i]



def solution2(s):

    fre = [0]*26
    n = len(s)
    for i in range(n):
        fre[ord(s[i]) - ord('a')] += 1
 
    count = 0
    for i in range(26):
        if (fre[i] % 2):
            count += 1
 
    if (count == 0 or count == 1):
        return 0
    else:
        return count - 1

# Driver code
if __name__ == "__main__":
     
    arr = [3,2,4,2,3,3,2]
    k = 2
    n = len(arr)
    solution(arr)

    s = "mayappa"

    print(solution2(s))