class KPrimeFactorFinder(object):
    
    def findKPrimes(self, k, start, end):
        kPrimes = []
        for i in range(start, end, 1):
            primeFactors = self._prime_factors(i)
            if(len(primeFactors) == k):
                kPrimes.append(i)
        return kPrimes
    
    def _prime_factors(self,n):
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
        return factors