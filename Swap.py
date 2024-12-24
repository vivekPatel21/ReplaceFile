#goal, we need to replace the claw image with another one and change the item description.
#There is an image that I am uploading on Github here, and I need to save the claw.png file, 
#and then I need to replace it with the custom png off of Github.

import os
import shutil
import requests

def replace_claw_image(github_url, target_path, new_description):
    """
    Replace the claw image and update the item description.

    Parameters:
        github_url (str): URL to the custom image on GitHub.
        target_path (str): Path to the directory containing the claw image.
        new_description (str): New description for the item.
    """

    Path = "Hollow Knight\hollow_knight_Data\Managed\Mods\Custom Knight\Skins\Default\Inventory"

    # Define paths
    claw_image_path = os.path.join(target_path, "claw.png")
    backup_path = os.path.join(target_path, "claw_backup.png")

    try:
        # Step 1: Backup the current claw image
        if os.path.exists(claw_image_path):
            shutil.copy(claw_image_path, backup_path)
            print("Backup created for the original claw image.")

        # Step 2: Download the custom image from GitHub
        response = requests.get(github_url, stream=True)
        if response.status_code == 200:
            with open(claw_image_path, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
            print("Custom image downloaded and replaced successfully.")
        else:
            print(f"Failed to download the custom image. Status code: {response.status_code}")
            return

        # Step 3: Update the item description
        description_file_path = os.path.join(target_path, "description.txt")
        with open(description_file_path, 'w') as desc_file:
            desc_file.write(new_description)
        print("Item description updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage 
github_image_url = "https://raw.githubusercontent.com/your-repo-path/claw.png"
target_directory = r"Hollow Knight\hollow_knight_Data\Managed\Mods\Custom Knight\Skins\Default\Inventory"
new_item_description = "This claw is custom-made for precision and style."

replace_claw_image(github_image_url, target_directory, new_item_description)
