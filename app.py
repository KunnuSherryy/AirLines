from supabase import create_client, Client

url = "https://xfaymniijjilpgxogxrh.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhmYXltbmlpamppbHBneG9neHJoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ2MTA1MjcsImV4cCI6MjA2MDE4NjUyN30.KCB6vgJL-_6tDdTCU2ARWYfRfPUuJwJX7gnxY7m5INk"

supabase: Client = create_client(url, key)

# Inserting data
insert_response = supabase.table("airport").insert({
    "name": "Indira Gandhi Intl",
    "city": "Delhi",
    "contactno": "1234567890",
    "address": "Delhi Airport Road"
}).execute()
print("Insert response:", insert_response)

# Fetching data
data = supabase.table("airport").select("*").execute()
print("All data:", data)
