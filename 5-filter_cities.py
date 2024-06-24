if __name__ == "__main__":
    
    import MySQLdb
    from sys import argv
    
    my_database = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        databse=argv[3],
        port=3306
    )
    
    my_cursor = my_database.cursor()
    
    querry = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id ASC;"
                
    my_cursor.execute(querry, (argv[4],))
    my_data = my_cursor.fetchall()
    if len(my_data) == 0:
        print()
    else:
        tup = ()
        for row in my_data:
            tup += row
        for i in range(len(tup)):
            if i == len(tup) - 1:
                print(tup[i])
            else:
                print(tup[i], end=',')
                
    my_cursor.close()
    my_database.close()
    