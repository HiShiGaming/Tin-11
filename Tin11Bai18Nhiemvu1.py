def logic(quanly,n):
    if n>len(quanly) or n<1:
        return True
    else:
        return print("Đầu điểm thứ ",n," là: ",quanly[n-1])
def main():
    quanly=input("Hãy nhập các điểm kiểm tra cách nhau bới dấu cách: ").split()
    quanly=[float(i) for i in quanly]
    print("Điểm trung bình: ",sum(quanly)/len(quanly))
    print("Điểm cao nhất: ",max(quanly))
    print("Điểm thấp nhất: ",min(quanly))
    print("Điểm đầu tiên: ",(quanly[0]),"| ","Điểm cuối cùng: ",(quanly[len(quanly)-1]))
    while True:
        n=int(input("Nhập đầu điểm bạn muốn kiểm tra: "))
        while logic(quanly,n):
            print("Sai cú pháp xin hãy nhập lại!!!")
            n=int(input("Nhập đầu điểm bạn muốn kiểm tra: "))
        check=input("Bạn có muốn dừng lại|YES or NO: ")
        if check=="YES":
            break
    return
main()
