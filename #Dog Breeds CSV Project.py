#Dog Breeds CSV Project
#Febuaury 13

#Init
import csv
import random
import os
dogs_csv_path = "C:\\Users\\ldmanning\\Downloads\\dogs.csv"
dog_name_list = []
dog_weight_list = []
dog_picture_list = []
dog_characteristics = []
dog_usage = []
dog_lifespan = []

#Func
def display_image(image_url):
    os.system("start "+ image_url)

def get_size(weight):
    if(weight <= 20):
        return "small"
    elif(weight<=40):
        return "medium"
    elif(weight<=80):
        return "large"
    else:
        return "extra large"

def pickdog():
    #Reading a CSV File
    #While the file is open, do something
    with open(dogs_csv_path, 'r') as file: #'r' means read only mode. No changes are being done; the next lines of code are called file
        reader = csv.reader(file) #csv.reader is a function that reads a file. The opened file is the one we are reading (Established on line 17)

        for row in reader:
            dog_name_list.append(row[1])
            dog_weight_list.append((int(row[9])+int(row[8]))/2) #takes average
            dog_picture_list.append(row[11])
            dog_characteristics.append(row[10])
            dog_usage.append(row[3])
            dog_lifespan.append(row[4])
            
    size_request = input("What size dog are you looking for today?\nsmall\nmedium \nlarge \nextra large\nSize: ")

    #Filtering a List
    filtered_size = []
    for i in range(len(dog_name_list)):
        dog = dog_name_list[i]
        weight = dog_weight_list[i]
        if(size_request == get_size(weight)):
            filtered_size.append(dog)
    if(filtered_size):    
        ran= random.choice(filtered_size)
        i = dog_name_list.index(ran)
        display_image(dog_picture_list[i])
        print("I believe a "+ "\033[31m"+ ran + "\033[37m"+ " is the best dog for you!\n It is "+"\033[31m"+ dog_characteristics[i] + "\033[37m"+ "!\n Their main usage is "+ "\033[31m"+ dog_usage[i]+ "\033[37m" + ".\n They live for around "+ "\033[31m"+ dog_lifespan[i]+ "\033[37m"+ " years!")
    else:
        print("No dogs fit that weight! Please enter in the weight as it is EXPLICITLY typed!")
        pickdog()
        
#Main
pickdog()












