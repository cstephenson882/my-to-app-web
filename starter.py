import os
import requests
import Add_http_images


# Specify the destination folder
def make_dest_folder(destination_folder ):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

def add_needed_files(destination_folder = 'gui_files/images'):
    todo_file_location = 'gui_files/'
    if not os.path.exists(todo_file_location):
        make_dest_folder(todo_file_location)
        if not os.path.exists(f"{todo_file_location}toDos.txt",):
            with open(f"{todo_file_location}toDos.txt", 'w') as file1:
                pass

    if not os.path.exists(destination_folder):
        make_dest_folder(destination_folder)
        Add_http_images.download_image('https://i.ibb.co/C0zJf4X/pencil.png',destination_folder)
        Add_http_images.download_image('https://i.ibb.co/yRQY96m/complete.png', destination_folder)
        Add_http_images.download_image('https://i.ibb.co/sVYQMH2/add.png', destination_folder)

add_needed_files()