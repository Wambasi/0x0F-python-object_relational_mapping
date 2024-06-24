if __name__ == "__main__":
    
    import MySQLdb
    from sys import argv
    
    my_database = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306   
    )
    
    my_cursor = my_database.cursor()
    
    querry = "SELECT * from states WHERE name = %s ORDER BY stated.id;"
    my_cursor.execute(querry, (argv[4],))
    my_data = my_cursor.fetchall()
    
    
    for row in my_data:
        print(row)
        
    my_cursor.close()
    my_database.close()