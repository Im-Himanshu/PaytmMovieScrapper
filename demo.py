n = 5;
prev1 = 0;
prev2 =1;
print(prev1)
print(prev2)
for i in range(1,n-1) :
    mid = prev1+prev2;
    prev1 = prev2
    prev2 = mid
    print(prev2)








