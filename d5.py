ner = ['Bold', 'Javhlan', 'Baatar','Saraa','Erdenebat']
urt = 15
for x in ner:
    if len(x) < urt:
        urt=len(x)
        bogino_ner = x

print(bogino_ner)
