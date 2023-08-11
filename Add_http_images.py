import os
import requests

# URL of the PNG image you want to download
def download_image(image_url,destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Get the filename from the URL
    filename = os.path.join(destination_folder, os.path.basename(image_url))

    # Download the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        """print(f"Image downloaded and saved as '{filename}'")
    else:
        print(f"Failed to download image from '{image_url}'")"""

