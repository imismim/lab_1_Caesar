class Caesar_decoce:
    @staticmethod
    def __get_key_alphabet(alphabet, key_word, k):
        result = ""
        for sym in alphabet:
            if sym not in key_word:
                result += sym
        if k == 0:
            return key_word + result
        k -= 1
        result = result[-k:] + result[:-k]
        return result[-k:] + key_word + result[:-k]

    @staticmethod
    def decode(alphabet, file_key, file_encrypted_word, file_name_decrypted_word):
        with open(file_key, "r") as file:
            key_word = file.readline()[:-1]
            k = int(file.readline())
        with open(file_encrypted_word, "r") as file:
            encrypted_word = file.readline()
        decrypted_word = ""
        key_alphabet = Caesar_decoce.__get_key_alphabet(alphabet, key_word, k)

        for sym in encrypted_word:
            index = key_alphabet.find(sym)
            if index != -1:
                decrypted_word += alphabet[index]
            else:
                decrypted_word += sym
        with open(file_name_decrypted_word, "w") as file:
            file.write(decrypted_word)
        return decrypted_word


def start():
    # print(string.ascii_uppercase)
    file_key = r"key.txt"
    file_encrypted_word = r"encrypted_word.txt"
    file_name_decrypted_word = r"decrypted_word.txt"
    alphabets = ["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                 "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"]
    with open(file_encrypted_word, "r") as file:
        encoded_word = file.readline()
        for i in encoded_word:
            if i in alphabets[0]:
                alphabet_index = 1
                break
            elif i in alphabets[1]:
                alphabet_index = 2
                break

    print("Decoded text: " + Caesar_decoce.decode(alphabets[alphabet_index - 1], file_key,
                                                  file_encrypted_word, file_name_decrypted_word))


if __name__ == '__main__':
    start()