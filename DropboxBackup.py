import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, origin, destination):
        dbx = dropbox.Dropbox(self.accessToken)

        with open(origin, 'rb') as f:
            dbx.files_upload(f.read(), destination)

def main():
    accessToken = 'JoFLlxHih0sAAAAAAAAAAWeqM1lQOXjDkjSWHeoOjH8t9Sq7L2qRbBvxOA51L3GL'
    transferData = TransferData(accessToken)

    origin = input("enter origin file: ")
    destination = input("enter file destination location: ")

    transferData.uploadFiles(origin, destination)

    print("File has been moved")

print(__name__)
main()