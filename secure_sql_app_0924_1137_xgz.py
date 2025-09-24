# 代码生成时间: 2025-09-24 11:37:44
#!/usr/bin/env python

"""
A Bottle application to demonstrate prevention of SQL injection.
"""

from bottle import route, run, request, response, template
import sqlite3

# Database configuration
DB_PATH = 'app.db'

# Establish a connection to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Function to sanitize user input to prevent SQL injection
def safe_input(input_var):
    return str(input_var).replace("'", "''")

# Home page
@route('/')
def home():
    return template('<p>Welcome to the secure SQL application</p>'
                         '<form action="/search" method="post">'
                         '<input type="text" name="search_term" />'
                         '<input type="submit" value="Search" />'
                         '</form>')

# Search endpoint to prevent SQL injection
@route('/search', method='POST')
def search():
    try:
        # Retrieve search term from POST request, sanitize input
        search_term = safe_input(request.forms.get('search_term'))
        
        # Create a parameterized query to prevent SQL injection
        query = 'SELECT * FROM users WHERE username LIKE ?'
        cursor.execute(query, ('%' + search_term + '%',))
        
        # Fetch the results
        results = cursor.fetchall()
        if results:
            return template("<p>Search results:</p>"
                         