# Тоон дарааллын хамгийн их болон багын байрыг соль.
n = [1,5,4,7,6,-1,-5,10]
ih = n.index(max(n))
baga = n.index(min(n))
n[ih],n[baga] = min(n),max(n)
print(n)