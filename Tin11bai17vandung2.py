def main():
    ex=input("Nhập một dãy số cách nhau bởi dấu cách: ").split()
    arr=list(set([str(i) for i in ex]))
    for i in arr:
        print("Số ",i," lặp lại ",ex.count(i)," lần")
main()
