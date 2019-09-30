# Байгууллагуудын нэрсийн жагсаалт өгөгдсөн бол хамгийн урт нэртэй хүнтэй байгууллагын байрлалыг ол.
ners = [['bold','baatar'], ['byamba','saraa'], ['delger','batkhangai']]
t = 0
for i in ners:
    ih = 0
    for j in i:
        if len(j)> ih: ih = len(j)
    if ih > t:
        t =ih
        k = i
print(ners.index(k))