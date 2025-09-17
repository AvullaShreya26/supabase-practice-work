import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# Update stock only
def update_stock(product_id, stock):
    resp = sb.table("products13").update({"stock": stock}).eq("product_id", product_id).execute()
    return resp.data

if __name__ == "__main__":
    product_id = int(input("Enter product ID to update stock: ").strip())
    stock = int(input("Enter new stock: ").strip())
    updated = update_stock(product_id, stock)
    print("Stock Updated:", updated)
