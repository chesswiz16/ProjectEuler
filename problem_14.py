__author__ = 'Tiger'

chains = {}
max_i = 0
max_chain = 0
for i in range(800000, 850000):
    end = i
    chain = 1
    while end != 1:
        if end % 2 == 0:
            end /= 2
        else:
            end = 3 * end + 1
        end = int(end)
        if end in chains:
            chain += chains[end]
            end = 1
        else:
            chain += 1
    chains[i] = chain
    # print(i, " ", " ", chain, " ", max_chain)
    if chain > max_chain:
        max_i = i
        max_chain = chain

print(max_chain)
print(max_i)

# import time
#
# start = time.time()
#
# limit = 1000000
# collatz_length = [0] * limit
# collatz_length[1] = 1
# max_length = [1, 1]
#
# for i in range(1, 1000000):
# n, s = i, 0
#     TO_ADD = []  # collatz_length not yet known
#     while n > limit - 1 or collatz_length[n] < 1:
#         TO_ADD.append(n)
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             n = 3 * n + 1
#         n = int(n)
#         s += 1
#     # collatz_length now known from previous calculations
#     p = collatz_length[n]
#     for j in range(s):
#         m = TO_ADD[j]
#         if m < limit:
#             new_length = collatz_length[n] + s - j
#             collatz_length[m] = new_length
#             if new_length > max_length[1]: max_length = [i, new_length]
#
# elapsed = (time.time() - start)
# print("found %s at length %s in %s seconds" % (max_length[0], max_length[1], elapsed))