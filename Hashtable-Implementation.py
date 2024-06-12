# Name: Nana Kwasi Owusu
# Program Description: Implementation of an open-hashing hash table

from birthday import Birthday

def read_file(file_name):
    '''
    This function reads birthday data from a file and returns a list of lines.
    It returns a list of lists, where each inner list represents a birthday.
    If the file does not exist, prints an error message and returns None.
    '''
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: that file does not exist. Try again.")
        return None

if __name__ == "__main__":
    hash_table = [[] for num in range(12)] #creates a hash table with 12 empty lists
    
    #this loop asks the user to enter a file name until they enter a correct one 
    birthdays = None
    while birthdays is None:
        file_name = input("Enter name of the data file: ")
        birthdays = read_file(file_name)
    
    #splits the string into day, month and year parts
    for i, bday in enumerate(birthdays):
        date_parts = bday.split('/')
        day = int(date_parts[1])
        month = int(date_parts[0])
        year = int(date_parts[2])
        
        #creating a birthday object
        birthday_object = Birthday(month, day, year)
        
        #getting the hash location for the birthday object 
        hash_location = hash(birthday_object)
        
        # Add the Birthday object and its line number to the appropriate hash table bucket
        hash_table[hash_location].append((birthday_object, i))
   
   # Output the number of elements in each hash table bucket
    for index, bucket in enumerate(hash_table):
        print(f"Hash location {index} has {len(bucket)} elements in it.")


    

