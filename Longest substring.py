s='azcbobobeggha' 
c=0
cmax=0
num=0
for x in range(len(s)-1):
    
    if s[x]<=s[x+1]:
        c+=1
        if c>cmax:
            cmax=c
            num=x+1
    else:
        c=0
print('Longest substring in alphabetical order is: ' + s[(num-cmax):(num+1)])

        
        

