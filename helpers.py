import sqlite3
import base64


# Runs SQL statements that modify the database
def sql_commit(sql_statement, values=None, database='uqhair.db'):

  # Connect to the database (default is uqhair.db)
  with sqlite3.connect(database) as conn:
 
    # Create a cursor to iterate through rows
    cursor = conn.cursor()
    
    # Set foreign_keys to be ON (off by default in SQLite - makes CASCADE work)
    cursor.execute("PRAGMA foreign_keys = ON;")
 
    # Execute the SQL statement
    if values is None:
      cursor.execute(sql_statement)
    else:
      # Allows values to be entered as a single value or a tuple
      if isinstance(values, tuple):
        if not isinstance(values[0], tuple):
          values = (values,)
      else:
        values = ((values,),)
      for value in values:
        cursor.execute(sql_statement, value)
 
    # Commit (write) the changes
    conn.commit()


# Runs SQL statements that query the database
def sql_fetch(sql_statement, values=None, database='uqhair.db'):
  
  # Connect to the database (default is uqhair.db)
  with sqlite3.connect(database) as conn:
 
    # Create a cursor to iterate through rows
    cursor = conn.cursor()

    # Allows us to access data returned using dictionary key-type notation
    # e.g. row["username"] instead of row[2]
    cursor.row_factory = sqlite3.Row

    # Execute the SQL statement
    if values is None:
        cursor.execute(sql_statement)
    # Allows values to be entered as a single value or tuple
    else:
        if not isinstance(values, tuple):
            values = (values,)
        cursor.execute(sql_statement, values)

    # Fetch the results as a list
    rows = cursor.fetchall()
    return rows


# Converts an image file into a binary object (blob) to store in the database
def convert_image(filename):
  with open(filename, 'rb') as f:
    blob = f.read()
    return blob


# Converts the blob to an image source attribute to insert into our HTML email
def convert_blob(blob):
  base64_image = base64.b64encode(blob)
  image_source = f"data:image/jpeg;base64,{base64_image.decode('utf-8')}"
  return image_source