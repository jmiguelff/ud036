import os
from string import digits

def rename_files():
	file_list = os.listdir(r"C:\Users\JFerreira\Projects\Udacity\ud036\prank")
	saved_path = os.getcwd()
	os.chdir(r"C:\Users\JFerreira\Projects\Udacity\ud036\prank")

	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, digits))

	os.chdir(saved_path)

rename_files()

print(os.listdir(r"C:\Users\JFerreira\Projects\Udacity\ud036\prank"))