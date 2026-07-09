file = open(".\\File Manager\\temp.txt", 'r')
content = file.read()
file.close()
print(f"content of the file: {content}")