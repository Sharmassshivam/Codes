from numpy import *


class Student:
    def __init__(self):
        self.array = array('i', [])
        self.nos = 0

    def set_array(self):
        self.nos = int(input('How many student have attended the training program : '))
        self.array = zeros(self.nos, dtype=int)

    def input(self):

        for i in range(self.nos):
            self.array[i] = int(input('Enter roll no : '))
            self.display()

    def sorted_input(self):
        no = int(input('Enter element'))
        self.array[0] = no
        self.display()
        for i in range(1, self.nos):
            no = int(input('Enter element'))
            for j in range(i + 1):
                if no < self.array[j]:
                    for k in range(i, j, -1):
                        self.array[k] = self.array[k - 1]
                    self.array[j] = no
                    self.display()
                    break
            else:
                self.array[i] = no
                self.display()

    def display(self):
        print('Entered roll no are : ', end="")
        for i in range(self.nos):
            print(self.array[i], end=" ")
        print()

    def linear_search(self):
        no = int(input('Enter roll no which you want to search : '))
        for i in range(self.nos):
            if self.array[i] == no:
                print('Roll no', no, 'found at', i, 'index')
                break
        else:
            print('Roll no', no, 'is not present.')

    def binary_search(self):

        start = 0
        end = self.nos - 1
        no = int(input('Enter roll no which you want to search : '))
        print('at start')
        print('start :', start, 'end :', end)
        while start <= end:
            mid = (start + end) // 2

            if self.array[mid] < no:
                start = mid + 1
                print('self.array[mid] < no')
                print('start :', start, 'end :', end)
            elif self.array[mid] > no:
                end = mid - 1
                print('self.array[mid] > no')
                print('start :', start, 'end :', end)
            else:
                print('element found')
                print('start :', start, 'end :', end)
                print('Roll no', 'found at', mid, 'index')
                return mid

        return -1

    def sentinal_search(self):
        no = int(input('Enter roll no which you want to search : '))
        temp = self.array[self.nos - 1]
        self.array[self.nos - 1] = no
        i = 0
        while self.array[i] != no:
            i += 1
        self.array[self.nos - 1] = temp
        if (i < self.nos - 1) or (no == self.array[self.nos - 1]):
            print('Roll no', 'found at', i, 'index')
        else:
            print("roll no not found")

    def fibonacci(self, n):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci_search(self):
        no = int(input('Enter roll no which you want to search : '))
        m = 0
        while self.fibonacci(m) < self.nos:
            m = m + 1

        offset = -1
        x=offset
        while self.fibonacci(m) > 1:
            mid = min(offset + self.fibonacci(m - 2), self.nos - 1)
            if no > self.array[mid]:
                m = m - 1
                offset = mid
                print("no >self.array[mid]")
                print("m =", m, "offset =", offset, "mid =", mid)
            elif no < self.array[mid]:
                m = m - 1
                print("no<self.array[mid]")
                print("m =", m, "offset =", offset, "mid =", mid)

            else:
                print("no == self.array[mid]")
                print("m =", m, "offset =", offset, "mid =", mid)
                return mid

        if self.fibonacci(m - 1) and self.array[x + 1] == no:
            return x + 1

        return -1

    def recursive_binary(self, arr, start, end, no):
        if start <= end:
            mid = (start + end) // 2
            if arr[mid] == no:
                print('self.array[mid] == no')
                print('start :', start, 'end :', end)
                return mid
            elif arr[mid] > no:
                print('self.array[mid] > no')
                print('start :', start, 'end :', end)
                return self.recursive_binary(self.array, start, mid - 1, no)
            else:
                print('self.array[mid] < no')
                print('start :', start, 'end :', end)
                return self.recursive_binary(self.array, mid + 1, end, no)
        else:
            return -1


while True:
    print("1.input\n2.sorted input\n3.linear search\n4.sentinel search\n5.binary search\n6.recursive binary "
          "search\n7.fibonacci search")
    c = int(input("enter choice"))
    if c == 0:
        break
    elif c == 1:
        s1 = Student()
        s1.set_array()
        s1.input()
    elif c == 2:
        s2 = Student()
        s2.set_array()
        s2.sorted_input()
    elif c == 3:
        s1.linear_search()
    elif c == 4:
        s1.sentinal_search()
    elif c == 5:
        result = s2.binary_search()
        if result != -1:
            print('Roll no', 'found at', result, 'index')
        else:
            print('Roll no', 'is not present.')

    elif c == 6:
        no = int(input('Enter roll no which you want to search : '))
        result = s2.recursive_binary(s2.array, 0, s2.nos-1, no)
        if result != -1:
            print('Roll no', 'found at', result, 'index')
        else:
            print('Roll no', 'is not present.')

    elif c == 7:
        n = s2.fibonacci_search()
        if n != -1:
            print('Roll no', 'found at', n, 'index')
        else:
            print('Roll no', 'is not present.')
    else:
        print("enter valid input")

'''    def sorted_input(self):

        for i  in range(self.nos):
            no = int(input('Enter element'))
            self.array[i]=no
            self.display()
            for j in range(i,0,-1):
                if self.array[j]>self.array[j+1]:
                    self.array[j],self.array[j+1]=self.array[j+1],self.array[j]
                    self.display()'''
