import utils.KPrimes as KPrimes

def test_findKPrimes():
    kPrimeFinder = KPrimes.KPrimeFactorFinder()
    primesList = kPrimeFinder.findKPrimes(5, 500, 600)
    assert primesList == [500, 520, 552, 567, 588, 592, 594]

test_findKPrimes()