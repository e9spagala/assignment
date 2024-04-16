from typing import List
even_lst: List[int] = [ i for i in range(0, 101) if i & 1 == 0 ]

for ind, val in enumerate(even_lst):
    print(f'{ind}: {val}')
