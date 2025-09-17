from supabase_client import sb

def list_books():
    books = sb.table("books").select("*").execute().data
    print("\n--- All Books ---")
    for b in books:
        print(b)

def search_books():
    keyword = input("Enter keyword to search in title: ")
    books = sb.table("books").select("*").ilike("title", f"%{keyword}%").execute().data
    print("\n--- Search Results ---")
    for b in books:
        print(b)

def member_details():
    member_id = int(input("Enter member ID: "))
    member = sb.table("members").select("*").eq("member_id", member_id).execute().data
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data
    print("\n--- Member Info ---")
    print("Member:", member)
    print("Borrowed Books:", borrowed)

def main():
    while True:
        print("\n--- List & Search ---")
        print("1. List All Books")
        print("2. Search Books")
        print("3. Show Member Details")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            list_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            member_details()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
