
# Simple binary converter

print("Text to binary converter.\nPlease type the word you want to convert:")

word = input()
print("\n")

a_byte_array = bytearray(word, "utf8")
byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation)

print("'" + word + "'" + " converted to binary is:\n" + str(byte_list))
