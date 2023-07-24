def main():
    m=int(input("Nhập số m: "))
    A=[]
    for i in range(m):
        res=input("Nhập dữ liệu hàng {0}:".format(i+1)).split()
        A.append([int(i) for i in res])
    print("In Mảng 2 chiều: ")
    for i in A:
        for j in i:
            print(j,end=" ")
        print()
    return
main()    
    
