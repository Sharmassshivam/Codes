class Matrix:
    def __init__(self):
        self.matrix = []
        self.row = 0
        self.col = 0

    def get_mat(self):
        self.row = int(input("Enter no of rows in matrix :"))
        self.col = int(input("Enter no of columns in matrix :"))
        self.matrix = [[int(input("enter element")) for i in range(self.col)] for j in range(self.row)]

    def set_mat(self, row, col):
        self.row = row
        self.col = col

    def show(self):
        for i in range(self.row):
            print("[ ", end=" ")
            for j in range(self.col):
                print( self.matrix[i][j], end=" ")
            print("]")

    def add_mat(self, mat):
        add = Matrix()
        add.set_mat(self.row, self.col)
        add.matrix = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                add.matrix[i][j] = self.matrix[i][j] + mat.matrix[i][j]
        add.show()

    def sub_mat(self, mat):
        sub = Matrix()
        sub.set_mat(self.row, self.col)
        sub.matrix = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                sub.matrix[i][j] = self.matrix[i][j] - mat.matrix[i][j]
        sub.show()

    def mul_mat(self, mat):
        mul = Matrix()
        mul.set_mat(self.row, mat.col)
        mul.matrix = [[0 for i in range(mat.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(mat.col):
                for k in range(self.col):
                    mul.matrix[i][j] = mul.matrix[i][j] + self.matrix[i][k] * mat.matrix[k][j]
        mul.show()

    def transpose_mat(self):
        trans = Matrix()
        trans.matrix = [[0 for i in range(self.row)] for j in range(self.col)]
        trans.set_mat(self.col, self.row)
        for i in range(self.col):
            for j in range(self.row):
                trans.matrix[i][j] = self.matrix[j][i]
        trans.show()


m1 = Matrix()
m2 = Matrix()
m3 = Matrix()
print("1.Enter elements in matrices\n2.Addition of matrices\n3.Subtraction of matrices\n4.Multiplication of "
      "matrices\n5.Transpose of matrix")
while True:
    print()
    c = int(input("Enter your choice"))
    if c == 1:
        print("For first matrix")
        m1.get_mat()
        print("For second matrix")
        m2.get_mat()
        print("First matrix")
        m1.show()
        print("Second matrix")
        m2.show()
    elif c == 2:
        if m1.row == m2.row and m1.col == m2.col:
            print("Addition of matrices is")
            m1.add_mat(m2)
        else:
            print("Operation can't perform as matrix are not similar. Enter new matrices")
    elif c == 3:
        if m1.row == m2.row and m1.col == m2.col:
            print("Subtraction of matrices is")
            m1.sub_mat(m2)
        else:
            print("Operation can't perform as matrix are not similar. Enter new matrices")
    elif c == 4:
        if m1.col == m2.row:
            print("Multiplication of matrices is")
            m1.mul_mat(m2)
        else:
            print("Operation can't perform as no of column are not equal to no of row. Enter new matrices")
    elif c == 5:
        print("for check transpose of matrix")
        m3.get_mat()
        print("Entered matrix")
        m3.show()
        print("Transpose of matrix is")
        m3.transpose_mat()

    else:
        print("Quiting program")
        break
