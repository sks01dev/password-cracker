
# 🔐 Password Cracker - Brute Force & Word List Matching

Welcome to the **Password Cracker** project! This tool, developed in Python, attempts to crack passwords using two methods: common word list matching and brute-force techniques. It's intended for educational purposes to demonstrate password security concepts.

![Password Cracker Demo](https://your-image-link.com/demo-image.png) <!-- Add an image link here if available -->

---

## 📜 Table of Contents
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Setup](#-setup)
- [Usage](#-usage)
- [Example Output](#-example-output)
- [Notes](#-notes)
- [License](#-license)

---

## ✨ Features

- **Common Word List Matching**: Checks the password against a list of commonly used passwords.
- **Brute-Force Attack**: Generates combinations to guess the password, with options to include digits and symbols.
- **Customizable**: Easily adjust parameters like maximum length, character set, etc.
- **Performance Tracking**: Displays time taken to attempt cracking.

---

## 🔍 How It Works

### 1. `common_guess` Function
This function checks if the password exists in a predefined `words.txt` file, which contains a list of common passwords.

- **Example**: If `words.txt` has entries like `password123`, `qwerty`, and `abc1`, the function quickly checks for a match.

### 2. `brute_force` Function
If the password isn't found in the common list, the `brute_force` function generates all possible character combinations up to a certain length and checks each one.

- **Parameters**:
  - `digits=True`: Includes numbers.
  - `symbols=True`: Includes special characters.
- **Example**: With `password = 'abc1'`, it will generate sequences like `"aaa"`, `"aab"`, until it matches `"abc1"`.

### 3. `main` Function
The `main` function runs the entire process:
- Attempts a common word match first.
- If unsuccessful, it switches to brute-force, incrementally increasing the character length.
- Displays time taken to complete the process.

---

## ⚙️ Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/password-cracker.git
   cd password-cracker
   ```
2. Create a `words.txt` file in the project directory with a list of common passwords (one per line).

3. Ensure you have Python 3 installed:
   ```bash
   python --version
   ```

---

## ▶️ Usage

Run the script from your terminal:
```bash
python password_cracker.py
```

Customize the password in `main()` by changing the `password` variable.

---

## 📝 Example Output

```plaintext
Searching
No match found for length 3.
No match found for length 4.
"abc1" was cracked in 5,432 guesses.
Time taken: 3.5 seconds
```

---

## ⚠️ Notes

- **Educational Use Only**: Do not use this project for unauthorized access.
- **`words.txt`**: Ensure the file is present in the project directory; otherwise, `common_guess` will skip the common word check.
- **Performance**: The brute-force method becomes slow with increased password length and complexity.

---

## 📜 License
This project is open-source and available under the MIT License.
