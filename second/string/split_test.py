import re
str = 'a, b  , ;;  c , d'


print(re.split(r'[\s|\,\;]+',str))