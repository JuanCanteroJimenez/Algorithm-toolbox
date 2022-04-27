#Python3

import collections


class packet:
    def __init__(self, Tll, Tp):
        self.llegada = Tll
        self.procesado = Tp
    def __str__(self):
        return("Tiempo de llegada {}, Tiempo de procesamiento {}".format(self.llegada, self.procesado))


class buffer:
    def __init__(self, capacity):
        self.data = collections.deque()
        self.capacidad = capacity
    def __str__(self):
        return("Capacidad {}, Contenido {}".format(self.capacidad,self.data))

    def add(self, paquete):
        if len(self.data) < self.capacidad:
            self.data.appendleft(paquete)
            return(1)
        else:
            return(0)
    def pop(self):
        if len(self.data) != 0:
            ret = self.data.pop()
            return(ret)   
        





def packetmanager(paquetes,buffercapacity):
    tiempoejecutado = []
    tampon = buffer(buffercapacity)
    timeline = 0
    trabajando = 0
    while len(paquetes) != len(tiempoejecutado):
        if trabajando == 0:
            pass
        else:
            trabajando -= 1
            if trabajando == 0:
                tampon.pop()
        
        for x in range(0, len(paquetes)):
            
            if len(tampon.data) != 0 and trabajando == 0:
                #if tampon.data[0].llegada == timeline:
                pa = tampon.pop()
                trabajando = pa.procesado
                tiempoejecutado.append(timeline)
            if paquetes[x].llegada == timeline and trabajando == 0:
                trabajando = paquetes[x].procesado
                tiempoejecutado.append(timeline)
                if paquetes[x].procesado == 0:
                    pass
                else:
                    tampon.add(paquetes[x])
            elif paquetes[x].llegada == timeline and trabajando != 0:
                exito = tampon.add(paquetes[x])
                if exito == 1:
                    pass
                else:
                    tiempoejecutado.append(-1)
            
        timeline += 1
        
        
        
        
    return(tiempoejecutado)



n = [int(x) for x in input().split()]
listapaquetes = []
for x in range(0,n[1]):
    inpu = [int(z) for z in input().split()]
    listapaquetes.append(packet(inpu[0],inpu[1]))

j = packetmanager(listapaquetes, n[0])

for x in j:
    print(x)







       



