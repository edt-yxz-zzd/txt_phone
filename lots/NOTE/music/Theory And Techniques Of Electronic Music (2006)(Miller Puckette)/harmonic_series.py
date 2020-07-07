
'''
harmonic series
    harmonics w n = n*w  -- Fourier linear v.s. human exp
    harmonic_series = 0, 1200, 1902, 2400, 2786, 3102, 3369, 3600, ...
    w[i] = w0 * (2^(harmonic_series[i]/1200)) = w0*(i+1)
    ==>> harmonic_series i = log2 (i+1) * 1200
'''
from math import log2

def harmonic_series(i):
    return log2(i+1)*1200

def harmonic_series_to(n):
    return list(map(harmonic_series, range(n)))

print(harmonic_series_to(10))
[0.0, 1200.0, 1901.9550008653873, 2400.0, 2786.3137138648344, 3101.9550008653873, 3368.825906469125, 3600.0, 3803.9100017307746, 3986.3137138648344]

