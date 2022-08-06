
# Creating files train.txt and test.txt
# for training in Darknet framework
#
# Algorithm:
# Setting up full paths --> List of paths -->
# --> Extracting 30% of paths to save into test.txt file -->
# --> Writing paths into train and test txt files
#
# Result:
# Files train.txt and test.txt with full paths to images


# Importing needed library
import os


"""
Start of:
Setting up full path to directory with labelled images
"""

# Full or absolute path to the folder with images
# Find it with Py file getting-full-path.py
# Pay attention! If you're using Windows, yours path might looks like:
# r'C:\Users\my_name\Downloads\video-to-annotate'
# or:
# 'C:\\Users\\my_name\\Downloads\\video-to-annotate'
print("Just enter without typing for default")
full_path_to_images = input("Enter Full path to dataset (locations where .jpg and .txt files are stored):\n")


if full_path_to_images == '':
    full_path_to_images = '/content/drive/MyDrive/dataset'
files = os.listdir(full_path_to_images)
# full_path_to_images = input("Enter where you want your train.txt and test.txt files")
# print(files)

train_data = files[:int(len(files)*0.7)]
test_data  = list(set(files) - set(train_data))

print(train_data)
print(test_data)
with open('train.txt', 'w') as train_txt:
    # Going through all elements of the list
    for file in train_data:
        if file.endswith(".jpg") or file.endswith(".png"): 
        # Writing current path at the end of the file
            train_txt.write(full_path_to_images+'/'+file+"\n")

with open('test.txt', 'w') as test_txt:
    # Going through all elements of the list
    for file in test_data:
        if file.endswith(".jpg") or file.endswith(".png"): 
        # Writing current path at the end of the file
            test_txt.write(full_path_to_images+'/'+file+"\n")

exit()


"""
End of:
Setting up full path to directory with labelled images
"""


"""
Start of:
Getting list of full paths to labelled images
"""

# Check point
# Getting the current directory
# print(os.getcwd())

# Changing the current directory
# to one with images
# os.chdir(full_path_to_images)

# # Check point
# # Getting the current directory
# # print(os.getcwd())

# # Defining list to write paths in
# p = []

# # Using os.walk for going through all directories
# # and files in them from the current directory
# # Fullstop in os.walk('.') means the current directory
# for current_dir, dirs, files in os.walk('.'):
#     # Going through all files
#     for f in files:
#         # Checking if filename ends with '.jpeg'
#         if f.endswith('.jpg'):
#             # Preparing path to save into train.txt file
#             # Pay attention!
#             # If you're using Windows, it might need to change
#             # this: + '/' +
#             # to this: + '\' +
#             # or to this: + '\\' +
#             path_to_save_into_txt_files = full_path_to_images + '/' + f

#             # Appending the line into the list
#             # We use here '\n' to move to the next line
#             # when writing lines into txt files
#             p.append(path_to_save_into_txt_files + '\n')


# # Slicing first 15% of elements from the list
# # to write into the test.txt file
# p_test = p[:int(len(p) * 0.15)]

# # Deleting from initial list first 15% of elements
# p = p[int(len(p) * 0.15):]

# """
# End of:
# Getting list of full paths to labelled images
# """


"""
Start of:
Creating train.txt and test.txt files
"""

# Creating file test.txt and writing all validation files location in it 
# with open('test.txt', 'w') as test_txt:
#     # Going through all elements of the list
#     for i in range(1706,1841):
#         # Writing current path at the end of the file
#         test_txt.write(full_path_to_images+"/a"+str(i)+".jpg\n")

"""
End of:
Creating train.txt and test.txt files
"""
