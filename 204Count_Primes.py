"""
Description
Count the number of prime numbers less than a non-negative number, n.
西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，这方法被称作厄拉多塞筛法(Sieve of Eeatosthese)。
具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数.
其实，当你要画圈的素数的平方大于 n 时，那么后面没有划去的数都是素数，就不用继续判了

"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return False
        isPrimes = [True] * n
        
        isPrimes[0] = isPrimes[1]  = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrimes[i]:
                isPrimes[i*i:n:i] = [False] * len(isPrimes[i*i:n:i])
        return isPrimes.count(True)#sum(isPrimes)
        
    def countPrimes2(self, n):
        
        isPrimes = [True] * max(n, 2)
        
        isPrimes[0] = isPrimes[1] = False
        
        x = 2
        while x * x < n:
            if isPrimes[x]:
                p = x * x
                while p < n:
                    isPrimes[p] = False
                    p += x
            x += 1
        return sum(isPrimes)
    
    def countPrimes3(self, n):
        if n < 3:
            return 0
        count = 0
        def isDivisible(n):
            return lambda x: x % n > 0
        def oddIter():
            m = 1
            while True:
                m += 2
                yield m
        def primes():
            yield 2
            it = oddIter()
            while 1:
                n = next(it)
                yield n
                it = filter(isDivisible(n), it)
        for num in primes():
            if num < n:
                count += 1
            else:
                break
        return count