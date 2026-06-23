a = {10: 28, 20: 65, 30: 97}
b = {30: 43, 40: 76, 50: 87}

common_sums = {}
for key in b:
    if key in a:
        common_sums[key] = a[key] + b[key]

print(common_sums)
    