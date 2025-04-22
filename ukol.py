#ovoce = ["jablko", "pomeranč", "jahoda"]

#dalsiOvoce = input("zadejte další ovoce: ")

#ovoce.append("malina")

#for i in ovoce:
    #print(i)

#print(len(ovoce))

příjmení = ["friedel", "havlík", "siládi", "flaks", "minařík", "hrečin"]
print(len(příjmení))
for i in příjmení:
    print(i)
dalšíPříjmení = input("Zadejte příjmení: ")
příjmení.append(dalšíPříjmení)
třetíPříjmení = input("Jaké příjmení chcete odebrat? ")
příjmení.remove(třetíPříjmení)
příjmení.sort()
print(příjmení)
příjmení.reverse()
print(příjmení)