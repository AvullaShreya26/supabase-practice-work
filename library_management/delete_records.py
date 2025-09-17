from supabase_client import sb

def delete_member():
    member_id = int(input("Enter member ID to delete: "))
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data
    if borrowed:
        print("Cannot delete: Member has borrowed books")
        return
    res = sb.table("members").delete().eq("member_id", member_id).execute().data
    print("Deleted member:", res)

def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).execute().data
    if borrowed:
        print("Cannot delete: Book is currently borrowed")
        return
    res = sb.table("books").delete().eq("book_id", book_id).execute().data
    print("Deleted book:", res)

def main():
    while True:
        print("\n--- Delete Records ---")
        print("1. Delete Member")
        print("2. Delete Book")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            delete_member()
        elif choice == "2":
            delete_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
