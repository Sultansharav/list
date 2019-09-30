# Нэрсийн дарааллаас хамгийн урт нэрийг олж бүх үсгийг том болго.
ner = ['Bold', 'Javhlan', 'Baatar','Saraa','Erdenebat']
urt = 0
for x in ner:
    if len(x) > urt:
        urt=len(x)
        urt_ner = x
        tom = x.upper()
print(tom)