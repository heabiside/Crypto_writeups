from Crypto.Util.number import inverse, long_to_bytes
from extended_euclid import exEuclid

# 'e' is always two if the program ends and you got ciphertext. check Collatz Conjecture.
e = 2

'''
If we do binary search, we can get a value close to n.
If this value is x, then n=x*x-(the value you got from the program).
After that, you can get p, q because n is composed of very close primes and you can factorize it using an online calculator.
-> reference: https://www.alpertron.com.ar/ECM.HTM
'''
n = 6931725712915655493095897568511187800253984549843264668955608703245627230726522209531771269458108742462041074767244936869983422134419504064764049609517753  # n=x*x-(the value you got from the program)
p = 83256985970641859964964364565121451903472930208453599686496834423180945616483
q = 83256985970641859964964364565121451903472930208453599686496834423180945616691

# get ciphertext using command G
ct = 0x738f1c05bbc82d93a021051b9b4f53be5787faaad9997c7368a311b4e957126e2d53a414be04ceba932ebf9375c309abd5d1a5ce21066c41abbb364d914e9b4e 

d = inverse(e, (p-1)*(q-1))  # I can't find the inverse in this problem!!


# https://en.wikipedia.org/wiki/Rabin_cryptosystem  <= This is the important information!
mp = pow(ct, (p+1)//4, p)
mq = pow(ct, (q+1)//4, q)
yp,yq=[1],[1]
exEuclid(p,q,yp,yq)

yp,yq = yp[0],yq[0]

r1 = (yp*p*mq+yq*q*mp) % n
r2 = n-r1
r3 = (yp*p*mq-yq*q*mp) % n
r4 = n-r3

ans_cand=[r1,r2,r3,r4]
for ans in ans_cand:
    print(long_to_bytes(ans))