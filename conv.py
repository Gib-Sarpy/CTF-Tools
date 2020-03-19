import binascii
import re

def toDigits(n, b):
    """Convert a positive number n to its digit representation in base b."""
    digits = []
    str1 = ""
    x=0
    #print "n:"+str(n)+" b:"+str(b)
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    str1 = ''.join(str(e) for e in digits)
    print str1
    x = len(str1) % 8
    print x, len(str1)
    if x != 0:  
        x = 8 - x
        str1 = "0"*x + str1
    str1 = '0b' + str1
    print str1
    return int(str1, 2)

def fromDigits(digits, b):
    """Compute the number given by digits in base b."""
    print digits
    n = 0
    for d in digits:
        n = b * n + d
    return n

def convertBase(digits, b, c):
    """Convert the digits representation of a number from base b to base c."""
    return toDigits(fromDigits(digits, b), c)

def main():
    cnt=0
    base = int(raw_input("Base: "))
    fn = raw_input("in E:/puz/ path\nFilename: ")
    filename = "E:/puz/" + fn

    #trim that shiz up
    oldfile = open(filename, "r")
    data = oldfile.read()
    oldfile.close()
    nfname = filename+".bak"
    newfile = open(nfname,"w")
    newfile.write(data)
    sdata = data.lstrip()
    rdata = "".join(sdata.split())
    stripped_data = rdata.strip()
    newfile = open(filename,"w")
    newfile.write(stripped_data)
    newfile.close()

    dig = []
    if int(base) == 2:
        lcm=int(base)*4
    elif 8 % int(base) != 0 and 8 % int(base) != 8:
        lcm=int(base)*2
    else:
        lcm = int(base)
    message = ""
    with open(filename) as f:
        while True:
            c = f.read(1)
            #for l in f:
            if not c:
                print "End of file"
                break
            elif cnt >= lcm:
                print "[CONHIT]cnt:" +str(cnt) + " lcm:" + str(lcm) + " diglen:" + str(len(dig))
                n = convertBase(dig,base,2)
                dig = []
                dig.append(int(c))
                if n != 10:
                    message += binascii.unhexlify('%x' % n)
                    print message
                else:
                    message += "\n"
                cnt = 1
            else:
                #print "cnt:" +str(cnt) + " lcm:" + str(lcm) + " diglen:" + str(len(dig))
                dig.append(int(c))
                cnt += 1

    print message
            

  
if __name__== "__main__":
  main()