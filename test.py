import sqlite3

records = [(y, x + 3, 100) for x, y in enumerate(["malesela", "confidence", "peggy"])]

try:
  #connect to database
  conn = sqlite3.connect("jupitervidya.db")

  #define cursor to execute queries
  cur = conn.cursor()
  
  #create a table
  #cur.execute("CREATE TABLE student (name text, rollno integer, average real)")
  
  #insert into a table
  #cur.executemany("INSERT INTO student values(?, ?, ?)", records)

  #commit to make changes to the db
  #conn.commit()

  #read db entries
  #for x in cur.execute("SELECT * FROM student order by name DESC"):
    #print(f"{x[0]}[id:{x[1]}], you got {x[2]}.")
  
  #fetch entries with: fetchone(), fetchmany() and fetchall() 
  #cur.execute("SELECT * FROM student order by name DESC")
  #for x in cur.fetchmany(3):
  #  print(x)

  #check how many students got over 70%
  cur.execute("SELECT name FROM student where average >= 70")
  print(cur.fetchall())
  
  #update the a specified record
  cur.execute("UPDATE student set name='sarah' where name ='Sara'")
  conn.commit()

except Exception as err:
  print(err)
else:
  print("Data is inserted")
finally:
  conn.close()
