def UnitMatrix(n):
    arr2d=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        arr2d[i][i]=1
    return arr2d
def main():
    n=int(input("Nhập số n: "))
    print("In mảng: ")
    for i in UnitMatrix(n):
        for j in i:
            print(j,end=" ")
        print()
    return
main()
