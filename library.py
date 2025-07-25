class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,new_book):
        self.books.append(new_book)
        print(f"\nBook:'{new_book}' added successfully!")
    def show_book(self):
        if not self.books:
            print("no book found")
        else:
            for i,book in enumerate(self.books,start=1):
                print(f"\n{i}: {book}")

    def options(self):
        print("\n1: Add a book")        
        print("2: show all  books")        
        print("3: EXIT")
        
library=Library() #new object is created
while True:    
    library.options()
    choice=input("Enter your choice: ").strip()
    if choice == "1":
        new_book=input("Enter a Book: ").strip()
        library.add_book(new_book)
    elif choice == "2":
        library.show_book()
    elif choice == "3":
        print("Library closed !")
        break
    else:
        print("Invalid choice,kindly fill from(1,2,3)")

