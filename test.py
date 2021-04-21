import time
from vedic_math import case2

if __name__ == '__main__':
    f1 = open('num1.txt')
    f2 = open('num2.txt')

    n1 = [i.strip('\n') for i in f1]
    n2 = [i.strip('\n') for i in f2]

    start = time.process_time()        
    for i in n1:
        for j in n2:
            case2(i, j)
            #Uncomment this line to check the time required by regular method
            #int(i)*int(j)  
    elapsed = (time.process_time() - start)
    print(elapsed)        
