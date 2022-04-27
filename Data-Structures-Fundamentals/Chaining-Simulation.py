#Python3

class hashtable:
    def __init__(self,spacesinit):
        if spacesinit == 0:
            self.data = [[]]
            self.m = 1
        else:
            self.data = [[] for x in range(0,spacesinit)]
            self.m = spacesinit
        self.n = 0
    
    def hashstring(self,string):
        unicode = [ord(x) for x in string]
        hash = 0
        x = 263
        p = 1000000007
        m = self.m
        for i in range(len(unicode)-1,-1,-1):
            hash = (hash * x + unicode[i]) % p
        
        return(hash%m)

    def addbystring(self, person):
        contact = person
        hash = self.hashstring(person)
        if len(self.data[hash]) == 0:
            self.data[hash].insert(0,contact)
            self.n += 1
            #self.rehash()
            return()
        else:
            for x in range(0,len(self.data[hash])):
                if (self.data[hash][x]) == person:
                    
                    return()
            self.data[hash].insert(0,contact)
            self.n += 1
            #self.rehash()
            return()
    def addbystring1(self, person):
        contact = person
        hash = self.hashstring(person)
        if len(self.data[hash]) == 0:
            self.data[hash].append(contact)
            self.n += 1
            #self.rehash()
            return()
        else:
            for x in range(0,len(self.data[hash])):
                if (self.data[hash][x]) == person:
                    
                    return()
            self.data[hash].append(contact)
            self.n += 1
            #self.rehash()
            return()
    def borrar(self, person):
        c = self.data[self.hashstring(person)]
        for x in range(0,len(c)):
            if c[x] == person:
                self.data[self.hashstring(person)].pop(x)
               
                #self.rehash()
                break
        
    def find(self, person):
        c = self.data[self.hashstring(person)]
        for x in range(0,len(c)):
            if c[x] == person:
                return("yes")
        return("no")
    def check(self,i):
        return(self.data[i])
    def rehash(self):
        loadfactor = self.n/self.m
        if loadfactor > 0.9:
            new = hashtable(self.m*2)
            
            
            for x in range(0,len(self.data)):
                if len(self.data[x]) != 0:
                    for y in range(0,len(self.data[x])):
                        new.addbystring1(self.data[x][y])
            self.data = new.data
            self.m = new.m



n = int(input())
agendita = hashtable(n)
orders = int(input())
resultados = []
for x in range(0,orders):
    j = [i for i in input().split()]
    if j == 0:
        break
    j[0] = str(j[0])
    if j[0] == "check":
        j[1] = int(j[1])
    else: 
        j[1] = str(j[1])
    if j[0] == "find":
        resultados.append(agendita.find(j[1]))
    elif j[0] == "add":
        agendita.addbystring(j[1])
    elif j[0] == "del":
        agendita.borrar(j[1])
    elif j[0] == "check":
        resultados.append(list(agendita.check(j[1])))
    elif j[0] == "0":
        break 


for x in range(0,len(resultados)):
    if type(resultados[x]) == str:
        print(resultados[x])
    else:
        print(*resultados[x])


    
    
