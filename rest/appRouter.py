from django.http import HttpResponse
class AppRouter:
    """A router to control all database operations on models in
    the ospi application"""

    def db_for_read(self, model, **hints):
            
        return None

    def db_for_write(self, model, **hints):
        
        return None
