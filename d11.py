# Тоон дарааллаас хамгийн бага элементийг устга.
n = [1,2,1,21,215,251,251,2513,5555]
baga = min(n)
for i in range(len(n)):
    if baga == n[i]:
        n.remove(baga)
print(n)

# baga = n.index(min(n))
# del n[baga]
# print(n)