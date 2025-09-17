import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# Delete product by ID
def delete_product(product_id):
    resp = sb.table("products1").delete().eq("product_id", product_id).execute()
    return resp.data

if __name__ == "__main__":
    product_id = int(input("Enter product ID to delete: ").strip())
    deleted = delete_product(product_id)
    print("Deleted:", deleted)
