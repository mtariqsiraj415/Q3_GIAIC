import streamlit as st

# Library Management System
book_list = list()

# Streamlit app setup
st.title("Library Management System")

menu = """
1. Add Book
2. Remove Book
3. Show Books
4. Exit System
"""

# Function to add a book
def add_book(booklist, book):
    booklist.append(book)
    st.success("Book added Successfully")

# Function to remove a book
def remove_book(booklist, book):
    if book in booklist:
        booklist.remove(book)
        st.success("Book removed Successfully")
    else:
        st.error("Book not found")

# Function to display books
def show_books(booklist):
    if booklist:
        st.write("Added Books: ", ", ".join(booklist))
    else:
        st.write("Book list is empty")

# Streamlit UI components
choice = st.selectbox("Choose an option", options=["Add Book", "Remove Book", "Show Books", "Exit System"])

if choice == "Add Book":
    book_name = st.text_input("Enter the book name you want to add:")
    if st.button("Add Book"):
        if book_name:
            add_book(book_list, book_name)
        else:
            st.warning("Please enter a book name.")

elif choice == "Remove Book":
    book_name = st.text_input("Enter the book name you want to remove:")
    if st.button("Remove Book"):
        if book_name:
            remove_book(book_list, book_name)
        else:
            st.warning("Please enter a book name.")

elif choice == "Show Books":
    show_books(book_list)

elif choice == "Exit System":
    st.write("System Exited")
    st.write("Thanks Your Using Library")
    st.stop()

else:
    st.write("Please select an option from the dropdown menu.")
