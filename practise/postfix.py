class stack:
    def __init__(self,arr) -> None:
        self.arr:list[str] = arr
    
    def pop(self)->str:
            res = self.arr[len(self.arr)-1]
            self.arr = self.arr[:len(self.arr)-1]
            return res
        
    def push(self,element):
        self.arr.append(element)

    def __str__(self) -> str:
        s = ""
        for e in self.arr:
            s += f"{e} "
        return s
    def len(self):
        return len(self.arr)

s = []
inx = input().split()
for i in inx:
    if i.isdigit():
        s.append(int(i))
    else:
        if len(s) >= 2:
            a = s.pop()
            b = s.pop()
            if i == "+":
                x = float(a) + float(b)
                s.append(x)
            elif i == "-":
                x = float(b) - float(a)
                s.append(x)
            elif i == "*":
                x = float(a) * float(b)
                s.append(x)
            elif i == "/":
                 x = float(b) / float(a)
                 s.append(x)
            elif i == "%":
                x = float(b) % float(a)
                s.append(x)
            elif i == "^":
                x = float(b) ** float(a)
                s.append(x)

print(s[0])






