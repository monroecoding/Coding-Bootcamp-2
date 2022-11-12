"""
Coding Bootcamp at the Monroe Township Library

Class 5 Project

A 'Caesar Cipher' is a simple type of encryption that shifts the letters of a message
forward across the alphabet using a specific key
For example, 'hello' shifted with a key of 3, would become 'khoor'

Write a program that can encrypt or decrypt a message using the Caesar cipher
The main program will ask the user to input a message and either encrypt or decrypt that message

Complete the encypt() and decrypt() functions
Both functions will accept a message as an argument, decrypt() takes a key argument also
Each character of the message should be shifted forward (encryption) or backward (decryption)
by the value of the key

Things to remember:
    - For simplicity, all messages will be converted to uppercase in the main() function before being passed as arguments
    - Make sure your program can account for messages with numbers or non-alpha characters
    - the ALPHABET constant is just a string containing all uppercase letters of the alphabet in order
        -this can be used to find each letter's index in the alphabet a=0, b=1, c=2, etc.
    - You will need to implement 'wrapping'; any shift that goes beyond the end of the alphabet should wrap
        back to the beginning ('z' shifted with a key of 3 would become 'c')
    - If you want to test your functions individually, you can comment out the 'if name == main' block
        and just call them with test arguments
"""


import string
import random

ALPHABET = string.ascii_uppercase #string containing all letters in the alphabet


#complete this function
def encrypt(message):
    """
    message {str} -- a message in all caps, to be encrypted

    prints encoded message, as well as the key used for encryption
    """

    key = random.randint(1,25)
    encrypted = ""

    #your code goes here!

    print(f"Encrypted message: {encrypted}\nKey used: {key}")
    

#complete this function
def decrypt(message, key):
    """
    message {str} -- an encrypted message in all caps, to be decrypted
    key {int} -- number of letters to shift for decryption

    prints decoded message
    """
    
    decrypted = ""

    #your code goes here!

    print(f"Decrypted message: {decrypted}")


def main():
    """
    accepts user input, allowing for either encryption or decryption of messages
    """

    print("Caesar Cipher")
    print("------")

    while True:
        answer = input("Are you (e)ncrypting or (d)ecrypting?: ").lower()

        if answer == "e":
            message = input("Enter your message: ").upper()
            encrypt(message)
            break
        
        elif answer == "d":
            message = input("Enter your message: ").upper()
            key = int(input("Enter the key (0-25): "))
            if 0 <= key < 26:
                decrypt(message, key)
                break


if __name__ == "__main__":
    main()