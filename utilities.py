

DATABASE_FILE = "./origami.db"

'''Functions'''
def show_all(connection):
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


def show_item(connection, find_type, value):
    '''prints a specific origami model's information'''
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM origami_models WHERE "
        match find_type:
            case '1':
                #find the item by name
                sql += "model_name = ?"
            case '2':
                #find the item by difficulty level
                sql += "difficulty_level = ?"
        cursor.execute(sql, (value,))
        results = cursor.fetchall()
        #check if the item was in the table
        if len(results) == 0:
            print('The item you are searching for could not be found. Please try again with correct values')
        else:
            #print the item(s)
            print(f"{'model_id':<15}{'model_name':<20}{'description':<140}{'difficulty_level'}")
            for item in results:
                print(f"{item[0]:<15}{item[1]:<20}{item[2]:<140}{item[3]}")
    except:
         print("Something went wrong with finding the item")


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

