#prblm: To find LCM And GCD (GFG)                        !Important
    #Solution: 1 --> Normal Approach
def lcmAndGcd(a : int, b : int):
    def lcm(a,b):                   #--> LCM
        lcm = 1
        x = 2
        while a != 1 or b != 1:
            if a%x == 0 and b%x == 0:
                a /= x
                b /= x
                lcm *= x
            else:
                if a%x == 0:
                    a /= x
                    lcm *= x
                if b%x == 0:
                    b /= x
                    lcm *= x
            if a%x != 0 and b%x != 0:
                x += 1
        return lcm
    def gcd(a,b):                   #--> GCD
        gcd = 1
        x = 2
        while a != 1 or b != 1:
            if a%x == 0 and b%x == 0:
                a /= x
                b /= x
                gcd *= x
            else:
                if a%x == 0:
                    a /= x
                if b%x == 0:
                    b /= x
            if a%x != 0 and b%x != 0:
                x += 1
        return gcd
    lst = [lcm(a,b),gcd(a,b)]
    return lst
    #Time Complexity: O(min(a,b))      --> Run Time: 0.12Sec
    #Space Complexity:O(1)
#print(lcmAndGcd(18,25))
    #Solution_2: Optimized Solution    --> Ecuclidean Algorithm
def LCM_and_Gcd(a,b):
    def gcd(a,b):
        while b!=0:
            temp = a
            a = b
            b = temp%b
        return a
    gcd = gcd(a,b)
    def lcm(a,b,gcd):
        lcm = (a*b)//gcd
        return lcm
    lcm = lcm(a,b,gcd)
    return [lcm,gcd]
    #Time Complexity: O(log(min(a,b)))      --> Run Time: 0.05Sec
    #Space Complexity:O(1)
#print(LCM_and_Gcd(5,10))