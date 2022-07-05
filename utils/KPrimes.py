import multiprocessing

class KPrimeFactorFinder(object):
    def __init__(self):
        self._primeFactorList = []
        self._k = 0 
    
    def findKPrimes(self, k, start, end):
        self._k = k
        data = range(start, end, 1)
        with multiprocessing.Pool() as pool:
            pool.map(self._primeFactors, data)
        return self._primeFactorList
        
    
    def _primeFactors(self,n):
        i = 2
        factors = []
        while i*i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        if(self._k == len(factors)):
            self._primeFactorList.append(n)
    

    
"""     def findKPrimes(self, k, start, end):
        kPrimes = []
        for i in range(start, end, 1):
            primeFactors = self._prime_factors(i)
            if(len(primeFactors) == k):
                kPrimes.append(i)
        return kPrimes """

    