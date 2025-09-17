import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# Get all products
def get_products():
    resp = sb.table("products1").select("*").execute()
    return resp.data

if __name__ == "__main__":
    products = get_products()
    print("Products:", products)


