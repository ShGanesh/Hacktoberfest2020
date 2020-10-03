def palindrome(n):
    m = n                                   
    while (n != 0):                         
        tpl = tuple(str(n))                 
        break                               
    a = int("".join(tpl[::-1]))             
                                            
    if (m == a):                            
        return "it is a palindrome number"  
    else:                                   
        return "it is not palindrome number"            
                                        

    
print palindrome(156)
