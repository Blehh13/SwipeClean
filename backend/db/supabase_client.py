import os
from supabase import create_client, Client

class SupabaseClient:
    def __init__(self):
        self.url = os.getenv('SUPABASE_URL', 'https://your-project.supabase.co')
        self.key = os.getenv('SUPABASE_ANON_KEY', 'your-anon-key')
        self.client: Client = create_client(self.url, self.key)
    
    def get_client(self):
        """Get Supabase client instance"""
        return self.client
    
    def insert_file(self, file_data):
        """Insert file record"""
        try:
            result = self.client.table('files').insert(file_data).execute()
            return result.data
        except Exception as e:
            print(f"Error inserting file: {e}")
            return None
    
    def get_files(self, limit=100):
        """Get files from database"""
        try:
            result = self.client.table('files').select('*').limit(limit).execute()
            return result.data
        except Exception as e:
            print(f"Error getting files: {e}")
            return []
    
    def update_file_status(self, file_id, status):
        """Update file status"""
        try:
            result = self.client.table('files').update({'status': status}).eq('id', file_id).execute()
            return result.data
        except Exception as e:
            print(f"Error updating file status: {e}")
            return None
    
    def insert_ai_suggestion(self, suggestion_data):
        """Insert AI suggestion"""
        try:
            result = self.client.table('ai_suggestions').insert(suggestion_data).execute()
            return result.data
        except Exception as e:
            print(f"Error inserting AI suggestion: {e}")
            return None
    
    def get_suggestions(self, processed=False):
        """Get AI suggestions"""
        try:
            result = self.client.table('ai_suggestions').select('*').eq('is_processed', processed).execute()
            return result.data
        except Exception as e:
            print(f"Error getting suggestions: {e}")
            return []