#### Bottom-up Approach #######
class Solution(object):
    def climbStairs(N):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(N + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp[N])
        print('-------------------------------------\n')
        return dp[N]

        
    if __name__ == '__main__':
        climbStairs(4)  

###### Implementation of Recursive Approach #####

def climbStairs(N):
    if N < 2 :
        print(1)
        return 1
    else:
        return climbStairs(N-1) + climbStairs(N-2)


if __name__ == '__main__':
    climbStairs(4)