import os
from supabase import create_client, Client

# Gantilah dengan detail dari Supabase Anda
SUPABASE_URL = "https://your-project-url.supabase.co"
SUPABASE_KEY = "your-anon-or-service-role-key"

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
