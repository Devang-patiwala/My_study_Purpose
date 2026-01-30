Books = {
    "Python": {"Available":5, "Issued":0},
    "Java": {"Available":5, "Issued":0},
    "JavaScript": {"Available":5, "Issued":0}
}
while True:
    print("\n Library Management System: ")
    print("1.. View All Books From Library")
    print("2.. Issue a book to a student")
    print("3.. Return a book")
    print("4.. Add new books to the library")
    print("5.. Remove books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice==1:
        print("All Books From Library")
        for book,b in Books.items():
            print(f"{book}{b}")

    elif choice==2:
        print("Issue a book to a student");
        book = input("Enter Book name : ")
        if book in Books:
            print(f"\n {book} Book is Issued")
        else:
            print("\n Book is not available Sorry")


    elif choice==3:
        book = input("Enter Book name to Return : ")
        if book in Book:
            print(f"\n {book} Book is Returned Successfully");
        else:
            print("\n Book not Returned")

    elif choice==4:
        print("Add new book to Library")
        book = input("Enter Book name to Enter: ")
        if book in Books:
            print("\n Book  already Exists")
        else:
            Available = int(input("Enter Available Book Number: "))
            Issued = int(input("Enter Issued Book Number: "))
            Books[book] = {"Available":Available, "Issued":Issued}

    elif choice==5:
        book = input("Enter the Book's name to delete: ")
        if book in Books:
            del Books[book]
            print("\n Book deleted successfully!")
        else:
            print("\n Book not found!")
        
    elif choice==6:
        print("\n Thank you for using the Student Marks System. Goodbye!");
        break;
    else:
        print('Invalid Choice!')
