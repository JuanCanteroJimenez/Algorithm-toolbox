#Python3







class hashtable:
    def __init__(self):
        self.data = [[] for x in range(0,10)]
        self.m = 10
        self.n = 0
    
    def hashnumber(self,number,m):
        a = 1
        b =  1
        
        p = 1000000007
        result = ((a*number + b)%p)%m
        return(result)
    
    def addbynumber(self, person, number):
        contact = [number,person]
        hash = self.hashnumber(number,self.m)
        if len(self.data[hash]) == 0:
            self.data[hash].append(contact)
            self.n += 1
            self.rehash()
            return()
        else:
            for x in range(0,len(self.data[hash])):
                if (self.data[hash][x][0]) == number:
                    self.data[hash][x][1] = person
                    return()
            self.data[hash].append(contact)
            self.n += 1
            self.rehash()
            return()
            
                    

    def borrar(self, number):
        c = self.data[self.hashnumber(number,self.m)]
        for x in range(0,len(c)):
            if c[x][0] == number:
                c.pop(x)
                self.n -= 1
                self.rehash()
                break
        
    def find(self, number):
        c = self.data[self.hashnumber(number,self.m)]
        for x in range(0,len(c)):
            if c[x][0] == number:
                return(c[x][1])
        return("not found")
    
    def rehash(self):
        loadfactor = self.n/self.m
        if loadfactor > 0.9:
            new = hashtable()
            new.data = [[] for x in range(0,round(self.m*2))]
            new.m = round(self.m*2)
            for x in range(0,len(self.data)):
                if len(self.data[x]) != 0:
                    for y in range(0,len(self.data[x])):
                        new.addbynumber(self.data[x][y][1],self.data[x][y][0])
            self.data = new.data
            self.m = new.m



agendita = hashtable()
n = int(input())
resultados = []
for x in range(0,n):
    j = [i for i in input().split()]
    if len(j) == 2:
        j[0] , j[1] = str(j[0]) , int(j[1])
    elif len(j) == 3:
        j[0] , j[1] , j[2] = str(j[0]) , int(j[1]), str(j[2])
    if j[0] == "find":
        resultados.append(agendita.find(j[1]))
    if j[0] == "add":
        agendita.addbynumber(j[2], j[1])
    if j[0] == "del":
        agendita.borrar(j[1])
for x in range(0,len(resultados)):
    print(resultados[x])
