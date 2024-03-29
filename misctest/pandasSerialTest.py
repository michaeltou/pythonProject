import pandas as pd
from pandas import DataFrame
from pandas import Series

sd = {'python':200,'c++':500,'c#':9002}

myseries = Series(sd)

filter = myseries[myseries > 200]

print(filter)


doubleSeries = myseries*2

print(doubleSeries)


