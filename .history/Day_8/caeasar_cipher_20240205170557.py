def encode():
   pass # This is a placeholder

def decode():
   pass  # This is a placeholder

def main():
   print("Welcome to the Caesar Cipher!")
   while True:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      if direction == "encode":
         encode()
         break
      elif direction == "decode":
         decode()
         break
      else:
         print("Invalid input")

if __name__ == "__main__":
   main()