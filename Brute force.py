import itertools
import string
import time

def common_guess(word: str) -> str | None:
    """Checks if the word is a common password in the word list."""
    try:
        with open('words.txt', 'r') as file:
            words_list = file.read().splitlines()
        
        for i, match in enumerate(words_list):
            if match == word:
                return f'Common match: {match} (#{i + 1})'
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
    return None

def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    """Attempts to brute-force the password by generating all possible combinations."""
    chars = string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    attempts = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess_str = ''.join(guess)
        if guess_str == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'

    return None

def main():
    """Main function to execute the common match and brute-force check."""
    print('Searching')
    password = 'abc1'
    start_time = time.perf_counter()

    # Check if password is in common passwords list
    if common_match := common_guess(password):
        print(common_match)
    else:
        # Attempt brute force with increasing length
        for i in range(3, 7):
            if cracked := brute_force(password, length=i, digits=True, symbols=True):
                print(cracked)
                break
            else:
                print(f'No match found for length {i}.')

    end_time = time.perf_counter()
    print(f'Time taken: {round(end_time - start_time, 2)} seconds')

if __name__ == '__main__':
    main()
