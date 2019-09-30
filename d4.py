ner = ['Bold', 'Javhlan', 'Baatar','Saraa','Erdenebat']
urt = 0
for x in ner:
    if len(x) > urt:
        urt=len(x)
        urt_ner = x

print(urt_ner)
