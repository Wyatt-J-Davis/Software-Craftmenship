import utils.KPrimes as KPrimes

def test_findKPrimes():
    primesList = KPrimes.findKPrimes(5, 500, 600)
    assert primesList == [500, 520, 552, 567, 588, 592, 594]

test_findKPrimes()