import math
def dem(n,ave):
    cou=0
    for i in n:
        if i>ave:
          cou+=1
    return cou
chieucao=input("Hãy nhập chiều cao của từng người: ").split()
chieucao=[int(i) for i in chieucao]
print("Chiều cao trung bình của cả lớp là: ",sum(chieucao)/len(chieucao))
print("Số bạn có chiều cao hơn trung bình của lớp là: ",dem(chieucao,sum(chieucao)/len(chieucao)))
