def encode(message, shift):
   print("This is the encode function")

def decode():
   print("This is the decode function")

def main():
   print("Welcome to the Caesar Cipher!")
   while True:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      message = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      if direction == "encode":
         encode(message, shift)
         break
      elif direction == "decode":
         decode(message, shift)
         break
      else:
         print("Invalid input")

if __name__ == "__main__":
   main()