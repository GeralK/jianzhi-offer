# -*- coding:utf-8 -*-
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n > 1:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
if __name__=="__main__":
    Test = Solution()
    print(Test.Fibonacci(3))