import encryption
import os, sys, random

strings_protected = 0

meme = ['njRat', 'Robert Private String Encryptor', 'Gl unpacking this', 'is that a ransomware?', 'send me nudes', 'is that a joke?', 'hi gay im dad', 'Redirecting to pornhub', 'stealing your data lol']

try:
    main_file = (sys.argv[1])
    if ((sys.argv[1].split('\\')[-1]))[-3:] == ".py":
        pass
    else:
        print('Make sure this file in made in python and contain extension .py')
        input()
        os._exit(0)
except:
    print('Drag and drop file that you want to protect')
    input()
    os._exit(0)
second_file = (sys.argv[1].split('\\')[-1]).replace('.py', '')
lol = 0
with open(main_file, "r") as m:
    with open(second_file+"_protected.py", "w") as n:
        n.write('import encryption\n')
        for a in m:
            lol += 1
            try:
                if '"""' in a or "'''" in a:
                    n.write(a)
                else:
                    l1x = ['f"', 'b"', 'u"', 'r"', 'fr"', 'rf"', 'fr"', 'rb"', 'br"', "f'", "b'", "u'", "r'", "fr'", "rf'", "fr'", "rb'", "br'"]
                    if any(n in a for n in l1x):
                        n.write(a)
                    else:
                        if a.count('"') == 0:
                            if a.count("'") == 0:
                                n.write(a)
                            else:
                                l = {}
                                for each in range(int(a.count("'")) // 2):
                                    if each == 0:
                                        b = a.split("'")[each+1]
                                        strings_protected += 1
                                    else:
                                        if (each % 2) == 0:
                                            b = a.split("'")[each+1]
                                        else:
                                            b = a.split("'")[each+2]
                                        strings_protected += 1
                                    p = encryption.encryptor().encrypt(b, {random.choice(range(0, 999999))}, {random.choice(meme)})
                                    l[f"'{b}'"] = f'encryption.encryptor().decrypt("{p}", {random.choice(range(0, 999999))}, " {random.choice(meme)}")'
                                    print(f'[INFO] Protected line number {lol}')
                                    
                                for each in l:
                                    a = a.replace(f'{each}', f'{l[each]}')
                                n.write(a)
                        else:
                            l = {}
                            for each in range(int(a.count('"')) // 2):
                                if each == 0:
                                    b = a.split('"')[each+1]
                                    strings_protected += 1
                                else:
                                    if (each % 2) == 0:
                                        b = a.split('"')[each+1]
                                    else:
                                        b = a.split('"')[each+2]
                                    strings_protected += 1
                                p = encryption.encryptor().encrypt(b, {random.choice(range(0, 999999))}, {random.choice(meme)})
                                l[f'"{b}"'] = f"encryption.encryptor().decrypt('{p}', {random.choice(range(0, 999999))}, '{random.choice(meme)}')"
                                print(f'[INFO] Protected line number {lol}')
                                
                            for each in l:
                                a = a.replace(f'{each}', f'{l[each]}')
                            n.write(a)
                        
            except Exception as e:
                print(e)
                n.write(a)
print('Protected {0} strings'.format(strings_protected))
print(f'File saved as: {second_file+"_protected.py"}')
print('Done')
input()
os._exit(0)