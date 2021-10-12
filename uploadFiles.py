import dropbox
for root,dirs,files in os.walk(file_from):
    relative_path - os.path.relpath(local_path,file_from)
    dropbox_path = os.path.join(file_to,relative_path)

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
       
    def upload_file(self, local_path, dropbox_path,file_from,file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'WfjVCodI1mMAAAAAAAAAAWdnlAyzTymrREtdE3mG36cd_j7qnS1OjMgZJlDkKuU1'
    transferData = TransferData(access_token)

    file_from = input("Enter the file name to transfer")
    file_to = input("Enter the full path to upload to dropbox:  ")  

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()