import time

reservationLst = [17,21,26,29,36]
reqestedTime = [8,19,24,33,40]

def verifyRequestedTime(reservationLst, reqestedTime):
    print(reqestedTime)
    lst = reservationLst.copy()
    found = False
    if reqestedTime < lst[0]:
        print("Invalid")
    else:
        lst.insert(0,reqestedTime)
        for i in range(0,len(reservationLst)):
            j = i + 1
            swapped = False
            while j >0 and lst[j-1] > lst[j]:
                swapped = True
                lst[j-1], lst[j] = lst[j], lst[j-1]
                j -=1
            
            if swapped:
                pos = j + 1
                if pos+1 < len(lst):
                    found = lst[pos+1] - lst[pos] >= 3
                found = lst[pos] - lst[pos-1] >= 3
            else:
                break
                
            
        if not found:
            print("Invalid")
        else:
            reservationLst = lst
            print(reservationLst)

st = time.process_time()
for i in reqestedTime:
    verifyRequestedTime(reservationLst, i)
et = time.process_time()
print(et-st)