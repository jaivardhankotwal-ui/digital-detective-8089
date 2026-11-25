# Mission 05 — Numbers and Data

## 1. Task / objective
Understand how digital computers represent numbers and characters in binary, perform manual conversions between decimal, binary, and hexadecimal numbering systems showing step-by-step working, verify results using Python built-in functions, build and test an interactive command-line conversion program (`number_converter.py`), and analyze text encoding standards (ASCII vs. UTF-8).

## 2. Work completed
- Carried out manual conversions with full mathematical breakdown for all 7 required numeric problems.
- Executed Python verification tests confirming 100% agreement between manual derivations and Python internal representations.
- Implemented `number_converter.py` supporting user input, conversion, error handling, and structured terminal output.
- Tested the converter against 3 distinct positive integers (`13`, `25`, `42`).
- Researched ASCII code points and character encoding mechanics.

## 3. Commands / tools used
- `python3` interactive evaluation: Used `bin()`, `hex()`, `int()`, and `ord()`.
- Python script runner: `python3 mission-05-numbers-data/number_converter.py`.

---

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | **Method (Repeated Division by 2):**<br>• $13 \div 2 = 6$, remainder **1**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1**<br>Reading remainders from bottom to top (MSB to LSB): **`1101`** |
| **Convert decimal 25 to binary** | **Method (Repeated Division by 2):**<br>• $25 \div 2 = 12$, remainder **1**<br>• $12 \div 2 = 6$, remainder **0**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1**<br>Reading remainders from bottom to top: **`11001`** |
| **Convert binary 1010 to decimal** | **Method (Positional base-2 expansion):**<br>• $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>• $= 8 + 0 + 2 + 0 = \mathbf{10}$ |
| **Convert binary 1101 to decimal** | **Method (Positional base-2 expansion):**<br>• $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>• $= 8 + 4 + 0 + 1 = \mathbf{13}$ |
| **Convert hexadecimal A to decimal** | In hexadecimal (base 16), symbols 0–9 represent values 0–9, and letters A–F represent 10–15.<br>• $\text{A}_{16} = 10 \times 16^0 = \mathbf{10}$ |
| **Convert hexadecimal 1F to decimal** | **Method (Positional base-16 expansion):**<br>• $(1 \times 16^1) + (\text{F} \times 16^0)$ where $\text{F} = 15$<br>• $= 16 + 15 = \mathbf{31}$ |
| **Convert binary 1111 to hexadecimal** | **Method (Grouping in nibbles of 4 bits):**<br>• Binary `1111` in base 10 is $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15$.<br>• In hexadecimal, 15 is represented by single digit **`F`** (or `0xF`). |

---

### Task 5.2 — Verify using Python

| Problem from Task 5.1 | Python Expression Tested | Python Result | Match Manual Calculation? |
| :--- | :--- | :--- | :---: |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | **Yes** (`1101`) |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | **Yes** (`11001`) |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | **Yes** (`10`) |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | **Yes** (`13`) |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | **Yes** (`10`) |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | **Yes** (`31`) |
| Binary 1111 to hexadecimal | `hex(int('1111', 2))` | `'0xf'` | **Yes** (`F`) |

---

### Task 5.3 — Build a small number converter
- Script created: `mission-05-numbers-data/number_converter.py`
- **What built-in functions do:**
  - `int(user_input)`: Converts the input string into a base-10 numerical integer.
  - `bin(number)`: Converts an integer into its equivalent binary string prefixed with `0b`.
  - `hex(number)`: Converts an integer into its equivalent hexadecimal representation prefixed with `0x`.

#### Test Executions

| Test number | Binary output | Hexadecimal output |
| :---: | :---: | :---: |
| **13** | `1101` (or `0b1101`) | `D` (or `0xD`) |
| **25** | `11001` (or `0b11001`) | `19` (or `0x19`) |
| **42** | `101010` (or `0b101010`) | `2A` (or `0x2A`) |

---

### Task 5.4 — How is text stored?

- **ASCII decimal codes:**
  - Uppercase letter **`A`**: **`65`** (`0b01000001` / `0x41`)
  - Lowercase letter **`a`**: **`97`** (`0b01100001` / `0x61`)
- **Why a computer needs an encoding standard:**
  Digital processors and storage memory can only store and manipulate binary voltage states (`0`s and `1`s). An encoding standard establishes an agreed-upon universal dictionary mapping human characters, numerals, and punctuation symbols to unique numeric binary code points, ensuring text written on one computer displays identically on any other system without corruption.
- **Example of character not in basic ASCII:**
  Basic ASCII is limited to 7 bits (128 characters, 0–127: English Latin alphabet, Arabic numerals, basic symbols). Characters such as the Indian Rupee symbol (**`₹`**), Euro symbol (**`€`**), or emojis like **`🚀`** require modern multi-byte character standards like **UTF-8** (Unicode).

## 5. Difficulties faced
Python's built-in `bin()` and `hex()` functions include `0b` and `0x` prefixes by default.

## 6. How I resolved them
Handled formatting cleanly in `number_converter.py` using slicing (`[2:]`) to present both raw numerical strings and formal prefixed representations to avoid confusion.

## 7. Evidence / files
- Conversion script: `mission-05-numbers-data/number_converter.py`
- Documentation: `mission-05-numbers-data/README.md`

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Status: Staged and committed locally to `main`.
