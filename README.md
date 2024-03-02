# RSA encyption software

## Overview
RSA encyption algorithm for fun

## Features
- Encrypts messages by using pre-existing keys or by generating new keys from two prime numbers
- Decrypts messages with the private keys 

## Prerequisites
Python 3.12.0

## Installation

### Python and pip
Ensure you have the correct version of Python installed. You can download Python [here](https://www.python.org/downloads/) which includes pip.

To check your Python version:
```bash
python3 --version
```


## Setting up the project
1. Clone the repository
2. Navigate to the project directory


## Running the application
1. Navigate to the project directory
2. Run the following command:
python3 main.py

##### Disclaimer: This RSA encryption program is intended just for fun. It is designed to demonstrate the principles of RSA cryptography and should not be used for actual secure communication or data protection.

## Usage

- Choose if you want to encrypt a message or decrypt an allready encrypted message

Encrypting:
- If you chose encryption, you have the choice between using pre-calculated keys or generating new keys. (Note: larger prime numbers are safer, however using numbers which are actually long enough might take a long time)
- Save the public and private keys for yourself somewhere safe
- Type in a message with the allowed characters

Decrypting:
- Enter in a encrypted message (messages encrypted with an other RSA-algorithm might not work, since the order and allowed character list length affects the encryption)
- Enter your private keys


## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

Copyright (c) 2024 - present, aili-li (https://github.com/aili-li)

Remember to give credit if you use this project in your own work.