def number_of_roti(arr,cooks,p,mid):
    roties = 0
    time = 0
    
    for i in range(cooks):
        time = arr[i]
        j = 2
        while(time<=mid):
            roties+=1
            time += (j*arr[i])
            j+=1
    if roties>=p:
        return True
    return False
    


T = int(input())
for t in range(T):
    p = int(input())
    arr = list(map(int,input().split()))
    no_of_cooks = arr.pop(0)
    
    lo = 0
    hi = 1e8
    ans = 0
    while lo<=hi:
        mid = (hi+lo)//2
        
        if number_of_roti(arr,no_of_cooks,p,mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    print(int(ans))
            
        
        
    
