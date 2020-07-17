class Library:
    def __init__(self,Type,List1,List2,List3,Name):
        self.Type=Type
        self.List1=List1
        self.List2=List2
        self.List3=List3
        self.Name=Name
        self.LendDict={}

    def DisplayBookType(self):
        print("we have following types of books")
        for Type in self.Type:
            print(Type)

    def DisplayBookList1(self):
        print("we have following types of books")
        for List in self.List1:
            print(List)

    def DisplayBookList2(self):
        print("we have following types of books")
        for List in self.List2:
            print(List)

    def DisplayBookList3(self):
        print("we have following types of books")
        for List in self.List3:
            print(List)

    def LendBook(self,User,Book):
        if Book not in self.LendDict.keys():
            self.LendDict.update({Book:User})
            print('Books has been updated')
        else:
            print('Book is already Issued')

    def ReturnBook(self,Book):
        self.LendDict.pop(Book)
        print('you return book successfully')
        
    def DonateBook(self,Book):
        self.List1.append(Book)
        print('Book has been added to the list...Thankyou')

if __name__ == "__main__":
    Swapnil=Library(['A. Programming Books','B. Story Books','C. Agriculture Books'],['Python','C++','Java'],
    ['The Old man and the sea','''Charlotte's Web''','The Cat in the Hat'],['The Market gardener','Dirt to soil','Mini farming'],"Swapnil's")

    while(True):
        print(f"Welcome to the {Swapnil.Name} library. Enter your choice to continue")
        print("1. Display Book List")
        print("2. Lend a Book")
        print("3. Return a Book")
        print("4. Donate a Book")
        User_choice = input()
        if User_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            User_choice = int(User_choice)


        if User_choice == 1:
            Swapnil.DisplayBookType()
            User_choice=input()
            if User_choice not in ['A','B','C']:
                print('Please enter a valid option')
                continue
            else:
                User_choice=str(User_choice)
            
            if User_choice == 'A':
                Swapnil.DisplayBookList1()
            elif User_choice == 'B':
                Swapnil.DisplayBookList2()
            elif User_choice == 'C':
                Swapnil.DisplayBookList3()
            else:
                print('Not a valid option')

        elif User_choice == 2:
            Book = input("Enter the name of the book you want to lend: ")
            User = input("Enter your name: ")
            Swapnil.LendBook(User, Book)
       
        elif User_choice == 3:
            Book = input("Enter the name of the book you want to return: ")
            Swapnil.ReturnBook(Book)
            
        elif User_choice == 4:
            Book = input("Enter the name of the book you want to donate: ")
            Swapnil.DonateBook(Book)

        else:
            print("Not a valid option")

        print("Press c to continue and q to quit")
        User_choice2 = ""
        while(User_choice2!="c" and User_choice2!="q"):
            User_choice2 = input()
            if User_choice2 == "q":
                exit()

            elif User_choice2 == "c":
                continue


