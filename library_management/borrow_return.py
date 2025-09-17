from supabase_client import sb
from datetime import datetime

def borrow_book():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    book = sb.table("books").select("*").eq("book_id", book_id).execute().data
    if not book or book[0]["stock"] <= 0:
        print("Book not available")
        return
    # Decrease stock
    sb.table("books").update({"stock": book[0]["stock"] - 1}).eq("book_id", book_id).execute()
    # Insert borrow record
    sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()
    print("Book borrowed successfully")

def return_book():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    record = sb.table("borrow_records").select("*")\
        .eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute().data
    if not record:
        print("No borrow record found")
        return
    sb.table("borrow_records").update({"return_date": datetime.utcnow()})\
        .eq("record_id", record[0]["record_id"]).execute()
    book = sb.table("books").select("*").eq("book_id", book_id).execute().data
    sb.table("books").update({"stock": book[0]["stock"] + 1}).eq("book_id", book_id).execute()
    print("Book returned successfully")

def main():
    while True:
        print("\n--- Borrow & Return ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
