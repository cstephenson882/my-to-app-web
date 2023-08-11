import os
import starter
def readToDO(filepath='gui_files/toDos.txt'):
	if not os.path.exists(filepath):
		with open(filepath, 'w') as file:
			pass
	with open(filepath, 'r') as file:
		toDos = file.readlines()
		return toDos
def writeToDo(toDos,filepath = 'gui_files/toDos.txt'):
	with open(filepath, 'w') as file:
		file.writelines(toDos)

if __name__ == '__main__':
	print ( f'Now running "functions" ')