candidates = []
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        candidate = str(i * j)
        if candidate[::-1] == candidate:
            candidates.append(i * j)

print(candidates)
print(max(candidates))