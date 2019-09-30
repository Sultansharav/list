#Тоон дарааллын элементүүдын хамгийн их элементийг ол.
too = [1,2,2,3,5,4,54,-5]
ih = too[0]
for x in too:
    if ih < x:
        ih = x
print(ih)
print(max(too))