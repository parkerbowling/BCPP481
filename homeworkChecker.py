#SHA-1 Implementation
#Parker Bowling

import sys

#Initial values for H

#H0 = 67452301
#H1 = efcdab89
#H2 = 98badcfe
#H3 = 10325476
#H4 = c3d2e1f0

def Ch(x, y, z):
    return ((x & y) ^ (~x & z))

def Parity(x, y ,z):
    return (x ^ y ^ z)

def Maj(x, y, z):
    return ((x & y) ^ (x & z) ^ (y & z)) 

def f(x,y,z,t):

    if t <=19:
        r = Ch(x,y,z)
    elif t >= 20 and t <= 39:
        r = Parity(x,y,z)
    elif t >= 40 and t <= 59:
        r = Maj(x,y,z)
    elif t >= 60 and t <= 79:
        r = Parity(x,y,z)

    return r

def padding(n,M):
    
    nBytes = bytearray(n, 'ascii')
    nBits  = [format(n, '08b') for n in nBytes]

    bitMessage = ''.join(nBits)
    #print(len(bitMessage))

    if len(bitMessage) >= 448:

        #split everything into three blocks
        if len(bitMessage) >= 960:
            paddedMessage = '1' + ('0' * ((1536 - ((8*len(n))%1536)-1-64))) + format((len(n))*8, '064b')
            
            finalMessage = bitMessage + paddedMessage

            M.append(finalMessage[:512])

            M.append(finalMessage[512:1024])
            M.append(finalMessage[1024:1536])

        #split into two blocks 
        else:
            paddedMessage = '1' + ('0' * ((1024 - ((8*len(n))%1024)-1-64))) + format((len(n))*8, '064b')
            
            finalMessage = bitMessage + paddedMessage
           
            M.append(finalMessage[:512])
           
            M.append(finalMessage[512:1024])

    #split into one block
    else:
       
        paddedMessage = '1' + ('0' * (512 - ((8*len(n))%512)-1-64)) + format((len(n))*8, '064b')

        finalMessage = bitMessage + paddedMessage
        M.append(finalMessage)    

    return M

def ROTL(x, n, w): #may not need w
    return ((x << n & (2 ** w - 1)) | (x >> w - n))

def prepMessageSchedule(M,i):
    
    W = []

    s = M[i]

    #split into W major
    for t in range(80):

        if t <=15:
            W.extend([ int(s[(32*t) : (32 * (t + 1))], 2) ])
        else:
            W.extend([ ROTL( (W[t - 3]) ^ (W[t - 8]) ^ (W[t - 14]) ^ (W[t - 16]), 1, 32) ])

    return W

def SHA1(message):
    
    K = []
    M = []

    M = padding(message,M) #this works!

    #make K
    for t in range(80):
        if t <= 19:
            K.append(0x5a827999)
        elif t >= 20 and t <= 39:
            K.append(0x6ed9eba1)
        elif t >= 40 and t <= 59:
            K.append(0x8f1bbcdc)
        elif t >= 60 and t <= 79:
            K.append(0xca62c1d6)

    H = [
        0x67452301,
        0xefcdab89, 
        0x98badcfe, 
        0x10325476, 
        0xc3d2e1f0
        ]

    N = int(len(M))

    for i in range(1,N+1):
        W = prepMessageSchedule(M,i-1)

        a = H[0]
        b = H[1]
        c = H[2]
        d = H[3]
        e = H[4]

        for j in range(80):
            T = (ROTL(a, 5, 32) + f(b, c, d, j) + e + K[j] + W[j]) % (2 ** 32)
            e = d
            d = c
            c = ROTL(b, 30, 32)
            b = a
            a = T

        H[0] = (a + H[0]) % (2 ** 32)
        H[1] = (b + H[1]) % (2 ** 32)
        H[2] = (c + H[2]) % (2 ** 32)
        H[3] = (d + H[3]) % (2 ** 32)
        H[4] = (e + H[4]) % (2 ** 32)

    H = [format((x), '08x') for x in H] 

    return("".join(H))

#print(sys.argv[1].strip())

inputString = sys.argv[1].replace("\n","")
inputString = inputString.replace(" ","")

print("\nYour input w/o spaces:", inputString, "\n")

hash = SHA1(inputString) 

print("Your hash value: ",hash)
