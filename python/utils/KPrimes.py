from utils.concurrency import ConcurrentClassifier

class KPrimeFactorFinder(object):
    def __init__(self):
        self._primeFactorList = [] 
        self._k = 0
        self._Classifier = ConcurrentClassifier()
    
    def findKPrimes(self, k, start, end, threads = 5):
        self._k = k
        kPrimeRange = range(start, end + 1, 1)
        return self._Classifier.determineTrue(self._primeFactors, kPrimeRange, threads)
    
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