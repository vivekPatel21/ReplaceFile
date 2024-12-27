import os
import shutil

#This entire file will reset the state of the changed item, when you run it.
#The maze keeps a copy of the changed item.

#We get rid of the old image, and replace it with the original.
def repair(file_Path, image_path):
    try:
        if not os.path.exists(file_path):
            return "Error: The file does not exist"
        if not os.path.exists(image_path):
            return "Error: The image does not exist"
        shutil.copyfile(image_path,file)
        return "Success"
    except Exception as e:
        return f"error occurred during repair: {e}"


file_Path = "Hollow Knight\hollow_knight_Data\Managed\Mods\Custom Knight\Skins\Default\Inventory\claw.png"
img_Path = "maze\F5\F22\F33\claw.png"
repair(file_Path, img_Path)