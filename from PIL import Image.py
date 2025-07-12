from PIL import Image

def encrypt_image(path, key):
    img = Image.open(path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Apply XOR with key to encrypt
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save("encrypted.png")
    print("Image encrypted and saved as encrypted.png")

def decrypt_image(path, key):
    encrypt_image(path, key)  # XOR again decrypts

# === User Interface ===
print("1: Encrypt Image")
print("2: Decrypt Image")
choice = input("Enter choice: ")
path = input("Enter image path (e.g. image.jpg): ")
key = int(input("Enter secret key (number): "))

if choice == '1':
    encrypt_image(path, key)
elif choice == '2':
    decrypt_image(path, key)
else:
    print("Invalid choice.")

