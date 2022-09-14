#find sum of digits
def digitSum(n):
    sum = 0
    while (n):
        sum += (n % 10)
        n = n // 10
    return sum

def solution(arr):
    # n = int(len(arr))
    mp = {}
    ans = -1
    pairi = 0
    pairj = 0
    for i in range(len(arr)):
        temp = digitSum(arr[i])
        
        if (temp not in mp):
            mp[temp] = 0
         
        if (mp[temp] != 0) :
            if (arr[i] + mp[temp] > ans):
                pairi = arr[i]
                pairj = mp.get(temp)
                ans = pairi + pairj
             
        # Change the value in the map
        mp[temp] = max(arr[i], mp[temp])
    print(f"{pairi} {pairj} {ans}")
    return ans
 
# Driver Code Starts.
arr = [71, 51, 17, 42]
n = len(arr)
solution(arr)