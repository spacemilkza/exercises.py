import os

items = os.listdir()
files = []
for x in items:
    if os.path.isfile(f"./{x}"):
        files.append(x)
filesToMove = []
start = 2008

while start != 2024:
    for x in files: #search files of specific year
        if str(start) in x:
            if filesToMove.append(x): #cut and paste 
                del files[x]

    if len(filesToMove) != 0: #move files to dir
        os.mkdir(str(start))
        for x in filesToMove:
            os.rename(x, f"./{start}/{x}")
        filesToMove.clear()
    start += 1
