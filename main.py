import os,json
from urllib.request import Request,urlopen
U=os.environ['MAKEFUN_ENV_URL'];V={'p':100,'n':320,'b':330,'r':500,'q':900,'k':20000};N=(-21,-19,-12,-8,8,12,19,21);B=(-11,-9,9,11);R=(-10,-1,1,10);K=B+R;D={'n':N,'b':B,'r':R,'q':K,'k':K};L=50000;n=0;T={};Z=StopIteration
def P(p,x):return json.loads(urlopen(Request(U+p,json.dumps(x).encode(),{'content-type':'application/json'})).read())
def I(s):return 21+ord(s[0])-97+10*(8-int(s[1]))
def S(i):return chr(97+(i-21)%10)+str(8-(i-21)//10)
def F(f):
 z=f.split();b=list(' '*20+''.join(' '+''.join('.'*int(p)if p.isdigit()else p for p in r)+' 'for r in z[0].split('/'))+' '*20)
 return b,1 if z[1]=='w' else-1,z[2],I(z[3])if z[3]!='-' else-1
def A(b,s,c):
	for d in((9,11)if c>0 else(-9,-11)):
		if b[s+d]==('P' if c>0 else 'p'):return 1
	for d in N:
		p=b[s+d]
		if p=='N' if c>0 else p=='n':return 1
	for d in K:
		p=b[s+d]
		if p=='K' if c>0 else p=='k':return 1
		for k in range(1,8):
			t=s+d*k
			if not 0<=t<120 or b[t]==' ':break
			p=b[t]
			if p!='.':
				if p.isupper()==(c>0)and(p.lower()=='q' or d in B and p.lower()=='b' or d in R and p.lower()=='r'):return 1
				break
	return 0
def KK(b,c):return b.index('K' if c>0 else 'k')
def G(b,c,C,E,o=0):
	for i,p in enumerate(b):
		if p in '. ' or p.isupper()!=(c>0):continue
		u=p.lower()
		if u=='p':
			d=-10*c;j=i+d
			if b[j]=='.':
				if j<29 or j>90:
					for x in 'qrbn':yield i,j,x
				elif not o:
					yield i,j,''
					if(81<=i<=88 if c>0 else 31<=i<=38)and b[i+2*d]=='.':yield i,i+2*d,''
			for j in(i+d-1,i+d+1):
				if b[j]!=' ' and(b[j]!='.' and b[j].isupper()!=(c>0)or j==E):
					for x in('qrbn' if j<29 or j>90 else('',)):yield i,j,x
		else:
			for d in D[u]:
				j=i+d
				while b[j]!=' ':
					q=b[j]
					if q=='.':
						if not o:yield i,j,''
					else:
						if q.isupper()!=(c>0)and q.lower()!='k':yield i,j,''
						break
					if u in 'nk':break
					j+=d
			if u=='k' and not o and i==(95 if c>0 else 25):
				for r,d,t in(('K' if c>0 else 'k',2,(1,2)),('Q' if c>0 else 'q',-2,(-1,-2,-3))):
					if r in C and all(b[i+x]=='.' for x in t)and b[i+(3 if d>0 else-4)].lower()=='r'and not A(b,i,-c)and not any(A(b,i+x,-c)for x in t[:2]):yield i,i+d,''
def M(b,c,C,E,m):
	i,j,p=m;z=b[i];a=b.copy();a[i]='.'
	if z.lower()=='p' and j==E and i%10!=j%10:a[j+10*c]='.'
	if z.lower()=='k' and abs(j-i)==2:
		x=i+(3 if j>i else-4);y=i+(1 if j>i else-1);a[y]=a[x];a[x]='.'
	a[j]=(p.upper()if c>0 else p)if p else z
	return a,-c,C,(i+j)//2 if z.lower()=='p' and abs(i-j)==20 else-1
def H(b,c,C,E,o=0):
	for m in G(b,c,C,E,o):
		a,_,_,_=M(b,c,C,E,m)
		if not A(a,KK(a,c),-c):yield m
def EV(b):return sum((1 if p.isupper()else-1)*(V[p.lower()]+8*((6-(i-21)//10)if p.isupper()else(i-21)//10-1)*(p.lower()=='p'))for i,p in enumerate(b)if p not in'. ')
def W(m,b):
	i,j,p=m;return-(V.get(b[j].lower(),0)*10-V[b[i].lower()]+(V[p]*8 if p else 0))
def Q(b,c,C,e,a,z):
	global n
	n+=1
	if n>L:raise Z
	h=A(b,KK(b,c),-c);v=EV(b)*c
	if not h:
		if v>=z:return z
		a=max(a,v)
	ms=list(H(b,c,C,e,not h))
	if not ms:return-30000 if h else a
	ms.sort(key=lambda m:(W(m,b),m))
	for m in ms:
		x,s,C,e=M(b,c,C,e,m);v=-Q(x,s,C,e,-z,-a)
		if v>=z:return z
		a=max(a,v)
	return a
def X(b,c,C,e,d,a,z):
	global n
	n+=1
	if n>L:raise Z
	h=A(b,KK(b,c),-c)
	if d<1:return Q(b,c,C,e,a,z)
	k=(''.join(b),c,C,e);bm=T.get(k)
	ms=list(H(b,c,C,e))
	if not ms:return-30000 if h else 0
	ms.sort(key=lambda m:(m!=bm,W(m,b)));best=-31000
	for m in ms:
		x,s,cc,ee=M(b,c,C,e,m);v=-X(x,s,cc,ee,d-1,-z,-a)
		if v>best:best=v;bm=m
		if v>a:a=v
		if a>=z:break
	T[k]=bm
	return best
def Cc(f,ls):
	global n,T
	b,c,C,e=F(f);root=[(I(m[:2]),I(m[2:4]),m[4:]if len(m)>4 else '')for m in ls]
	best=root[0];T={};n=0
	for d in range(1,30):
		try:
			a=-31000
			for m in sorted(root,key=lambda m:(m!=best,W(m,b))):
				x,s,cc,ee=M(b,c,C,e,m);v=-X(x,s,cc,ee,d-1,-31000,-a)
				if v>a:a=v;best=m
		except Z:break
	return S(best[0])+S(best[1])+best[2]
while 1:
	g=P('/game',{})
	if g['status']=='done':break
	while g['status']=='your_move':g=P('/move',{'game':g['game'],'move':Cc(g['fen'],g['legal_moves'])})
