# Mission 02 — Become Comfortable with the Terminal

## 1. Task / objective
Master essential command-line interface (CLI) interactions: navigating directory hierarchies, manipulating files safely, understanding standard input/output redirection and Unix piping, comparing command flags, and explaining the role of system package managers.

## 2. Work completed
- Practised foundational terminal navigation and file operations in a safe isolated sandbox (`terminal-practice/`).
- Executed file content writing and non-destructive appending (`>` vs `>>`).
- Executed copy (`cp`) and move/rename (`mv`) routines.
- Evaluated flag modifications with `ls` (`-l`, `-a`, `-h`) and pipeline chaining via `| head -n 5`.
- Verified macOS Homebrew package manager presence and version (`Homebrew 7.0.7`).
- Formatted privacy-conscious logs documenting observed outputs.

## 3. Commands / tools used

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the absolute filesystem path of the current working directory. | Displayed full path: `/[redacted]/digital_detective_assignment/terminal-practice` |
| **Directory listing (`ls`)** | Lists non-hidden files and folders within the current directory. | Displayed file names `original.txt` and `renamed_backup.txt`. |
| **Detailed listing (`ls -l`)** | Lists contents displaying permissions, link count, owner, group, file size, and timestamp. | Showed columns like `-rw-r--r-- 1 [redacted] staff 60 Nov 25 16:49 original.txt`. |
| **Change directory (`cd ..`)** | Modifies the active shell shell context to the parent directory. | Working directory stepped up from `terminal-practice` to project root. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new filesystem folder. | Created isolated directory without errors. |
| **Create empty file (`touch original.txt`)** | Creates a new 0-byte file or updates existing file timestamps. | File `original.txt` appeared in the directory listing. |
| **Copy file (`cp original.txt backup.txt`)** | Creates an identical duplicate file at the specified destination path. | Duplicate `backup.txt` created with exact same 60-byte content. |
| **Move / rename file (`mv backup.txt renamed_backup.txt`)** | Relocates or renames an inode without duplicating data. | `backup.txt` was renamed to `renamed_backup.txt`; original file remained untouched. |
| **Display file contents (`cat original.txt`)** | Concatenates and streams file contents to standard output (stdout). | Printed both Line 1 and Line 2 onto the terminal screen. |

---

### Task 2.2 — Practise file changes safely
Executed sequence inside `terminal-practice/`:
```bash
touch original.txt
echo "Line 1: First entry into file" > original.txt
echo "Line 2: Second appended entry" >> original.txt
cat original.txt
cp original.txt backup.txt
mv backup.txt renamed_backup.txt
```

**Conceptual Answers:**
1. **Difference between replacing file contents (`>`) and adding to the end (`>>`):**
   - The single redirection operator `>` truncates (overwrites) the target file to 0 bytes before writing, erasing previous contents.
   - The double redirection operator `>>` appends new data onto the existing end-of-file (EOF) pointer, preserving all historical content.
2. **Difference between copying a file and moving a file:**
   - `cp` allocates new storage blocks and duplicates the data, producing two independent files with distinct inodes.
   - `mv` modifies the directory entry/metadata pointer without duplicating underlying data blocks on the disk, effectively transferring or renaming the file.
3. **What information does the current-directory display provide?**
   - `pwd` provides the unambiguous absolute hierarchical path from the root directory (`/`) to the active working location, preventing accidental commands executed in unintended paths.
4. **Why is a directory-listing operation useful?**
   - It provides situational awareness of filesystem state, enabling users to verify file existence, file permissions, exact naming, timestamps, and sizes prior to taking action.

---

### Task 2.3 — Understand flags and pipes
- **Directory listing comparison:**
  - `ls`: Shows plain names of non-hidden files.
  - `ls -lah`: Flags combine `-l` (detailed table), `-a` (includes hidden dotfiles such as `.git`, `.`, `..`), and `-h` (renders byte counts into human-readable units like `K`, `M`, `G`).
- **Pipes (`|`) mechanism:**
  - Running `ls -la | head -n 5`:
  - The pipe symbol `|` binds the Standard Output (`stdout`) of the upstream command (`ls -la`) directly to the Standard Input (`stdin`) of the downstream filter command (`head -n 5`).
  - Upstream (`ls -la`) produces the full catalog of files, while downstream (`head`) truncates the stream to only show the initial 5 header lines, preventing terminal overflow.

---

### Task 2.4 — Understand package managers
- **Check performed:** Checked system Homebrew installation (`brew --version`).
  - Observation: `Homebrew 7.0.7`
- **Role of Package Managers:**
  A package manager is a specialized command-line automation suite that handles the fetching, installing, upgrading, dependency resolution, and cleanly removing of third-party software packages and command-line tools. It automates compilation and binary distribution while tracking dependency trees, preventing version conflicts and manual download vulnerabilities.

## 5. Difficulties faced
No major difficulties. Terminal pathing and permission checks executed as expected.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Sandbox practice directory: `terminal-practice/`
- Evidence files: `terminal-practice/original.txt`, `terminal-practice/renamed_backup.txt`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Status: Staged and committed locally to `main`.
