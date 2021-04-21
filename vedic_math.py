'''
Case 1 from the multiplication method.
The sutra used here is Ekadhikena Poorvena and Antyayordashakepi.
This method is used when then sum of digits from unit place is either 10,100,1000.... and so on.
The remaning digits in the number should be same.
'''

def case1(n1, n2):
    l1 = len(n1) - 1
    l2 = len(n2) - 1
    rhs = int(n1[-l1:]) * int(n2[-l2:])
    lhs = (int(n1[:-l1]) + 1) * int(n2[:-l2])
    return str(lhs) + str(rhs).rjust(l1+l2,'0')

'''
Case 2 from the multiplication method.
The sutra used here is Ekanyuena poorvena.
This method is used when either multiplier or multiplicand is 9,99,999,9999,...... and so on.
'''

def case2(n1, n2):
    l1 = len(n1)
    l2 = len(n2)
    if l1 == l2 or l1 < l2:
        lhs = int(n1) - 1
        rhs = int(n2) - lhs
        return str(lhs) + str(rhs)
    elif l1 > l2:
        lhs = int(n1) - 1
        d = str(lhs)[:-l2]
        rhs = int(n2) - int(str(lhs)[-l2:])
        return str(lhs - int(d)) + str(rhs)	
        
