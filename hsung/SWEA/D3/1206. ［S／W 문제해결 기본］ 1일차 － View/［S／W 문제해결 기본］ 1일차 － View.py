"""
4<= N <= 1000
0<= height <= 255
맨 왼 쪽 두칸과  맨 오른 쪽 두칸은 항상 빈칸이다. 

0이 아닌 건물 왼쪽 2개 오른쪽 2개 뽑아서 
"""

for i in range(10):
    building_num = int(input())    
    buildings = list(map(int, input().split()))
    count = 0
    
    for building in range(2, building_num - 2):
        if ((buildings[building] > buildings[building -1]) 
            and (buildings[building] > buildings[building -2]) 
            and (buildings[building] > buildings[building +1])
            and (buildings[building] > buildings[building +2])):
            count += (buildings[building]-max([buildings[building-2],buildings[building-1],
                                               buildings[building+1],buildings[building+2] ]))
    print(f"#{i + 1} {count}")