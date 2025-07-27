import os

class Folder:
    def __init__(self, title, tags):
        self.title = title
        self.tags = tags

    def myFunc(self):
        print(self.title, self.tags)


def Fetch():
    objs = []
    path = 'public'
    folders = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    print(folders)

    for folder in folders:
        title, tags = folder.split(':')
        tags = tags.split('.')
        print(title, tags)

        obj = Folder(title, tags)
        objs.append(obj)

    print(objs)

    return objs

# Fetch()