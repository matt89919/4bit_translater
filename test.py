rec={}
for i in range(0,3):
    name=input("name: ")
    score=input("score: ")
    rec[name]=score
    print(end='\n')

for i in range(0,3):
    name=input("search: ")
    print(rec.get(name,"404 not found"))
    print(end='\n')
    