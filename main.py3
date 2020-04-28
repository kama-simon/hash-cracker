from urllib.request import urlopen, hashlib # to open files from a remote URL and hash pw guesses into SHA-1
usrhash = input('Insert hask to crack: ');
LIST_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
for guess in LIST_PASSWORDS.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest();
    if usrhash == hashedGuess:
        print('The password is ', str(guess));
        quit();
    elif usrhash != hashedGuess:
        print('Password guess ', str(guess), ' does not match, trying next...');
print('Password not in library, darnnit');