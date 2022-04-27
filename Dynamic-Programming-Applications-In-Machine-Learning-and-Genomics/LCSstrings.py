


class alignment:
    def __init__(self, a, b, D):
        self.A = a
        self.B = b
        self.D = D
        self.up = ""
        self.down = ""
        self.lcs = ""
    def __repr__(self):
        return("{}\n{}".format(self.up, self.down))
    def outputalignment(self, i, j):
        if i == 0 and j == 0: 
            return
        if j > 0 and self.D[i][j] == self.D[i][j-1]:
                self.outputalignment(i,j-1)
                self.up = self.up + "-"
                self.down = self.down + self.B[j-1]
        else:
            if i > 0 and self.D[i][j] == self.D[i-1][j]:
                self.outputalignment(i-1, j)
                self.up = self.up + self.A[i-1]
                self.down = self.down + "-" 
            
            else:
                self.outputalignment(i-1, j-1)
                if self.A[j-1] == self.B[i-1]:
                    self.lcs = self.lcs + self.A[i-1]
                self.up = self.up + self.A[i-1]
                self.down = self.down + self.B[j-1]


def editdistance(a,b):
    rows = len(b) + 1
    colums = len(a) + 1
    D = [[ 0 for x in range(0,colums)] for x in range(0,rows)]
    """
    for x in range(0,rows):
        D[x][0] = x
    for x in range(0,colums):
        D[0][x] = x
    """
    for i in range(1, rows):
        for j in range(1, colums):
            insertion = D[i-1][j] #+ 1
            deletion =  D[i][j-1] #+ 1
            match = D[i-1][j-1] + 1
            mismatch = D[i-1][j-1] #+ 1
            if a[j-1] == b[i-1]:
                D[i][j] = max(insertion, deletion, match)
            else:
                D[i][j] = max(insertion, deletion, mismatch)
    lcs_inverse_list = []
    A = D
    r = rows - 1
    c = colums - 1
    s = a
    t = b
    while r > 0 and c > 0:
            
        if A[r][c] == A[r - 1][c - 1] + 1 and s[c - 1] == t[r - 1]:
            lcs_inverse_list.append(s[c - 1])
            c = c - 1
            r = r - 1

        elif A[r][c] == A[r - 1][c - 1]:
            c = c - 1
            r = r - 1

        elif A[r][c] == A[r][c - 1]:
            c = c - 1

        elif A[r][c] == A[r - 1][c]:
            r = r - 1
        
    return ''.join(lcs_inverse_list[::-1])
    
    
    
   
    




def main():
    a = str(input())
    b = str(input())
    d = editdistance(a, b)
    print(d)

if __name__ == "__main__":
    main()
