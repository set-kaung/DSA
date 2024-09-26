# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

user_input = input()

numbers = []

user_input = user_input.strip()

for i in user_input.split(" "):
    numbers.append(int(i))


evens = []
odds = []

for j in numbers:
    if j % 2 == 0:
        evens.append(j)
    else:
        odds.append(j)

for i in odds:
    print(i,end=" ")
print()

large_even = evens[0]

for e in evens:
    if e > large_even:
        large_even = e

print(large_even)



last = len(evens) - 1

while last >= 0:
    print(f"{evens[last]}",end=" ") 
    last -= 1
print()

    




