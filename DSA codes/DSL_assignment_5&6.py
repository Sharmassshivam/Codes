

import numpy as np



class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = np.zeros(self.len, dtype=int)

    def input(self):
        print("Enter {} inputs for roll numbers ".format(self.len))
        for i in range(self.len):
            self.arr[i] = float(input())

    def display(self):
        print("The array is {", end="")
        for i in range(self.len):
            print(self.arr[i], end=",")
        print("}")

    def bubble_sort(self):
        self.display()
        for pas in range(self.len - 1, 0, -1):
            swap_flag = False
            print("Pass ", pas)
            for i in range(pas):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swap_flag = True
                print("i=", i, end="  ")
                self.display()
            if not swap_flag:
                break

    def selection_sort(self):
        self.display()
        for i in range(self.len - 1):
            minimum = i
            print("i =", i, "\nMin=", self.arr[minimum], end="  ")
            for j in range(i, self.len - 1):
                if self.arr[j + 1] < self.arr[minimum]:
                    minimum = j + 1
                print("Min=", self.arr[minimum], end="  ")
            self.arr[i], self.arr[minimum] = self.arr[minimum], self.arr[i]
            self.display()

    def insertion_sort(self):
        self.display()
        for i in range(1, self.len):
            print("i =", i)
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j - 1]:
                    self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                self.display()

    def shell_sort(self):
        self.display()
        d = self.len // 2
        while d > 0:
            print("d= ", d)
            for i in range(d, self.len):
                print(i)
                j = i
                curr = self.arr[i]
                while j >= d and self.arr[j - d] > curr:
                    self.arr[j], self.arr[j - d] = self.arr[j - d], self.arr[j]
                    j -= d
                self.arr[j] = curr
                self.display()
            d //= 2

    def rec_quick_sort(self, left, right):
        self.display()
        if left < right:
            i, j, pivot = left+1, right, self.arr[left]
            print("left ", left, "  right ", right,"  pivot ",pivot)
            while True:
                while i < right and self.arr[i] < pivot:
                    i += 1
                while j > left and self.arr[j] > pivot:
                    j -= 1
                print("i=", i, "  j=", j," a[i]=", self.arr[i], "  a[j]=", self.arr[j],end="\n")
                if i < j:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    self.display()
                else:
                    break
            self.arr[left], self.arr[j] = self.arr[j], self.arr[left]
            self.display()
            self.rec_quick_sort(left, j)
            self.rec_quick_sort(j+1, right)



while True:
    choice = int(input("""\nSelect an operation  
1 for Terminating 
2 for Bubble Sort
3 for Selection Sort
4 for Insertion Sort
5 for Shell Sort
6 for Quick Sort
  """))
    if choice == 1:
         break
    elif choice == 2:
        n = int(input("Enter the number of nos to enter :"))
        a1 = Sort(n)
        a1.input()
        a1.bubble_sort()
        a1.display()
    elif choice == 3:
        n = int(input("Enter the number of nos to enter :"))
        a2 = Sort(n)
        a2.input()
        a2.selection_sort()
        a2.display()
    elif choice == 4:
        n = int(input("Enter the number of nos to enter :"))
        a3 = Sort(n)
        a3.input()
        a3.insertion_sort()
        a3.display()
    elif choice == 5:
        n = int(input("Enter the number of nos to enter :"))
        a4 = Sort(n)
        a4.input()
        a4.shell_sort()
        a4.display()
    elif choice == 6:
        n = int(input("Enter the number of nos to enter :"))
        a5 = Sort(n)
        a5.input()
        a5.rec_quick_sort(0, a5.len - 1)

