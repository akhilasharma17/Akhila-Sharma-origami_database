import sqlite3

DATABASE_FILE = "./origami.db"

#open the connection

'''Functions'''
def show_origami(connection):
    '''prints all the origami models' information'''
    try:
         cursor = connection.cursor()
         sql = "SELECT * FROM origami_models"
         cursor.execute(sql)
         results = cursor.fetchall()
         print(f"{'model_id':<15}{'model_name':<20}{'description':<140}{'difficulty_level'}")
         for item in results:
             print(f"{item[0]:<15}{item[1]:<20}{item[2]:<140}{item[3]}")
    except:
        print("Something went wrong with connection.")


def add_item(connection, item_name, item_description, item_difficulty_level):
    '''adds an item to the origami database'''
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO origami_models(model_name, description, difficulty_level) VALUES (?, ?, ?)"
        cursor.execute(sql,(item_name, item_description, item_difficulty_level))
        connection.commit()
    except:
        #could not commit connection because something was incomplete
        print("Couldn't add item.")


def delete_item(connection, item_name):
    '''deletes an item by name from the origami database'''
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM origami_models WHERE model_name = ?"
        cursor.execute(sql,(item_name,))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            #none of the rows in the table had the item
            print("Couldn't find item.")
        else:
            connection.commit()
    except:
        #could not commit connection because something was incomplete
        print("Couldn't delete item. Item does exist.")


def update_item(connection, item_name, new_item_description):
    '''updates/modifies an item by name from the origami database'''
    try:
        cursor = connection.cursor()
        #update item's description
        sql = "UPDATE origami_models SET description = ? WHERE model_name = ?"
        cursor.execute(sql,(new_item_description, item_name))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print("Cannot update item.")
        else:
            connection.commit()
    except:
        #could not commit connection because something was incomplete or missing
        print("Failed to update the item.")

with sqlite3.connect(DATABASE_FILE) as connection:
    #user interaction
    while True:
        user_input = input(f'''\nWhat would you like to do?
1.Print an item
2.Add an item
3.Delete an item
4.Update an item's description
5.Exit\n''')
        if user_input == '1':
            #print origami model
            show_origami(connection)
        elif user_input == '2':
            #add a new origami model to the database
            item_name = input("\nItem name: ")
            item_description = input("\nItem description: ")
            item_difficulty_level = input("\nItem difficulty: ")
            add_item(connection, item_name, item_description, item_difficulty_level)
        elif user_input == '3':
            #delete an item by name
            item_name = input("\nItem name: ")
            delete_item(connection, item_name)
        elif user_input == '4':
            #update the item's description
            item_name = input("\nCurrent item: ")
            new_item_description = input("\nUpdated description: ")
            update_item(connection, item_name, new_item_description)
        else:
            print("\nGoodbye.")
            break

#connection will close automatically

#use match and cases to put two different tables in one code file









# with sqlite3.connect(DATABASE_FILE) as connection:
#     #user interaction
#     while True:
#         user_input = input(f"\nWhat would you like to do?\n1.Print an item\n2.Add an item\n3.Delete an item\n4.Update an item's description\n")
#         match user_input:
#             case '1':
#                 #print origami model
#                 show_origami(connection)
#             case '2':
#                 #add a new origami model to the database
#                 item_name = input("\nItem name: ")
#                 item_description = input("\nItem description: ")
#                 item_difficulty_level = input("\nItem difficulty: ")
#                 add_item(connection, item_name, item_description, item_difficulty_level)
#             case'3':
#                 #delete an item by name
#                 item_name = input("\nItem name: ")
#                 delete_item(connection, item_name)
#             case '4':
#                 #update the item's description
#                 item_name = input("\nCurrent item: ")
#                 new_item_description = input("\nUpdated description: ")
#                 update_item(connection, item_name, new_item_description)
#             case _:
#                 print("\nGoodbye.")
#                 break
'''
#add item
    # delete_item(connection, "Crane")
    # show_origami(connection)

# #update item
#     update_item(connection, "Crane", "The origami crane symbolizes peace and is one of the most popular origami models.")
#     show_origami(connection)
'''