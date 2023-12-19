import sqlite3

my_connection_manager = sqlite3.connect("gta.db")

my_cursor = my_connection_manager.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_date INT, release_name TEXT, release_city TEXT)")

data_insert_query = """
INSERT INTO gta (release_date, release_name, release_city) VALUES (?,?,?)
"""

first_sample_data = (1997, "Grand Theft Auto", "state of New Guernsey")
second_sample_data = (1999, "Grand Theft Auto 2", "Anywhere, USA")

# my_cursor.execute(data_insert_query, first_sample_data)
# my_cursor.execute(data_insert_query, second_sample_data)

# release_list = [
#     (2001, "Grand Theft Auto III", "Liberty City"),
#     (2002, "Grand Theft Auto: Vice City", "Vice City"),
#     (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
#     (2008, "Grand Theft Auto IV", "Liberty City"),
#     (2013, "Grand Theft Auto V", "Los Santos")
# ]
#
# my_cursor.executemany(data_insert_query, release_list)

# release_date_input = int(input("Release year: "))
# release_name_input = input("Release name: ")
# release_city_input = input("Release city: ")
#
# my_input_tuple = (release_date_input, release_name_input, release_city_input)
#
# my_cursor.execute(data_insert_query, my_input_tuple)

my_connection_manager.commit()

for row in my_cursor.execute("SELECT * FROM gta"):
    print(row)

my_connection_manager.close()
