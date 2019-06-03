from Crypto.Hash import HMAC 
secret=b'SowrdFish'
h=HMAC.new(secret)
h_first=h.digest()
print(h.digest())

h1=HMAC.new(secret)
h_second=h1.digest()
print(h_second)

if(h_second==h_first):
    print("They are same")
else:
    print("They are not same")