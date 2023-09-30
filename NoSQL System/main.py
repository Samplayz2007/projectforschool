import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkthemes import ThemedStyle

# Constants for paging
RECORDS_PER_PAGE = 5

# Variable to keep track of the current page
current_page = 1

# Functions for database operations
host = simpledialog.askstring("Input", "Enter the host:")
username = simpledialog.askstring("Input", "Enter the username:")
password = simpledialog.askstring("Input", "Enter the password:")

def display_database_info():
    selected_db = database_var.get()
    if not selected_db:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,   # Replace with your password
            database=selected_db
        )

        cursor = conn.cursor()

        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]

        conn.close()

        table_info_text.delete(1.0, tk.END)
        table_info_text.insert(tk.END, f"Tables in {selected_db}:\n\n")
        table_info_text.insert(tk.END, "\n".join(tables))
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")

def display_table_contents():
    global current_page
    selected_db = database_var.get()
    selected_table = table_var.get()
    if not selected_db or not selected_table:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,   # Replace with your password
            database=selected_db
        )

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {selected_table}")
        rows = cursor.fetchall()

        conn.close()

        # Calculate the total number of pages
        total_pages = (len(rows) + RECORDS_PER_PAGE - 1) // RECORDS_PER_PAGE

        # Update the current page label
        current_page_label.config(text=f"Page {current_page} of {total_pages}")

        # Calculate the start and end indices for the current page
        start_index = (current_page - 1) * RECORDS_PER_PAGE
        end_index = start_index + RECORDS_PER_PAGE

        # Display records for the current page
        table_contents_text.delete(1.0, tk.END)  
        table_contents_text.insert(tk.END, f"Contents of {selected_table} (Page {current_page}):\n\n")

        # Create separate entry boxes for each record's values
        for row in rows[start_index:end_index]:
            record_frame = ttk.Frame(table_contents_text)
            record_frame.grid(columnspan=3, sticky="nsew")

            for value in row:
                value_entry = ttk.Entry(record_frame, width=20, background='black', foreground='white')
                value_entry.insert(0, value)
                value_entry.grid(row=0, column=rows.index(row), padx=5, pady=5)

            edit_button = ttk.Button(record_frame, text="Edit", command=lambda r=row: update_record(selected_db, selected_table, r))
            edit_button.grid(row=1, column=rows.index(row), padx=5, pady=5)
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")


def create_database():
    new_db_name = simpledialog.askstring("Input", "Enter the name for the new database:")
    if not new_db_name:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )

        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE {new_db_name}")

        conn.commit()
        messagebox.showinfo("Success", f"Database '{new_db_name}' created successfully.")
        conn.close()
        
        connect_to_database()  # Reconnect to refresh database list
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error creating database: {e}")

def create_table():
    selected_db = database_var.get()
    if not selected_db:
        return

    new_table_name = simpledialog.askstring("Input", "Enter the name for the new table:")
    if not new_table_name:
        return
    
    new_table_columns = simpledialog.askstring("Input", "Enter table columns (e.g., 'id INT PRIMARY KEY, name VARCHAR(255)'):")
    if not new_table_columns:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=selected_db
        )

        cursor = conn.cursor()

        cursor.execute(f"CREATE TABLE {new_table_name} ({new_table_columns})")

        conn.commit()
        messagebox.showinfo("Success", f"Table '{new_table_name}' created successfully in '{selected_db}'.")
        conn.close()
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error creating table: {e}")
def next_page():
    global current_page
    current_page += 1
    display_table_contents()

def prev_page():
    global current_page
    if current_page > 1:
        current_page -= 1
        display_table_contents()

def insert_record():
    selected_db = database_var.get()
    selected_table = table_var.get()
    new_record = new_record_entry.get()
    
    if not selected_db or not selected_table or not new_record:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,   # Replace with your password
            database=selected_db
        )

        cursor = conn.cursor()

        try:
            cursor.execute(f"INSERT INTO {selected_table} VALUES {new_record}")
            conn.commit()
            messagebox.showinfo("Success", "Record inserted successfully.")
        except mysql.connector.Error as e:
            conn.rollback()
            messagebox.showerror("MySQL Error", f"Error inserting record: {e}")

        conn.close()
        display_table_contents()
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")

def update_record(selected_db, selected_table, record):
    selected_record = selected_record_entry.get()
    new_value = new_value_entry.get()
    
    if not selected_record or not new_value:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,   # Replace with your password
            database=selected_db
        )

        cursor = conn.cursor()

        try:
            cursor.execute(f"UPDATE {selected_table} SET {new_value} WHERE {selected_record}")
            conn.commit()
            messagebox.showinfo("Success", "Record updated successfully.")
        except mysql.connector.Error as e:
            conn.rollback()
            messagebox.showerror("MySQL Error", f"Error updating record: {e}")

        conn.close()
        display_table_contents()
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")

def delete_record(selected_db, selected_table, selected_record):
    if not selected_record:
        return
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,   # Replace with your password
            database=selected_db
        )

        cursor = conn.cursor()

        try:
            cursor.execute(f"DELETE FROM {selected_table} WHERE {selected_record}")
            conn.commit()
            messagebox.showinfo("Success", "Record deleted successfully.")
        except mysql.connector.Error as e:
            conn.rollback()
            messagebox.showerror("MySQL Error", f"Error deleting record: {e}")

        conn.close()
        display_table_contents()
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")

def reset_app():
    global current_page
    current_page = 1
    database_combobox.set('')
    table_combobox.set('')
    new_record_entry.delete(0, tk.END)
    selected_record_entry.delete(0, tk.END)
    new_value_entry.delete(0, tk.END)
    table_info_text.delete(1.0, tk.END)
    table_contents_text.delete(1.0, tk.END)

def display_table_window():
    selected_db = database_var.get()
    selected_table = table_var.get()
    if not selected_db or not selected_table:
        return

    try:
        # Create a new Toplevel window for displaying tables
        table_window = tk.Toplevel(root)
        table_window.title(f"Table: {selected_table}")

        # Create a Treeview widget to display table contents
        table_columns = []  # Store table column names
        table_data = []     # Store table data rows

        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,   # Replace with your password
            database=selected_db
        )

        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {selected_table}")

        for column in cursor.fetchall():
            table_columns.append(column[0])

        cursor.execute(f"SELECT * FROM {selected_table}")
        table_data = cursor.fetchall()

        conn.close()

        # Create Treeview columns
        tree = ttk.Treeview(table_window, columns=table_columns, show="headings")

        for column in table_columns:
            tree.heading(column, text=column)
            tree.column(column, width=100)  # Adjust the column width as needed

        tree.pack(padx=20, pady=20, fill='both', expand=True)

        # Insert table data into the Treeview
        for row in table_data:
            tree.insert("", "end", values=row)

        # Create Update Record Entry and Button
        update_frame = ttk.Frame(table_window)
        update_frame.pack(pady=10)

        new_value_label = ttk.Label(update_frame, text="New Values (e.g., 'name = 'Alice''):", background='black', foreground='white')
        new_value_label.grid(row=0, column=0)

        new_value_entry = ttk.Entry(update_frame, background='black', foreground='white')
        new_value_entry.grid(row=0, column=1)

        update_button = ttk.Button(update_frame, text="Update Record", command=update_record)
        update_button.grid(row=0, column=2, padx=10)

        # Create Delete Record Button
        delete_button = ttk.Button(table_window, text="Delete Record", command=delete_record)
        delete_button.pack(pady=10)
    except mysql.connector.Error as e:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")

# Create the main application window
root = tk.Tk()
root.title("Database Visualizer")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size as a percentage of the screen size
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
root.geometry(f"{window_width}x{window_height}")

style = ThemedStyle(root)
style.set_theme("equilux")

# Create a main frame
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, fill='both', expand=True)

# Frame 1 for buttons (top)
frame1 = ttk.Frame(main_frame)
frame1.pack(side="top", padx=10, pady=10, fill="both", expand=True)

# Database selection
database_label = ttk.Label(frame1, text="Select Database:", background='black', foreground='white')
database_label.pack()

database_var = tk.StringVar()
database_combobox = ttk.Combobox(frame1, textvariable=database_var)
database_combobox.pack(fill="x")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="The_Fox",       # Replace with your username
        password="Amsam"      # Replace with your password
    )

    cursor = conn.cursor()

    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]

    database_combobox["values"] = databases

    conn.close()
except mysql.connector.Error as e:
    messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {e}")

create_db_button = ttk.Button(frame1, text="Create Database", command=create_database)
create_db_button.pack(fill="x")

create_table_button = ttk.Button(frame1, text="Create Table", command=create_table)
create_table_button.pack(fill="x")

# Button to display database info
info_button = ttk.Button(frame1, text="Display Database Info", command=display_database_info)
info_button.pack(fill="x", pady=10)

# New Record Entry
new_record_label = ttk.Label(frame1, text="New Record (e.g., '(1, 'John', 'Doe')'):", background='black', foreground='white')
new_record_label.pack()

new_record_entry = ttk.Entry(frame1, background='black', foreground='white')
new_record_entry.pack()

# Insert Record Button
insert_button = ttk.Button(frame1, text="Insert Record", command=insert_record)
insert_button.pack()

# Selected Record Entry (for update and delete)
selected_record_label = ttk.Label(frame1, text="Selected Record (e.g., 'id = 1'):", background='black', foreground='white')
selected_record_label.pack()

selected_record_entry = ttk.Entry(frame1, background='black', foreground='white')
selected_record_entry.pack()

# New Value Entry (for update)
new_value_label = ttk.Label(frame1, text="New Value (e.g., 'name = 'Alice''):", background='black', foreground='white')
new_value_label.pack()

new_value_entry = ttk.Entry(frame1, background='black', foreground='white')
new_value_entry.pack()

# Update Record Button
update_button = ttk.Button(frame1, text="Update Record", command=update_record)
update_button.pack()

# Delete Record Button
delete_button = ttk.Button(frame1, text="Delete Record", command=delete_record)
delete_button.pack()

# Create a Reset Button
reset_button = ttk.Button(frame1, text="Reset App", command=reset_app)
reset_button.pack()

# Frame 2 for displaying database info and table selection (bottom)
frame2 = ttk.Frame(main_frame)
frame2.pack(side="top", padx=10, pady=10, fill="both", expand=True)

# Table selection
table_label = ttk.Label(frame2, text="Select Table:", background='black', foreground='white')
table_label.pack()

table_var = tk.StringVar()
table_combobox = ttk.Combobox(frame2, textvariable=table_var)
table_combobox.pack(fill="x")

# Button to display table contents in a separate window
contents_button = ttk.Button(frame2, text="Display Table Contents", command=display_table_window)
contents_button.pack(fill="x", pady=10)

# Text widget to display table info
table_info_text = tk.Text(frame2, height=10, width=40, background='black', foreground='white')
table_info_text.pack(fill='both', expand=True)

root.mainloop()
