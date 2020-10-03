#reverse each word
#find the error and correct it
st=input()
l=[] #Error: {}
p=""
for i in range(len(st)):
    if st[i]==' ':
        l.append(p)
        p=""
    else:
        p+=st[i]
    
l.append(p)
        
for i in l:
    print(i[::-1],end=" ")

'''
Test input: Garaj Garaj Aaye Kaare Bhadra
Output:     jaraG jaraG eyaA eraaK ardahB 
Each word is being reversed.
'''
