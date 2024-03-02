from src.rsa_encryption import number_asker, get_keys, encrypt, decrypt

def again_asker():
    while True:
        choice = input('Do you want to run the program again? (y/n): ').lower()
        if choice == 'n':
            return False
        elif choice == 'y':
            return True
        else:
            print('Invalid choice. Please try again.')


# main program
def run():

    run_program = True

    while run_program:

        print('RSA encryption and decryption program\n')

        characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '<', '>', '(', ')', '.', ',', ':', '?', '!']

        choice = input('Do you want to encrypt or decrypt? (e/d): ')
        print()

    # encryption
        if choice == 'e':

            choice2 = input('Do you want to use allready existing keys or generate new ones? (e/g): ')
            print()

            # generate new keys
            if choice2 == 'g':
                p, q = number_asker()
                n = p * q
                phi = (p - 1) * (q - 1)
                e, d = get_keys(phi)

                print(f'Public key: (e={e}, n={n})')
                print(f'Private key: (d={d}, n={n})\n')

            # use existing keys
            elif choice2 == 'e':
                e = int(input('Give the public key e: '))
                n = int(input('Give the public key n: '))
                print()


            while True:
                message = input('Give the message to be encrypted (allowed characters A-Ö, a-ö, 0-9, <>().,:?! and space): ')
                if all(ch in characters for ch in message):
                    print()
                    break

            # encrypts the message and prints the encrypted message
            encrypted_message = encrypt(message, e, n, characters)
            print(f'Your encrypted message is: {encrypted_message}\n')

            run_program = again_asker()
            print()

    # decryption
        elif choice == 'd':

            encrypted_message = input('Give the encrypted message to be decrypted: ').strip()
            print()

            print('Give your private key (d and n)')
            d = int(input('d: '))
            n = int(input('n: '))
            print()

            # decrypts the message and prints the decrypted message
            decrypted_message = decrypt(encrypted_message, d, n, characters)
            print(f'Your decrypted message is: {decrypted_message}\n')

            run_program = again_asker()
            print()