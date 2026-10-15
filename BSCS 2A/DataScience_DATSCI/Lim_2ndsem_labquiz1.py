import numpy as np
print("[DATE: 10/14/26]" + "\nNUMPY VER: " + np.__version__)

# INSTRUCTIONS:
# a to m is array1
# n to z is array2
# zip the 2 arrays, giving (a,n), (b,o), etc
# replace all vowels with !,#,$,%,&
# encrypt is changed, while decrypt is plain text

np1 = np.array(['a', 'b', 'c','d', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm'])
np2 = np.array(['n', 'o', 'p','q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z'])

zipped = zip(np1, np2)

np1_unzipped, np2_unzipped = zip(*zipped)

while True:
    user_input = (input("ENTER TEXT: "))
    if not user_input:
        print("ERROR: Please input something.")
        continue
    else:
        break
choice = input("Enter E to Encrypt or D to Decrypt: ").lower()

while True:
    if choice == 'e':
        print("ENCRYPTING...")
        # encryption encyclopedia
        for x, y in np.nditer([np1_unzipped, np2_unzipped]):
            if x[0]: #a
                x = "!"
            elif x[4]: #e
                x = "#"
            elif x[8]: #i
                x = "$"
            elif y[1]: #o
                x = "%"
            elif y[8]: #u
                x = "&"
            else:
                x = y

        # now um, making text input match the np.nditer
        # itd be like, if text has np1, converts into np2 + vowel logic
        # now i just need to seperate the words in text

        break
    elif choice == 'd':
        print("DECRYPTING...")
        break
    else:
        print("ERROR: Choice out of bounds. Retry.")
        continue

