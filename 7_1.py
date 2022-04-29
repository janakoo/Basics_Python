class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        for row in self.list_1:
            for i in row:
                print(f"{i: 5}", end="")
            print()
        return ''

    def __add__(self, other):
        if len(self.list_1) != len(other.list_1) or len(self.list_1[0]) != len(other.list_1[0]):
            return "матрицы разных размерностей"


        for i in range(len(self.list_1)):
            for j in range(len(other.list_1[i])):
                self.list_1[i][j] = self.list_1[i][j] + other.list_1[i][j]
        return Matrix.__str__(self)


my_matrix = Matrix([[5, 18, 2],
                    [6, 17, 2]])

my_matrix2 = Matrix([[45, 8],
                     [6, 71]])

print(my_matrix.__add__(my_matrix2))