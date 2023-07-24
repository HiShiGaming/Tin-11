def main():
    arr=[]
    money=[]
    arr2d=[]
    ans=0
    while True:
        year=(input("NHẬP NĂM BẠN MUỐN TÍNH TIỀN ĐIỆN 12 THÁNG: "))
        if year=="":
            print("KẾT THÚC QUÁ TRÌNH NHẬP VÀ HIỆN KẾT QUẢ")
            break
        else:
            arr.append(int(year))
            for i in range(12):
                money.append(int(input("Nhập Số tiền điện tháng thứ "+str(i+1)+" năm "+str(year)+" : ")))
            arr2d.append(list(money))
            money=[]
    print("In bảng tiền điện: ")
    for i in arr2d:
        print("Năm "+str(arr[arr2d.index(i)])+":"+str(" VNĐ| ".join(list(map(str,i))))," VNĐ " )
        print()
    for i in arr:
        ave=(sum(arr2d[arr.index(i)])/len(arr2d[arr.index(i)]))
        print("Số tiền điện trung bình của năm thứ "+str(i)+" là: ",ave," VNĐ")
        ans+=ave
    print("Tổng số tiền điện trung bình của tất cả các năm là: ",ans/len(arr),"VNĐ")
main()

            
    
