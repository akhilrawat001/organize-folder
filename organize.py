import os


def check_if_directory_exists(path):
	return os.path.isdir(path)


def create_folder_for_extension(ext=False):
	if not ext:
		dir_name = 'Un-Classified'
	else:
		ext = ext.upper()
		dir_name = ext + '-Files'
	if not check_if_directory_exists(dir_name):
		os.mkdir(dir_name)
	return dir_name


def list_directory_contents():
	return os.listdir()


def get_file_extension(file):
	file_name = file.split('.')
	if len(file_name) > 1:
		return file_name[-1]
	return False


def move_file_to_directory(file, dir_name):
	if check_if_directory_exists(dir_name):
		dest_file_name = dir_name + '/' + file
		print('Moving', file, 'to', dest_file_name)
		os.rename(file, dest_file_name)


def main():
	path = input('Enter the absolute path directory to organize:')
	if not check_if_directory_exists(path):
		print('Invalid Path')
		exit()
	os.chdir(path)
	files_and_folders = list_directory_contents()
	for item in files_and_folders:
		if item[0] == '.':
			print('Skipping', item)
		elif not check_if_directory_exists(item):
			extension = get_file_extension(item)
			dir_name = create_folder_for_extension(extension)
			move_file_to_directory(item, dir_name)


main()
