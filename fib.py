# Author: Kai Geller
# GitHub Username: KaiGeller
# Date: 4/20/2022
# To give the value of the fibonacci sequence
term = int(input("fib:"))
previous=1
prev_prev=1
for i in range(3,term+1):
    current= previous+prev_prev
    if i == term:
        print((current))
        break
    prev_prev=previous
    previous=current