import cv2
import os

# Read the image
img = cv2.imread('mypic.jpg')

# Get the secret message and password from the user
secret_message = input("Enter secret message: ")
password = input("Enter password: ")

# Create dictionaries for character-to-integer and integer-to-character mapping
char_to_int = {chr(i): i for i in range(255)}
int_to_char = {i: chr(i) for i in range(255)}

# Initialize variables for encryption
current_row, current_channel = 0, 0

# Encryption process
for char in secret_message:
    img[current_row, current_channel, current_channel] = char_to_int[char]
    current_row += 1
    current_channel = (current_channel + 1) % 3

# Save the encrypted image
cv2.imwrite("EncryptedMsg.jpg", img)
os.system("start EncryptedMsg.jpg")

# Initialize variables for decryption
current_row, current_channel = 0, 0
decrypted_message = ""

# Get the passcode for decryption
decryption_passcode = input("Enter passcode for Decryption: ")

# Check if the provided password matches the original password
if decryption_passcode == password:
    # Decryption process
    for _ in range(len(secret_message)):
        decrypted_message += int_to_char[img[current_row, current_channel, current_channel]]
        current_row += 1
        current_channel = (current_channel + 1) % 3

    # Display the decrypted message
    print("Decrypted message:", decrypted_message)
else:
    print("Not a valid key.")