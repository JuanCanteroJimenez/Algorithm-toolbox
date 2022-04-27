#Python3


class alignment:
    def __init__(self, A, B, match, mismatch, gap):
        self.A = A
        self.B = B
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.alingscore = None
        self.start = None
        self.distancem = self.distancematrixlocal()
        
        self.up = []
        self.down = []
        self.outputali(self.start[0],self.start[1])
        
        
    def __repr__(self):
        a = "".join(self.up[::-1])
        b = "".join(self.down[::-1])

        
        return("{}\n{}\n{}".format(self.alingscore,a, b))
    def distancematrixlocal(self):
        rows = len(self.B) + 1
        colums = len(self.A) + 1
        
        D = [[ 0 for x in range(0,colums)] for x in range(0,rows)]
        
        for x in range(0,rows):
            D[x][0] = x*(-self.gap)
        """
        for x in range(0,colums):
            D[0][x] = x*(-self.gap)
        """
        
        max_ali_r = rows -1
        max_ali_c = 0 
        
        for j in range(1, colums):
            for i in range(1, rows):
                insertion = D[i-1][j] - self.gap
                deletion =  D[i][j-1] - self.gap
                match = D[i-1][j-1] + self.match
                mismatch = D[i-1][j-1] - self.mismatch
                if self.A[j-1] == self.B[i-1]:
                    D[i][j] = max(insertion, deletion, match)
                    
                else:
                    D[i][j] = max(insertion, deletion, mismatch)
                if j == colums -1  and D[i][j] > D[max_ali_r][max_ali_c]:
                    max_ali_r = i
                    max_ali_c = j

        
        self.alingscore = D[max_ali_r][max_ali_c]
        self.start = [max_ali_r,max_ali_c]

        
            
        return(D)
    def outputali(self, r, c):
        
        while r > 0 and c > 0:
            
            if  self.distancem[r][c] == self.distancem[r-1][c-1] + (self.match if self.A[c-1] == self.B[r-1] else -self.mismatch):
                self.up.append(self.A[c-1])
                self.down.append(self.B[r-1])
                c -= 1
                r -= 1
            
            elif self.distancem[r][c] == self.distancem[r][c-1] - self.gap:
                self.up.append(self.A[c-1])
                self.down.append("-")
                c -= 1
            elif self.distancem[r][c] == self.distancem[r-1][c] - self.gap:
                self.up.append("-")
                self.down.append(self.B[r-1])
                r -= 1
        while r > 0:
            self.up.append("-")
            self.down.append(self.B[r-1])
            r -= 1

        
    


def main():
    variables = [int(x) for x in input().split()]
    a = str(input())
    b = str(input())
    ali = alignment(a, b, variables[0], variables[1], variables[2])
    print(ali)

if __name__ == "__main__":
    main()