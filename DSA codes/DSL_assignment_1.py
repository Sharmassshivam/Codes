def creat_set(len):
    a=[]

    for i in range(0,len):
        j=int(input("enter alement in set"))
        if j in a:
            print("duplicate entry")
        else:
            a.append(j)
    return a

def display(a):
    print("{" , end="")
    for i in range(0,len(a)):
            print(" ",a[i]," ,", end="")
    print("}")

def intersection(a , b):
    inter = []
    for i in a :
        if i in b:
            inter.append(i)

    return inter

def union(p, q):
    union = []
    for i in p:
        union.append(i)
    for j in q:
        if j not in union:
            union.append(j)
    return union

def difference(a,b):
    diff = []
    for i in a:
        if i not in b:
            diff.append(i)
    return diff

def no_of(a):
    print(len(a))

a_len = int(input("enter no of element in Cricket"))
a_set = creat_set(a_len)

b_len = int(input("enter no of element in Badminton"))
b_set = creat_set(b_len)

c_len = int(input("enter no of element in Football"))
c_set = creat_set(c_len)

print("cricket set is")
display(a_set)
print("Badminton set is")
display(b_set)
print("cricket set is")
display(c_set)
a_int_b=intersection(a_set , b_set)
a_union_b=union(a_set,b_set)
a_union_c=union(a_set,c_set)
a_diff_b=difference(a_set,b_set)
a_int_c = intersection(a_set, c_set)
b_int_c = intersection(b_set, c_set)

while True:
    print("\n1.List of students who play both cricket and badminton\n2.List of students who play either cricket or badminton but not both \n3.Number of students who play neither cricket nor badminton\n4.Number of students who play cricket and football but not badminton\n0.Quit")
    c=int(input("Enter choice"))
    if c==0:
        print("Quit")
        break
    elif c==1:
        print("List of students who play both cricket and badminton")
        display(a_int_b)
    elif c==2:
        s = difference(a_union_b, a_int_b)
        print("List of students who play either cricket or badminton but not both")
        display(s)
    elif c==3:
        w = difference(c_set, a_union_b)
        print("Number of students who play neither cricket nor badminton")
        no_of(w)
        print("they are")
        display(w)
    elif c==4:
        a = difference(a_union_c, b_set)
        print("Number of students who play cricket and football but not badminton")
        no_of(a)
        print("they are")
        display(a)

    else:
        print("Wronge Input")



