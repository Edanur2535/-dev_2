


def sifre_cozucu(ciphertext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_len = len(keyword)
    plaintext = ""

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword[i % key_len].upper()
            shift = alphabet.index(key_char)
            if char.isupper():
                plaintext += alphabet[(alphabet.index(char) - shift) % 26]
            else:
                plaintext += alphabet[(alphabet.index(char.upper()) - shift) % 26].lower()
        else:
            plaintext += char

    return plaintext

anahtar = "PINES"
metin ="WmlHaexrvsclZetttOpwclvrztzrMeRcevwcbycDxdvryXvGlwNmnv1883 sclVLasBumkAmgxwgGaLgemfXzpbVxOdcyhGcmGegGmngzNwhMYdbGlwXlreXgwzXztWbzatZrxmgvOeuzenvvhBbXztXnwlPonmf3"
cozulmus_metin = sifre_cozucu(metin, anahtar)
print("Çözülmüş Metin:", cozulmus_metin)
