import os

def displayFiles(filepath):
    if os.path.isfile(filepath):
        print('File name: ' + filepath)
        print(open(filepath).read())
    elif os.path.isdir(filepath):
        print('Directory name: ' + filepath)
        for dir, subdir, files in os.walk(filepath):
            for item in files:
                displayFiles(filepath + '/' + item)
    else:
        print('Big trouble')

displayFiles('/Users/family/test')
