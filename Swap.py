import os
import shutil
# Don't spoil the surprise
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
## Please?
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
## I am begging
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
##
#
#
## Fine I guess
#
#
#

def replace_file_with_png(target_file_path, png_file_path):
    """
    Replaces the target file with a PNG file, overwriting the original file or creating it if missing.

    Args:
        target_file_path (str): Path to the file to be replaced or created.
        png_file_path (str): Path to the PNG file that will replace or create the target file.

    Returns:
        str: Message indicating the operation result.
    """
    try:
        # Ensure the PNG file exists
        if not os.path.exists(png_file_path):
            return f"Error: The PNG file does not exist at {png_file_path}."

        # Create target directory if it does not exist
        #target_dir = os.path.dirname(target_file_path)
        #if not os.path.exists(target_dir):
        #    os.makedirs(target_dir)

        # Copy the PNG file to the target path
        shutil.copyfile(png_file_path, target_file_path)
        return f"The file has been successfully replaced."
    except Exception as e:
        return f"An error occurred: {e}"

target_file = os.path.join(
    "hollow_knight_Data", "Managed", "Mods", 
    "Custom Knight", "Skins", "Default", 
    "Inventory", "claw.png"
)
png_file = os.path.join(
    "maze", "F3", "F66", "F111", "Claw.png"
)


result = replace_file_with_png(target_file, png_file)
print(result)