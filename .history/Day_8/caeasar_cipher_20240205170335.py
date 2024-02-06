def encode():
   pass # This is a placeholder

def decode():
   pass  # This is a placeholder

def main():
   print("Welcome to the Caesar Cipher!")
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))

   if direction == "encode":
      encode(text, shift)
   elif direction == "decode":
      decode(text, shift)
   else:
      print("Invalid input")

if __name__ == "__main__":
   main()