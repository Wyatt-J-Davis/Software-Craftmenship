import multiprocessing

class KPrimeFactorFinder(object):
    def __init__(self):
        self._primeFactorList = [] 
        self._k = 0
    
    def findKPrimes(self, k, start, end):
        self._k = k
        kPrimeRange = range(start, end, 1)
        isKPrime = []
        with multiprocessing.Pool(5) as pool:
            isKPrime = list(pool.map(self._primeFactors, kPrimeRange))
        for count, value in enumerate(isKPrime):
            if(True == value):
                self._primeFactorList.append(kPrimeRange[count])
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
            return True
        else:
            return False    