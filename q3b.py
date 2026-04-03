def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a1 = a[2::]
    b1 = b[2::]
    
    
    def binsum(string):
        suma = 0
        for i in range(len(string)):
           if string[i]=='1':
               suma += 2**(len(string)-1-i)
        return suma
    
    c = binsum(a1) + binsum(b1)
    

    
    def maxg(gle):
        a = 0
        while gle>=2**(a):
            a+=1
        return a-1
    
    
    res = ''
    for i in range(maxg(c),-1,-1):
        if c>= 2**(i):
            res+= '1'
            c-=2**(i)
            
        else:
            res +='0'
            
            
    return '0b' +res
        
        
            
    
            
            

            
        
            
        