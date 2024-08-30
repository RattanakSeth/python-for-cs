import re

file_path = 'data/segmented_text.txt'

with open(file_path, "r") as file1:
    FileContent = file1.read()
    # print(FileContent)
    file1.close()

# print(FileContent)
entries = re.split(r"\n", FileContent)
print(entries)

def usingSplit():
    count = 0
    entries = FileContent.split()#re.split(r'\n+', FileContent)
    for v in entries:
        if v != '|':
            count = count + 1
    # print(len(entries))
    print(count)


