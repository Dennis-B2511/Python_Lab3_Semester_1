import tkinter as tk
from PIL import Image, ImageTk  # Pillow-Bibliothek nötig
import random
import pygame

angle = 0 #Start angle for animation 


weight_coefficient_dictionary = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}
def key_generator():

    #Why range 1-104 -> Code Format: XXXX-XXXX-XXXX , max sum per block is ZZZZ = 104
    #random.radint() choses a random int from a list 
    def intervall_generator():
        numbers_list = list(range(1,105))   
        intervall_lenght = 5
        max_intervall_start = len(numbers_list) - intervall_lenght 
        start = random.randint(0, max_intervall_start)

        random_intervall_sequence = numbers_list[start: start + intervall_lenght]
        return random_intervall_sequence

    #random.sample(alphabet_list_str_1, 4) choses 4 random chars from the list
    #afterwads I put them together in a Block string (first XXXX)
    #with my weight_coefficient_dictionary I translate the random chars in int numbers and sum them up
    #I return sum_block_1, block_str_1 because I need this variables afterswards in another function 
    def block_generator_1():
        alphabet_list_str_1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                            "W", "X", "Y", "Z"]
        
        random_alphabet_sample_1 = random.sample(alphabet_list_str_1, 4)
        block_str_1 = random_alphabet_sample_1[0]+random_alphabet_sample_1[1]+random_alphabet_sample_1[2]+random_alphabet_sample_1[3]
        sum_block_1 = sum([weight_coefficient_dictionary[random_alphabet_sample_1[0]],weight_coefficient_dictionary[random_alphabet_sample_1[1]],
            weight_coefficient_dictionary[random_alphabet_sample_1[2]],weight_coefficient_dictionary[random_alphabet_sample_1[3]]])
        return sum_block_1, block_str_1
    
    def block_generator_2():
        alphabet_list_str_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                            "W", "X", "Y", "Z"]
        
        random_alphabet_sample_2 = random.sample(alphabet_list_str_2, 4)
        block_str_2 = random_alphabet_sample_2[0]+random_alphabet_sample_2[1]+random_alphabet_sample_2[2]+random_alphabet_sample_2[3]
        sum_block_2 = sum([weight_coefficient_dictionary[random_alphabet_sample_2[0]],weight_coefficient_dictionary[random_alphabet_sample_2[1]],
            weight_coefficient_dictionary[random_alphabet_sample_2[2]],weight_coefficient_dictionary[random_alphabet_sample_2[3]]])
        return sum_block_2, block_str_2
    
    def block_generator_3():
        alphabet_list_str_3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                            "W", "X", "Y", "Z"]
        
        random_alphabet_sample_3 = random.sample(alphabet_list_str_3, 4)
        block_str_3 = random_alphabet_sample_3[0]+random_alphabet_sample_3[1]+random_alphabet_sample_3[2]+random_alphabet_sample_3[3]
        sum_block_3 = sum([weight_coefficient_dictionary[random_alphabet_sample_3[0]],weight_coefficient_dictionary[random_alphabet_sample_3[1]],
            weight_coefficient_dictionary[random_alphabet_sample_3[2]],weight_coefficient_dictionary[random_alphabet_sample_3[3]]])
        return sum_block_3, block_str_3

    # intervall_genarator() generates my ranmdom sequence intervall and safes it on the variable random_intervall_sequence
    random_intervall_sequence = intervall_generator()

    # Logic behind the loop: I want to check if the sum of our generated blocks is a number in our random_intervall_sequence
    # if yes -> break loop go to the next , if no -> generate a new block 
    while True:
        sum_block_1, block_str_1 = block_generator_1()
        if sum_block_1 in random_intervall_sequence:
            break  # gereration rule true -> end loop
    
    while True:
        sum_block_2, block_str_2 = block_generator_2()
        if sum_block_2 in random_intervall_sequence:
            break  # gereration rule true -> end loop
    
    while True:
        sum_block_3, block_str_3 = block_generator_3()
        if sum_block_3 in random_intervall_sequence:
            break  # gereration rule true -> end loop
    
    # variable for our full key
    full_key = f"{block_str_1}-{block_str_2}-{block_str_3}"
    
    #I have to return a few variables from key_generator() because I need them in the next functions 
    return (
    random_intervall_sequence,
    sum_block_1,
    sum_block_2,
    sum_block_3,
    block_str_1,
    block_str_2,
    block_str_3,
    full_key
)
'''
for me: How does 
'''

def rotate_key_image():
    global angle, pillow_img, key_img_label                  #defining global variables 

    angle += 90                                              #change the rotation angle for the new image 
    key_img_rotaded = pillow_img.rotate(angle)               #rotate pillow image
    photo_rotated = ImageTk.PhotoImage(key_img_rotaded)      #convert our pillow object in an object tkinter can use

    key_img_label.configure(image=photo_rotated)             #safe our tkinter photo object on an label
    key_img_label.image = photo_rotated                      #it's imporant to safe the reference so it doesn't get lost

    # with root.after() we can deside what should happen after a defined time (here 100ms -> animation)
    root.after(100, rotate_key_image)


def button_clicked():
    button_generate_key.config(text="You have found a key!!!!", bg="lightgreen", fg="black", font=("Arial", 12, "bold"), state="disabled")

    #for music integration I had to use pygame functions
    pygame.mixer.music.load("06. Level Complete.mp3")  
    pygame.mixer.music.play()

    #I want to read all previous variables from the function key_generator()
    (
        random_intervall_sequence,
        sum_block_1,
        sum_block_2,
        sum_block_3,
        block_str_1,
        block_str_2,
        block_str_3,
        full_key
    ) = key_generator()


    #shows the random intervall sequence and our correct key
    tk.Label(root, text=f"random intervall sequence: {random_intervall_sequence}", font=("Arial", 12)).place(relx=0.5, y=140, anchor="n")
    tk.Label(root, text=f"your key: {full_key}", font=("Arial", 12)).place(relx=0.5, y=160, anchor="n")

    #just a few extra files to check if the generated key is correct
    tk.Label(root, text=f"Sum Block Check:", font=("Arial", 12)).place(x=120, y=500, anchor="n")
    tk.Label(root, text=f"{block_str_1} = {sum_block_1}", font=("Arial", 12), justify="left").place(x=110, y=520, anchor="n")
    tk.Label(root, text=f"{block_str_2} = {sum_block_2}", font=("Arial", 12), justify="left").place(x=110, y=540, anchor="n")
    tk.Label(root, text=f"{block_str_3} = {sum_block_3}", font=("Arial", 12), justify="left").place(x=110, y=560, anchor="n")

     # open image and load
    global pillow_img, key_img_label
    pillow_img = Image.open("Key.png")                   #Opens the image as an pillow object
    pillow_img = pillow_img.resize((100, 100))           #resize our object
    key_photo = ImageTk.PhotoImage(pillow_img)           #ImageIk.PhotoImage() converts the pillow object into an object that tkinter can use

    # creates an image label under our button 
    key_img_label = tk.Label(root, image=key_photo)      #safe key_photo on a label 
    key_img_label.image = key_photo                      #safe reference
    key_img_label.place(relx=0.5, y=220, anchor="n")

    #after our key image is createtd, we can use our rotete_key_image() function
    rotate_key_image()

    




# creating main window 
root = tk.Tk()
pygame.mixer.init()
root.title("Lab 3, Semester 1")   
root.geometry("800x600")  

# load image and show 
img = Image.open("Super_Mario.png")   
img = img.resize((260, 260))      
photo = ImageTk.PhotoImage(img)

# creates an image label 
img_label = tk.Label(root, image=photo)
img_label.image = photo  # Referenz speichern, sonst wird das Bild gelöscht!
img_label.pack(side= tk.BOTTOM)



# dictionery text
dict_text = """A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
J = 10
K = 11
L = 12
M = 13
N = 14
O = 15
P = 16
Q = 17
R = 18
S = 19
T = 20
U = 21
V = 22
W = 23
X = 24
Y = 25
Z = 26"""

#I want to show the translations of the characters, so everybody can check 
dict_label = tk.Label(root,text=dict_text,font=("Arial", 12),justify="left", bg= "peach puff")
dict_label.place(x=700, y=10)  


# welcome label 
welcome_label = tk.Label(root, text="Hello, this is your key generator!\nPress the Button to find a key", font=("Arial", 14))
welcome_label.place(relx=0.5, y=10, anchor="n")


# button = button_generate_key
button_generate_key = tk.Button(root, text="find key", command=button_clicked, width=30, height=3, bg="yellow", 
    fg="black", font=("Arial", 12, "bold"))                   
button_generate_key.place(relx=0.5, y=60, anchor="n")

# starting our main loop
root.mainloop()
