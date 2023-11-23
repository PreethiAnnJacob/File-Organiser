# Author: Preethi Ann Jacob
# 23.11.2023

# Python Program to organise files using extension

#----------Preliminaries------------

# 1. 	.suffix is from Path module: PurePath.suffix gives the file extension of the final component, if any.
# 2. 	Attributes in entry(a DirEntry object): name, path, inode(), is_dir(), is_file(), is_symlink(), stat()
# 3. 	Syntax: os.makedirs(path, mode = 0o777, exist_ok = False) 
# 		Parameter: 
# 		path: A path-like object representing a file system path. A path-like object is either a string or bytes object representing a path.
# 		mode (optional) : A Integer value representing mode of the newly created directory..If this parameter is omitted then the default value Oo777 is used.
# 		exist_ok (optional) : A default value False is used for this parameter. If the target directory already exists an OSError is raised if its value is False otherwise not. For value True leaves directory unaltered. 
# 		Return Type: This method does not return any value.
				
#---------------------------------------

import os
from pathlib import Path

# Dictionary to map directory to extension
directories_dictionary = {
	"HTML": [".html5", "html", ".htm", ".xhtm"],
	"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".heif", ".psd"],
	"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".qt", ".mpg", ".mpeg", ".3gp"],
	"Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd"],
	"Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
	"Audio": [".aac", ".aa", ".aac", "dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", "oga", ".raw", ".vox", ".wav", ".wma",".opus"],
	"Plaintext": [".txt", ".in", ".out"],
	"PDF": [".pdf"],
	"Python": [".py"],
	"XML": [".xml"],
	"EXE": [".exe"],
	"Shell": [".sh"]
}

# Dictionary to map extension to directory
file_formats_dictionary = {
	file_format: directory
	for directory, file_formats in directories_dictionary.items()
	for file_format in file_formats		
}
# print (file_formats) 
# # {'.html5': 'HTML', 'html': 'HTML', '.htm': 'HTML', '.xhtm': 'HTML', '.jpeg': 'Images', '.jpg': 'Images', '.tiff': 'Images', '.gif': 'Images', '.bmp': 'Images', '.png': 'Images', '.heif': 'Images', '.psd': 'Images', '.avi': 'Videos', '.flv': 'Videos', '.wmv': 'Videos', '.mov': 'Videos', '.mp4': 'Videos', '.webm': 'Videos', '.qt': 'Videos', '.mpg': 'Videos', '.mpeg': 'Videos', '.3gp': 'Videos', '.oxps': 'Documents', '.epub': 'Documents', '.pages': 'Documents', '.docx': 'Documents', '.doc': 'Documents', '.fdf': 'Documents', '.ods': 'Documents', '.odt': 'Documents', '.pwi': 'Documents', '.xsn': 'Documents', '.xps': 'Documents', '.dotx': 'Documents', '.docm': 'Documents', '.dox': 'Documents', '.rvg': 'Documents', '.rtf': 'Documents', '.rtfd': 'Documents', '.a': 'Archives', '.ar': 'Archives', '.cpio': 'Archives', '.iso': 'Archives', '.tar': 'Archives', '.gz': 'Archives', '.rz': 'Archives', '.7z': 'Archives', '.dmg': 'Archives', '.rar': 'Archives', '.xar': 'Archives', '.zip': 'Archives', '.aac': 'Audio', '.aa': 'Audio', 'dvf': 'Audio', '.m4a': 'Audio', '.m4b': 'Audio', '.m4p': 'Audio', '.mp3': 'Audio', '.msv': 'Audio', '.ogg': 'Audio', 'oga': 'Audio', '.raw': 'Audio', '.vox': 'Audio', '.wav': 'Audio', '.wma': 'Audio', '.txt': 'Plaintext', '.in': 'Plaintext', '.out': 'Plaintext', '.pdf': 'PDF', '.py': 'Python', '.xml': 'XML', '.exe': 'EXE', '.sh': 'Shell'}

def organise():
	directory_to_be_organised = "Directory to Organise"
	for entry in os.scandir(directory_to_be_organised):
		# print(entry.name)
		if entry.is_dir():
			continue

		# Both give same result
		# print (entry.path)
		# print (Path(entry)) 
		file_path = Path(entry) # .suffix won't work with entry.pathsuffix but works with Path(entry).suffix 
		file_format = file_path.suffix.lower()

		if file_format in file_formats_dictionary:
			parentDirectoryPath = Path(directory_to_be_organised)
			newOrganisingFolderPath = Path(file_formats_dictionary[file_format]) 
			finalDirectoryPath = parentDirectoryPath.joinpath(newOrganisingFolderPath)
			finalDirectoryPath.mkdir(exist_ok=True)
			fileNamePath = Path(entry.name)
			file_path.rename(finalDirectoryPath.joinpath(fileNamePath))

organise()

