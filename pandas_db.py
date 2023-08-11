import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
institutes =[ "Nareshit","Satech","Gana Tech.","Pee Tech.","Dreams Solu."]
values =[3803,638,150,374,296]
explode = [0.05,0,0,0,0] #explode 1st i.e slice is separated by 0.05 distance
colors =["c","b","g","r","y"]
plt.pie(values, labels=institutes, explode=explode, colors=colors, autopct="%0.1f%%")
plt.show()
