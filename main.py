alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("""
  ____    _    _____ ____    _    ____     ____ ___ ____  _   _ _____ ____  
 / ___|  / \  | ____/ ___|  / \  |  _ \   / ___|_ _|  _ \| | | | ____|  _ \ 
| |     / _ \ |  _| \___ \ / _ \ | |_) | | |    | || |_) | |_| |  _| | |_) |
| |___ / ___ \| |___ ___) / ___ \|  _ <  | |___ | ||  __/|  _  | |___|  _ < 
 \____/_/   \_\_____|____/_/   \_\_| \_\  \____|___|_|   |_| |_|_____|_| \_\
""")

def CC(opt, text, sn):
    ctext = ""
    for l in text:
        if l in alphabet:
            post = alphabet.index(l)
            if opt == "encode":
                shiftedl = alphabet[post+sn]
            elif opt == "decode":
                shiftedl = alphabet[post-sn]
            ctext += shiftedl
        if l not in alphabet:
            ctext += l
    print(f"Your {choice}d text is: {ctext}")

endpg = False
while not endpg:
    choice = input("Type 'encode'to encrypt or type 'decode' to decrypt:\n").lower()
    mg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= 45:
        shift %= 24
        
    CC(choice, mg, shift)

    fchoice = input("Type 'yes' if you wanna go again or 'no' if you want to quit.\n").lower()
    if fchoice == "no":
        endpg = True
        print("Goodbye")
