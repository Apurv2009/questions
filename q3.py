cock1 = 0
cock2 = 100
time = 0

# let them move
while cock1 < cock2:
    time += 1
    
    if time % 10 == 0:
        cock1 -= 2
    else:
        cock1 += 1
        
    if time % 5 == 0:
        cock2 += 1
    else:
        cock2 -= 2
# stop them when they cross

print("Coackroach meet at:", time)
print(cock1, cock2)

time1 = time 
time2 = time 

# move first cockraoch
while cock1 < 100:
    time1 += 1
    if time1 % 10 == 0:
        cock1 -= 2
    else:
        cock1 += 1

# move second cockraoch
while cock2 > 0:
    time2 += 1
    if time2 % 5 == 0:
        cock2 += 1
    else:
        cock2 -= 2
        
print("Cockroach 1 completes the rod at: ", time1)
print("Cockroach 2 completes the rod at: ", time2)
