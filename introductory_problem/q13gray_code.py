def graycode(n):
    
     
    if n == 1:
        return ["0", "1"]
  
    
    prevGrayCode = graycode(n - 1)
      
    
    reversedPrevGrayCode = prevGrayCode[::-1]
  
    prevSize = len(prevGrayCode)
    index = 0
    while index < prevSize:
        
      
        appendedZero = "0" + prevGrayCode[index]
   
       
        prevGrayCode[index] = "1" + reversedPrevGrayCode[index]
        prevGrayCode.append(appendedZero)
        index += 1
    
    return prevGrayCode

if __name__ == "__main__":
    n = 3
    res = graycode(n)
    for code in res:
        print(code)