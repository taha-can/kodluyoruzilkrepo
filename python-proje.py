

//Soru 1


def flatten(n):
    n = list(n)
    xp = list()
    for x in n:
        if type(x) is int or type(x) is str:
            xp.append(x)
            
            
        elif type(x) is list:
            for i in x:
                if type(i) is int or type(i) is str:
                    xp.append(i)
                    
                elif type(i) is list:
                    for k in i:
                        if type(k) is int or type(k) is str:
                            xp.append(k)
                        elif type(k) is list:
                            for p in k:
                                if type(p) is int or type(p) is str:
                                    xp.append(p)
                                    
                                    
    print(xp)
                        
flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
    
    
    
    
//Soru 2

def reverse(n):
    print(n)
    n = list(n)
    n.reverse()
    for x in n:
        if type(x) is list:
            x.reverse()
        else:
            pass
        
    print(n)