import sys
import json

try:
    with open('morse_codes.json', mode='r', encoding='UTF-8') as f:
        morse_codes = json.load(f)

    user_input = input("\n[*] Enter your message: ")
    morse_chars = ""
    for char in user_input.strip():
        if char.upper() in morse_codes.keys():
            morse_chars += f" {morse_codes.get(char.upper())}"
    print(f"\n[+] Original Text: {user_input}")
    print(f"[+] Morse Codes: {morse_chars}")
except FileNotFoundError:
    print("[-] Morse codes file not found.")
except KeyboardInterrupt:
    print("\n[-] ctrl + c detected, program terminated.")
    sys.exit(0)
