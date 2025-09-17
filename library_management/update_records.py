from supabase_client import sb

def update_member_email():
    member_id = int(input("Enter member ID: "))
    new_email = input("Enter new email: ")
    try:
        res = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
        print("Updated member:", res.data)
    except Exception as e:
        print("Error updating member:", e)

def update_book_stock():
    book_id = int(input("Enter book ID: "))
    new_stock = int(input("Enter new stock: "))
    try:
        res = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
        print("Updated book stock:", res.data)
    except Exception as e:
        print("Error updating book:", e)

def main():
    while True:
        print("\n--- Update Records ---")
        print("1. Update Member Email")
        print("2. Update Book Stock")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            update_member_email()
        elif choice == "2":
            update_book_stock()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
