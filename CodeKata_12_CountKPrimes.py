import utils.KPrimes as KPrimes

def test_findKPrimes():
    kPrimeFinder = KPrimes.KPrimeFactorFinder()
    primesList = kPrimeFinder.findKPrimes(5, 500, 600)
    print(primesList)
    assert primesList == [500, 520, 552, 567, 588, 592, 594]

def test_findMoreKPrimes():
    kPrimeFinder = KPrimes.KPrimeFactorFinder()
    primesList = kPrimeFinder.findKPrimes(2, 14, 18)
    print(primesList)
    assert primesList == [14, 15]


if __name__ == "__main__":
    test_findKPrimes()
    test_findMoreKPrimes()