def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    a = 0
    res = ''
    if s[0] != s[1]:
        res+= s[0]
    a+=1
    while a<= len(s)-1 :
        if s[a+1] != s[a] and s[a-1] != s[a]:
            res+= s[a]
            a+=1
        
        else:
            a+=1
            
    return res
            