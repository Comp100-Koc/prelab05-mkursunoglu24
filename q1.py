def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    if len(s) ==1 or len(s) == 0:
        return ''
    
    tup1 = ()
    
    for i in range(len(s)):
        
        low = i-1
        hi = i+1
        res = ''
        while low >= 0  and hi <= (len(s)-1) and s[low] == s[hi]:
            res = s[low:hi+1]
            low -= 1
            hi += 1
            
            
        if len(res) >2:
            tup1 += ((res,i),)
            
     


    for i in range(len(s)):
         left = i
         right = i+1
         
         res = ''
         
         while left >= 0  and right <= (len(s)-1) and s[left] == s[right]:
             res = s[left:right+1]
             left -=1
             right +=1
             
             
         if len(res) >=2:
             tup1 += ((res,left),)
             
        
         
             
             
             
    max1 = ''
    for i in tup1:
        if len(i[0]) > len(max1):
            max1 = i[0]
            
    return max1
            
        
            
    
        
        
            
             
        