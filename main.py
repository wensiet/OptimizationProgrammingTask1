from algorithm import Simplex


def main():
    """
    C = (2 -1 3)
    A = (1 -2 1
         3 1 2
         2 2 2)
    b = (4 3 5)
    e = 1e-6
    """

    lpp_type = input("Enter the type of the problem(min/max): ")
    rows = int(input("Enter number of constraints: "))
    columns = int(input("Enter number of x's: "))
    c = []
    print("Enter vector of coefficients of objective function (C): ")
    for i in range(columns):
        c.append(int(input()))
    a = []
    print("Enter matrix of coefficients of constraint function (A): ")
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(int(input()))
        a.append(temp)
    print("Enter vector of right-hand side numbers (B): ")
    b = []
    for i in range(rows):
        b.append(int(input()))
    print("Enter the approximation (e): ")
    e = float(input())
    s = Simplex(c, a, b, lpp_type, e=e)

    s.solve()


if __name__ == "__main__":
    main()
