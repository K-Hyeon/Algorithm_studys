
import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    word = str(input().strip())

    
    word_back = word[::-1]


    if word == word_back:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")
