#Import Libraries
import os
import shutil

file_path = r'D:'

def move_file_by_extension():
	global file_path
	
	print('Old directory ----->>> ',os.getcwd())
	os.chdir(file_path)
	print('Current directory ----->>> ',os.getcwd())

	all_files = os.listdir()

	for filename in all_files:

		if filename.endswith('.txt'):
			if not os.path.exists('Text_Documents'):
				os.mkdir('Text_Documents')
				
			shutil.move(filename, (os.path.join(os.getcwd(),'Text_Documents')))
			print('Text documents moved')

		if filename.endswith('.docx'):
			if not os.path.exists('Word_Documents'):
				os.mkdir('Word_Documents')

			shutil.move(filename, (os.path.join(os.getcwd(),'Word_Documents')))
			print('Word documents moved')

		if filename.endswith('.mp4') or filename.endswith('.MP4') or filename.endswith('.avi') or filename.endswith('.mkv'):
			if not os.path.exists('Videos'):
				os.mkdir('Videos')

			shutil.move(filename, (os.path.join(os.getcwd(),'Videos')))
			print('Videos moved')

		if filename.endswith('.png') or filename.endswith('.jpg'):
			if not os.path.exists('Images'):
				os.mkdir('Images')

			shutil.move(filename, (os.path.join(os.getcwd(),'Images')))
			print('Images moved')

		if filename.endswith('.xlsx'):
			if not os.path.exists('Excel_Documents'):
				os.mkdir('Excel_Documents')

			shutil.move(filename, (os.path.join(os.getcwd(),'Excel_Documents')))
			print('Excel documents moved')

		if filename.endswith('.zip'):
			if not os.path.exists('Zip_files'):
				os.mkdir('Zip_files')

			shutil.move(filename, (os.path.join(os.getcwd(),'Zip_files')))
			print('Zip files moved')

		if filename.endswith('.ipynb'):
			if not os.path.exists('Jupyter_Notes'):
				os.mkdir('Jupyter_Notes')

			shutil.move(filename, (os.path.join(os.getcwd(), 'Jupyter_Notes')))
			print('Jupyter Notes moved')

		if filename.endswith('.pdf'):
			if not os.path.exists('PDF_Documents'):
				os.mkdir('PDF_Documents')

			shutil.move(filename, (os.path.join(os.getcwd(),'PDF_Documents')))
			print('PDF documents moved')

		if filename.endswith('.csv'):
			if not os.path.exists('Csv_Documents'):
				os.mkdir('Csv_Documents')

			shutil.move(filename, (os.path.join(os.getcwd(),'Csv_Documents')))
			print('csv documents moved')

		if filename.endswith('.json'):
			if not os.path.exists('Json_Documents'):
				os.mkdir('Json_Documents')

			shutil.move(filename, (os.path.join(os.getcwd(),'Json_Documents')))
			print('json documents moved')

		if filename.endswith('.py'):
			if not os.path.exists('Python_Files'):
				os.mkdir('Python_Files')
			shutil.move(filename, (os.path.join(os.getcwd(),'Python_Files')))
			print('python files moved')

		if filename.endswith('.exe'):
			if not os.path.exists('Softwares'):
				os.mkdir('Softwares')

			shutil.move(filename, (os.path.join(os.getcwd(),'Softwares')))

move_file_by_extension()
