# Нэрсийн дарааллаас хамгийн богино нэрийг олж 'Сайн уу?' гэж соль.
ner = ['Bold', 'Javhlan', 'Baatar','Saraa','Erdenebat']
urt = 15
for x in ner:
    if len(x) < urt:
        urt=len(x)
        bogino_ner = x
        bogino_ner_in = ner.index(x)
ner[bogino_ner_in]= 'Sain uu'
print(ner)
