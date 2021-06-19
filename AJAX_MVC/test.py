
from typing import Collection

import collections


a = [(7369, 'SMITH', 800.0), (7499, 'ALLEN', 1600.0), (7521, 'WARD', 1250.0), (7566, 'JONES', 2975.0), (7654, 'MARTIN', 1250.0), (7698, 'BLAKE', 2850.0), (7782, 'CLARK', 2450.0), (7839, 'KING', 5000.0), (7844, 'TURNER', 1500.0), (7900, 'JAMES', 950.0), (7902, 'FORD', 3000.0), (7934, 'MILLER', 1300.0), (7000, 'LEE', 1500.0), (7100, 'KIM', 800.0), (7200, 'PARK', 1800.0)]

v = []
for i in a:
    b = collections.OrderedDict()
    b['no']=i[0]
    v.append(b)

print(v)

