secret_word=''

def GetSecretWord():
    global  secret_word
    secret_word='maccoroni'

def ShowHangMan(failed):
    print(' +-------+')
    if failed==0:
        print('         |' )
    if failed>0:
        print('  O      |' )
    if failed==2:
        print(' / \\     |')
    if failed>2:
        print('/ | \\    |')
    if failed>3:
        print(' / \\     |')




def main():
    GetSecretWord()
    ShowHangMan(0)





if __name__ == "__main__":
    main()


