
class Solution(object):
    def sumBase(n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        
        while n > 0:
            res += n % k
            n /= k
        print(res)
        return res

if __name__ == '__main__':
    Solution.sumBase(10,10)