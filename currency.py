tt=0
fh=0
th=0
oh=0
fty=0
tw=0
ten=0
five=0
two=0
one=0
amt=int(input())
while amt>=2000:
    tt+=1
    amt-=2000
while amt>=500:
    fh+=1
    amt-=500
while amt>=200:
    th+=1
    amt-=200
while amt>=100:
    oh+=1
    amt-=100
while amt>=50:
    fty+=1
    amt-=50
while amt>=20:
    tw+=1
    amt-=20
while amt>=10:
    ten+=1
    amt-=10
while amt>=5:
    five+=1
    amt-=5
while amt>=2:
    two+=1
    amt-=2
while amt>=1:
    one+=1
    amt-=1
if tt>0:
    print("2000:"+str(tt))
if fh>0:
    print("500:"+str(fh))
if th>0:
    print("200:"+str(th))
if oh>0:
    print("100:"+str(oh))
if fty>0:
    print("50:"+str(fty))
if tw>0:
    print("20:"+str(tw))
if ten>0:
    print("10:"+str(ten))
if five>0:
    print("5:"+str(five))
if two>0:
    print("2:"+str(two))
if one>0:
    print("1:"+str(one))
