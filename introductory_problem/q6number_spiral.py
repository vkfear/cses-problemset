def number_spiral(Y, X):

    if Y > X:
        
        ans = (Y - 1) * (Y - 1)
        
        if Y % 2 != 0:
            add = X
        else:
          
            add = 2 * Y - X
      
        print(ans + add)
   
    else:
      
        ans = (X - 1) * (X - 1)
     
        if X % 2 == 0:
          
            add = Y
        else:
         
            add = 2 * X - Y
      
        print(ans + add)

Y = 4
X = 3
number_spiral(Y, X)