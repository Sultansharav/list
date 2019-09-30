# Олимпиадын дүн бүхий оноонуудын жагсаалт өгөгдсөн бол хэд дэх хүн түрүүлсэн бэ.
n = [int(i) for i in input().split()]
ih = max(n)
for i in range(len(n)):
    if ih == n[i]:
        print(i, end=' ')

# print(n.index(max(n)))