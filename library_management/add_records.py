from supabase_client import sb

def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    try:
        res = sb.table("members").insert({"name": name, "email": email}).execute()
        print("Member added:", res.data)
    except Exception as e:
        print("Error adding member:", e)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    stock = int(input("Enter stock: "))
    try:
        res = sb.table("books").insert({
            "title": title,
            "author": author,
            "category": category,
            "stock": stock
        }).execute()
        print("Book added:", res.data)
    except Exception as e:
        print("Error adding book:", e)

def main():
    while True:
        print("\n--- Add Records ---")
        print("1. Add Member")
        print("2. Add Book")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_member()
        elif choice == "2":
            add_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
