# Example message
message = "This is a secret message."
# Convert message to integer
message_int = int(binascii.hexlify(message.encode('utf-8')), 16)

# Encrypt the message using RSA
encrypted_message = pow(message_int, e, p * q)

print(f"Original message (int): {message_int}")
print(f"Encrypted message (int): {encrypted_message}")