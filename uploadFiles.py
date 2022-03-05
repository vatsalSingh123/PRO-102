import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BDOppF7Rb7c97upYclYau5bXB3nJtFBL5-5tnnrR6GN1V4anQIZNIkNkdX02YF7PxXvqVKu2aUwEIBTxB5fBf-QG07ASUCNeOzeaicrr11MrLaYL8BrAMr89NAasTBNwbBBFv2A'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/Great Son/Desktop/P-102/test.txt'
    file_to ='https://www.dropbox.com/home'
    transferData.upload_file(file_from,file_to)
    print('file has been uploaded')

main()  