def knapsack(Price,weight,W):
    
    Ratio=[]
    n=len(Price)
    for i in range(n):
        Rat=Price[i]/weight[i]
        Ratio.append((Rat,Price[i],weight[i],i))
    Ratio.sort(key=lambda x:x[0],reverse=True)    

    Profit=0
    items=[]
    for rat,pr,wt,id in Ratio:
        if(wt<=W):
            W-=wt
            Profit+=pr
            items.append((id,1))   
        else:
            frac=W/wt
            Profit+= pr * frac
            W=0
            items.append((id,frac))
            
    return items,Profit  


Price=[100,250,300,210,260,350]
weight=[10,20,25,30,40,50]
result=knapsack(Price,weight,100)
print(result)