def checking_en(alphabet, key_word, k):
    post = True
    if len(set(alphabet)) != len(alphabet):
        print(f"    All letters in the alphabet must be different: {alphabet}")
        post = False
    if len(set(key_word)) != len(key_word):
        print(f"    All letters in the key world must be different: {key_word}")
        post = False
    if not k.isdigit():
        print(" k must be integer!")
        post = False
    elif 0 > int(k) or int(k) > len(alphabet) - len(key_word):
        print(f"    attribute k = {k}. 'k' must be in interval [0;{len(alphabet) - len(key_word)}]")
        post = False
    return post


class Caesar_encode:

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
    def encode(alphabet, key_word, k, text, file_key, file_encrypted_text):
        encrypted_word = ""
        key_alphabet = Caesar_encode.__get_key_alphabet(alphabet, key_word, k)

        for sym in text:
            index = alphabet.find(sym)
            if index != -1:
                encrypted_word += key_alphabet[index]
            else:
                encrypted_word += sym

        with open(file_key, "w") as file:
            file.write("\n".join([key_word, str(k)]))
        with open(file_encrypted_text, "w") as file:
            file.write(encrypted_word)

        return encrypted_word


def start():
    # print(string.ascii_uppercase)
    file_key = r"key.txt"
    file_encrypted_word = r"encrypted_word.txt"
    file_name_decrypted_word = r"decrypted_word.txt"
    alphabets = ["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                 "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"]
    while True:
        alphabet_index = input("Enter alphabet (1-en | 2-uk): ")
        if alphabet_index not in ["1", "2"]:
            continue
        alphabet_index = int(alphabet_index)

        while True:
            key_word = input("Input key_word: ")
            k = input("Input position k: ")
            if checking_en(alphabets[alphabet_index - 1], key_word, k):
                break
            print("    Try again\n")

        k = int(k)
        text = input(f"Input text which you want to encrypted: ")

        encoded_text = Caesar_encode.encode(alphabets[alphabet_index - 1], key_word, k, text, file_key,
                                            file_encrypted_word)
        print(f"Encoded text: {encoded_text}")
        break


if __name__ == '__main__':
    start()

