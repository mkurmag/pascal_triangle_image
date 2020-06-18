import functools
import image

@functools.lru_cache(maxsize=None)
def choose(n, k):
    if k in (0, n):
        return 1
    return choose(n-1, k-1) + choose(n-1, k)

res = []
for row in range(20):
    for k in range(row + 1):
        res.append(choose(row, k))

image.draw(res)
