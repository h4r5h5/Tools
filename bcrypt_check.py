print("""
          -Bcrypt Hash Cracker-
           --------     --------                  
            --------     --------        
             ---------------------     
              ---------------------   
               --------     --------     
                --------     --------   
                 -Bcrypt Hash Cracker-
                 
                 
                 """)
import bcrypt
import signal
import progressbar
import getopt
import sys
def signal_handler(sig, frame):
    print('''
----------------------------------------------------------
        Tool Terminated - Bcrypt Hash Cracker
----------------------------------------------------------
    ''')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

argv = sys.argv[1:]

try:
    
    opts, args = getopt.getopt(argv, 'h:w:', ['foperand', 'soperand'])
    
    for opt, arg in opts:
        try:
            hashed_bcrypt = opts[0][1]
            wordlist_path = opts[1][1]
        except IndexError:
            print (' usage: bcrypt-cracker.py -h <hash> -w <wordlist-path>')
            print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
            sys.exit(0)
        
except getopt.GetoptError:
    print (' usage: bcrypt-cracker.py -h <hash> -w <wordlist-path>')
    print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
    sys.exit(2)
try:
    hashed_bcrypt
    wordlist_path
except NameError:
    print (' usage: bcrypt-cracker.py -h <hash> -w <wordlist-path>')
    print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
    sys.exit(2)
else:
    
    hash = hashed_bcrypt.encode('utf8')
    wordlist=wordlist_path
    try:
        n_words = len(list(open(wordlist, "r", encoding="utf-8")))
    except FileNotFoundError:
        print ('\n Error: Incorrect Wordlist Path')
        print (' usage: bcrypt-cracker.py -h <hash> -w <wordlist-path>')
        print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
        sys.exit(2)
    else:
       
        print(" Total passwords:", n_words)
        print(" Setting up \n Wait......")
        wordlists_pass = open(wordlist, "r", encoding="utf-8").readlines()
        wordlists_pass = wordlists_pass
        new_list=[]
        for k in wordlists_pass:
            wordlists_pass_replace = k.replace("b'","").replace("\n","").encode('utf8')
            new_list.append(wordlists_pass_replace)
        print(" Starting the Attack")
        total_len=int(len(new_list)-1)
        def animated_marker():
            widgets = [' Craking Hash: ', progressbar.AnimatedMarker(), '                          Total:[', progressbar.SimpleProgress(), ']',  ' (', progressbar.ETA(), ') ',]
            bar = progressbar.ProgressBar(widgets=widgets, maxval=len(new_list)).start()
            for i in range(0, len(new_list)):
                isSamePassword = bcrypt.checkpw(new_list[i],hash)
                if isSamePassword == False:
                    bar.update(i)
                    if i == total_len:
                        print("\n\n Sorry:Unable to Crack Hash with This Wordlist")
                        print(" Tip: Try Another Wordlist")
                        print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
                        
                else:
                    print("\n Woooh Hash cracked \n Password is:",new_list[i])
                    print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
                    sys.exit(0)
                    break


        animated_marker()