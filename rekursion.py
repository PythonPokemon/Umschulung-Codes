
def fakultät(n):
    if n < 1:
        return 1
    return fakultät(n-1) * n

print(fakultät)