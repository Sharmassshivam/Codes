class String:
    def __init__(self):
        self.str=" "


    def split_str(self):
        l = []
        initial = 0
        for i in range(len(self.str)):
            if self.str[i] == " ":
                l.append(self.str[initial:i])
                initial = i + 1
            if i == len(self.str) - 1:
                l.append(self.str[initial:])
        return l

    def longest_word(self):

        list = self.split_str()
        long = list[0]
        for i in range(len(list)):
            if len(list[i]) > len(long):
                long = list[i]
        print("longest word in the given string is", long)
            

    def frequency(self):
        count=0
        character=input("enter character of which frequency has to calculate")
        for i in self.str:
            if character==i:
                count+=1
        print(character,"occure",count,"times")

    def palindrome(self):
        s = input("enter string to check palindrome : ")
        r=[]
        for i in range(len(s)-1 , -1 , -1):
            r.append(s[i])
        reverse="".join(r)
        if s == reverse:
            print(s,"is palindrom")
        else:
            print(s," is not a palindrome")

    def substring(self):
        sub = input("enter substring : ")
        sub_len = len(sub)
        for i in range(len(self.str)):
            if self.str[i:i + sub_len] == sub:
                print(sub ," substring found at", i)
                break
        else:
            print("substring not found")
    def count_word(self):
        list=self.split_str()

        d = {}
        for i in list:
            if i  in d:
                d[i]+=1
            else:
                d[i]=1
        for i , j  in d.items():
            print(i," occure", j, "times")

s1 = String()
s1.str=input("enter your string : ")
# s1.longest_length()
print(" 1.To display word with the longest length\n 2.To determines the frequency of occurrence of particular character in the string\n 3.To check whether given string is palindrome or not\n 4.To display index of first appearance of the substring\n 5.To count the occurrences of word in a given string\n 0.Quit\n")
while True:

    c = int(input("Enter your choice"))
    if c==0:
        print("Quit")
        break
    elif c==1:
        s1.longest_word()
    elif c==2:
        s1.frequency()
    elif c==3:
        s1.palindrome()
    elif c==4:
        s1.substring()
    elif c==5:
        s1.count_word()
    else:
        print("wrong input")




