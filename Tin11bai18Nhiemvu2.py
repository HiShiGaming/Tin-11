def updateA(st,name,point,n):
    if st<1 or st>n:
        return True
    else:
        return print("Điểm của học sinh có số thứ tự ",st," : "," ".join(list(map(str,point[st-1]))))
def updateB(st,name,point,n,l):
    if st<1 or st>n:
        return True
    if l>len(point[st-1]) or l<1:
        return True
    else:
        return print("Điểm của học sinh có số thứ tự ",st," : "," ".join(list(map(str,point[st-1][0:l]))))
def main():
    name=[]
    point=[]
    ave=[]
    n=int(input("Nhập số học sinh: "))
    for i in range(n):
        j=input("Nhập tên học sinh thứ "+str(i+1)+" : ")
        name.append(j)
        p=input("Điểm kiểm tra của học sinh "+j+" là: ").split()
        point.append([float(i) for i in p])
    for i in range(n):
        ans=sum(point[i])/len(point[i])
        print("Điểm trung bình của ",name[i]," : ",ans)
        ave.append(ans)
    print(name[ave.index(max(ave))],"đạt điểm trung bình ",max(ave)," cao nhất lớp.")
    print("Điểm thấp nhất ",min(ave))
    while True:
        st=int(input("Nhập số thứ tự muốn kiểm tra điểm: "))
        while updateA(st,name,point,n):
            print("Số thứ tự không hợp lệ, nhập lại!!!")
            st=int(input("Nhập số thứ tự muốn kiểm tra điểm: "))
        check=input("Bạn có muốn Tra cứu điểm theo n số điểm muốn tra cứu?(Có hoặc Không)")
        if check=="Có" or check=="CÓ":
              break
    while True:
        st=int(input("Nhập số thứ tự muốn kiểm tra điểm: "))
        l=int(input("Nhãy nhập n điểm muốn kiểm tra: "))
        while updateB(st,name,point,n,l):
            print("Số thứ tự hoặc n điểm kiểm tra không hợp lệ,nhập lại!!!")
            st=int(input("Nhập số thứ tự muốn kiểm tra điểm: "))
            l=int(input("Nhãy nhập n điểm muốn kiểm tra: "))
        check=input("Bạn có muốn kết thúc Tra cứu điểm theo n số điểm muốn tra cứu?(Có hoặc Không)")
        if check=="Có" or check=="CÓ":
              break               
main()
