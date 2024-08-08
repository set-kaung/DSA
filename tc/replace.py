import time
tesxt = input()

src = "e"
target = "i"


tesxt = list(tesxt)

st = time.process_time()
for i in range(len(tesxt)):
    if tesxt[i] == src:
        tesxt[i] = target
et = time.process_time()

print("Time taken:",et-st)
print("".join(tesxt))