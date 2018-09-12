import os
import numpy as np
import tkinter as tk
import scipy.fftpack
from scipy.fftpack import dct
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from tkinter import filedialog
from PIL import Image, ImageTk

############ 2 Dimensions DCT function ############
def dct2_library(my_matrix):
    dct2_matrix = scipy.fftpack.dct(scipy.fftpack.dct(my_matrix.T, norm = 'ortho').T, norm = 'ortho')
    return dct2_matrix
############ ############ ############ ############

############ 2 Dimensions IDCT function ############
def idct2_library(my_matrix):
    idct2_matrix = scipy.fftpack.idct(scipy.fftpack.idct(my_matrix.T, norm = 'ortho').T, norm = 'ortho')
    return idct2_matrix
############ ############ ############ ############

############ Frequency Filtering ############
def frequency_filtering():
    print("Frequency filtering process started..")
    img_matrix =  np.array(Image.open(root.filename))
    #print(img_matrix)
    if(len(img_matrix.shape) > 2):
        img_matrix = img_matrix[:,:,0]
    dct_matrix = dct2_library(img_matrix)
    # Frequency threshold: value within 0 and N+M-2
    d = int(parameter_1.get())
    R,C = dct_matrix.shape
    if(d<0):
        print("The parameter 'd' can't be negative, assumed as 0."); d = 0
    elif(d > R+C-2):
        print("The parameter 'd' can't be higher than ",R+C-2,", assumed as ", R+C-2); d = R+C-2

    # Coefficient
    beta_coeff = float(parameter_2.get())
    R,C = dct_matrix.shape
    for i in range(0,R):
        for j in range(0,C):
            if(i+j >= d):
                dct_matrix[i,j] = dct_matrix[i,j]*beta_coeff
    idct_matrix = idct2_library(dct_matrix)

    # Cast all the idct_matrix values to integer
    # Substitute all the negative values with 0 and all the values above 255 with 255
    idct_matrix[idct_matrix < 0] = 0
    idct_matrix[idct_matrix > 255] = 255
    numbers_matrix = np.array(idct_matrix.astype(np.uint8)).reshape(R,C)
    # Converting the numbers matrix back to the Image format.
    elab_photo = Image.fromarray(numbers_matrix)
    # Saving the elaborated image
    name_saved_pic = str("Elaborated_Photos/Elab_"+"d="+str(parameter_1.get())+"_beta="+str(parameter_2.get())+"_"+os.path.basename(root.filename))
    plt.imsave(name_saved_pic, elab_photo, cmap = cm.gray)
    # Uploading the elaborated image and displaying it on the GUI frame
    elab_photo = Image.open(name_saved_pic); N, M = elab_photo.size
    elab_photo = ImageTk.PhotoImage(elab_photo.resize((450, 450), Image.ANTIALIAS))
    # Updating the elaborated picture on the GUI frame with the new one
    elab_img.config(image=elab_photo); elab_img.image = elab_photo
    # Updating the elaborated picture label on the GUI frame
    label_elab_img_descr.config(text="Elaborated image("+str(N)+"x"+str(M)+")")
    print("Frequency filtering process successfully terminated!\n")
############ ############ ############ ############

############ Frequency Filtering ############
def file_selection():
    print("User is selecting a picture..")
    # Function that allow the user to select an arbitrary file from the computer
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/Andrea/Desktop/Progetto MCS - Consegna/Progetto2/Part_2/Original_Photos",title = "Select file",filetypes = (("bmp files","*.bmp"), ("jpeg files","*.jpg")))
    # Converting the selected file to Image format and resize it.
    original_pic = Image.open(root.filename)
    N, M = original_pic.size; Max_d = N+M-2
    original_pic = original_pic.resize((450, 450), Image.ANTIALIAS)
    original_photo = ImageTk.PhotoImage(original_pic)
    # Displaying the selected picture on the GUI frame
    original_img.config(image=original_photo)
    original_img.image = original_photo
    label_note1.config(text=" Note that 'd' has to be between 0 and N+M-2, in this case: 0 <= d <= "+str(Max_d)+"")
    label_orig_img_descr.config(text="Original image("+str(N)+"x"+str(M)+")")
    print("Picture has been selected and uploaded!\n")

############ ############ ############ ############


###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######

# Create the main window
print("Building the GUI interface..")
root = tk.Tk()
root.title("GUI Interface - Frequencies Manipulation")

# Set the original image label and initialize it to "no_img"
original_pic = Image.open(r"Original_Photos/no_img.png")
original_pic = original_pic.resize((450, 450), Image.ANTIALIAS)
original_photo = ImageTk.PhotoImage(original_pic)

# Set the elaborted image label and initialize it to "no_img"
elab_pic = Image.open(r"Original_Photos/no_img.png")
elab_pic = elab_pic.resize((450, 450), Image.ANTIALIAS)
elab_photo = ImageTk.PhotoImage(elab_pic)

# Set the entry for the first parameter
var1_descr = " Enter 'd' parameter input: " ; label_descr1 = tk.Label(root, text=var1_descr)
var1_note = " Note that 'd' has to be between 0 and N+M-2 " ; label_note1 = tk.Label(root, text=var1_note)
parameter_1 = tk.Entry(root)

var2_descr = " Enter 'beta' parameter input: "
label_descr2 = tk.Label(root, text=var2_descr)
parameter_2 = tk.Entry(root)

# Images viewer
orig_img_descr = " Original image" ; label_orig_img_descr = tk.Label(root, text=orig_img_descr)
elab_img_descr = " Elaborated image " ; label_elab_img_descr = tk.Label(root, text=elab_img_descr)

original_img = tk.Label(root, image=original_photo)
elab_img = tk.Label(root, image=elab_photo)

# Create the buttons
convert = tk.Button(root, text = "Convert", command = frequency_filtering)
filename_selection = tk.Button(root, text = "Select input image", command = file_selection)

# Grid is used to add the widgets to root
# Alternatives are Pack and Place
label_descr1.grid(row = 0, column = 1)
parameter_1.grid(row = 1, column = 1)
label_note1.grid(row = 1, column = 2)

label_descr2.grid(row = 2, column = 1)
parameter_2.grid(row =3, column = 1)
filename_selection.grid(row = 4, column = 1)
label_orig_img_descr.grid(row = 5, column = 0)
label_elab_img_descr.grid(row = 5, column = 2)
original_img.grid(row = 6, column = 0)
convert.grid(row = 6, column = 1)
elab_img.grid(row = 6, column = 2)

print("GUI Interface is ready!\n")
root.mainloop()
