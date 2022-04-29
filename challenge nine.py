def func(x):    
    count=0
    a=x
    r=0
    while a!=0:
        r=r+ a%10
        count = count + 1
        a=a//10
    q=r-9
    if q<0:
        q= -q
    if q>9:
        while q>9:
            q=q-9
    m= x*10 +q
    n= q*(10**count)+x
    if m<n:
        result=m
    elif n<m:
        result= n
    else:
        result =m
    
    return result

no_of_inputs= int(input())
inputs= []
while no_of_inputs>0:
    value= int(input())
    inputs.append(value)
    no_of_inputs=no_of_inputs-1
for i in inputs:
    ans=func(i)
    print(ans)