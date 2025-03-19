import streamlit as st
import os
import ast

LIBRARY_FILE="library.txt"

st.title("Library Management System ")


def load_library():
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as file:
                return ast.literal_eval(file.read())  # Safe evaluation
        except (SyntaxError, ValueError):
            print("Error reading the library file. It might be corrupted or empty.")
            return []
    return []

def save_library(library):
    with open(LIBRARY_FILE,"w") as file:
        file.write(str(library))



def add_book(library):
    title=input("Enter the title of the book:")
    author=input("Enter the author of the book:")
    year=input("Enter the publication yearL: ")
    genre=input("Enter the genre: ")
    read_status=input("Has the book been read? (yes/no): ")
    book={
        "title":title,
        "author":author,
        "year":year,
        "genre":genre,
        "read":read_status.lower()=="yes"
    }
    library.append(book)
    print("Book added successfully!")


def remove_book(library):
    title=input("Enter the title of the book to remove:")
    library[:]=[book for book in library if book["title"].lower()!=title.lower()]
    print("Book removed successfully!")



def search_book(library):
    choice=input("Search by:\n1. Title\n2. Author\n")
    keyword=input("Enter your search term ").lower()
    results=[]
    if choice=="1":
        results=[book for book in library if keyword in book["title"].lower()]
    elif choice=="2":
        results=[book for book in libaray if keyword in book["auther"].lower()]
    else:
        print("Invalid choice. Please try again.")
    if results:
        print("Search results:")
        for book in results:
            status="Read" if book['read'] else "Not read"
            print(f"{book['title']} by {book['author']} status {status}")
    else:
        print("No results found.")


def display_books(library):
    if library:
        print("Your Library:")
        for book in library:
            status="Read" if book['read'] else "Not read"
            print(f"{book['title']} by {book['author']} status {status}")
    else:
        print("Your library is empty")


def display_statistics(library):
    total_books=len(library)
    read_book=sum(book['read'] for book in library)
    percentage_read=(read_book/total_books*100) if total_books>0 else 0
    print(f"Total books: {total_books}")
    print(f"Percenatge read: {percentage_read:.2f}%")




def main():
    library=load_library()
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            add_book(library)
        elif choice=="2":
            remove_book(library)
        elif choice=="3":
            search_book(library)
        elif choice=="4":
            display_books(library)
        elif choice=="5":
            display_statistics(library)
        elif choice=="6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")


if __name__=="__main__":
    main()




