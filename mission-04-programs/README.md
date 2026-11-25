# Mission 04 — How Programs Run

## 1. Task / objective
Understand program execution workflows, create and run an executable Python 3 script (`hello.py`), and contrast the operational characteristics, compilation pipelines, runtime outputs, and trade-offs of compilers versus interpreters.

## 2. Work completed
- Authored `hello.py` containing a single print statement displaying `"Hello from Python"`.
- Verified execution through `python3 mission-04-programs/hello.py`, confirming expected standard output.
- Analyzed the translation pipeline difference between ahead-of-time compiled languages and dynamic bytecode interpreted runtimes.
- Completed the compiler versus interpreter comparative matrix.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Invoked the CPython 3 interpreter runtime to compile and evaluate the script.

### Task 4.1 — Create and run a Python program
- File created: `mission-04-programs/hello.py`
- Source code:
  ```python
  print("Hello from Python")
  ```
- Output observed:
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire high-level source code ahead-of-time (AOT) into binary machine code or assembly prior to program execution. | Translates and executes instructions on-the-fly line-by-line (or via intermediate virtual machine bytecode) during runtime. |
| **Typical output** | A standalone executable binary file (e.g., ELF on Linux, Mach-O on macOS, `.exe` on Windows) or intermediate object file (`.o`). | Direct runtime program output; or cached bytecode (e.g., Python `.pyc`) interpreted by a virtual machine. |
| **One example** | C, C++, Rust, Go | Python, JavaScript (Node.js engine), Ruby, PHP |
| **One advantage** | Maximum execution speed and CPU optimization because CPU instructions are pre-generated with no runtime interpretation overhead. | Rapid development, fast debugging cycle, and immediate platform portability without recompiling binaries for every target OS/CPU. |

### Explanation of Differences
A **compiler** parses the entire codebase at once, performs static type and syntax verification, and transforms human-readable source code directly into native machine code architecture specific to the host CPU before execution ever starts. This makes execution extremely fast and resource-efficient, although the build process takes time and the resulting binary cannot run across different CPU architectures without recompilation.

An **interpreter**, on the other hand, loads source code at runtime and translates and executes commands dynamically step-by-step. While this allows rapid experimentation, interactive REPL debugging, and portable cross-platform execution (any machine with the interpreter installed can run the code), it introduces slight runtime overhead because translation occurs simultaneously with execution. Many modern languages like Python use a hybrid model—compiling source code to intermediate bytecode (`.pyc`) which is then executed by the Python Virtual Machine (PVM).

## 5. Difficulties faced
No difficulties encountered. Script executed cleanly on Python 3.13.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Python program: `mission-04-programs/hello.py`
- Output log: `Hello from Python`

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Status: Staged and committed locally to `main`.
