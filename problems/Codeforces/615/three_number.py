
for _ in range(int(input())):

 n=int(input());a=['YES'];i=j=2

 while j<4and i*i<n:

  if n%i<1:a+=i,;n//=i;j+=1
  i+=1
 print(*(a+[n],['NO'])[j<4])