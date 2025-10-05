"""Database helper module for MySQL operations."""

import mysql.connector
from mysql.connector import Error

class DatabaseHelper:
    """Handle database connections and operations."""
    
    def __init__(self, host="localhost", user="root", password="", database="hotel_management"):
        """Initialize database connection parameters."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        """Establish database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return True
        except Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def disconnect(self):
        """Close database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
