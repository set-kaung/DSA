# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

def parking(cars, k):

    if cars == sorted(cars, reverse=True):
        return 0
    
    holding_tracks = []

    for car in cars:
        placed = False
    
        for track in holding_tracks:
            if track[-1] < car:
                track.append(car)
                placed = True
                break

        if not placed:
            if len(holding_tracks) < k:
                holding_tracks.append([car])
            else:
                return "No Solution"

    return len(holding_tracks)

cars = list(map(int, input().split()))
k = int(input())

result = parking(cars, k)
print(result)
