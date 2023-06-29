import sqlite3
#get functions and DATABASE_FILE from utilities
from utilities import(show_all, show_item, add_item, delete_item, update_item, DATABASE_FILE)


#open the connection


with sqlite3.connect(DATABASE_FILE) as connection:
     #user interaction
     while True:
         user_input = input(f"\nWhat would you like to do?\n1.Print item(s)\n2.Add an item\n3.Delete an item\n4.Update an item's description\nPress Enter to exit\n")
         match user_input:
             case '1':
                 #print origami model(s)
                 print_origami = input("\nIs there a specific item you would like to search for?\nY/N\n")
                 match print_origami.capitalize():
                     case 'Y':
                        #  search for an item(s)
                         find_type = input(f"\nWhat would you like to search for the item by?\n1.Name\n2.Difficulty level\n")
                         if find_type == '1':
                            # view an item by name
                            find_name = input(f"\nWhat is the name of the item you would like to see?\n")
                                #print the item
                            show_item(connection, find_type, find_name)
                         elif find_type == '2':
                            #view an item(s) by difficulty level
                            find_difficulty = input(f"\nWhat is the difficulty level of the items you would like to see?\n")
                            show_item(connection, find_type, find_difficulty)
                     case'N':
                         #print all the origami models
                         show_all(connection)
             case '2':
                 #add a new origami model to the database
                 item_name = input("\nItem name: ")
                 item_description = input("\nItem description: ")
                 item_difficulty_level = input("\nItem difficulty: ")
                 add_item(connection, item_name, item_description, item_difficulty_level)
             case '3':
                 #delete an item by name
                 item_name = input("\nItem name: ")
                 delete_item(connection, item_name)
             case '4':
                 #update the item's description
                 item_name = input("\nItem name: ")
                 new_item_description = input("\nUpdated description: ")
                 update_item(connection, item_name, new_item_description)
             case _:
                 #when the user wants to exit, they can enter a random key, and the loop will break
                 print("\nGoodbye.")
                 break


#connection will close automatically


'''
#add item
     delete_item(connection, "Crane")
     show_origami(connection)

#update item
     update_item(connection, "Crane", "The origami crane symbolizes peace and is one of the most popular origami models.")
     show_origami(connection)
'''