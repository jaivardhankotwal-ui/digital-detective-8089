# Mission 03 — Understand the Operating System

## 1. Task / objective
Investigate the operating system environment, explore active processes and process identifiers (PIDs), evaluate filesystem hierarchies and path conventions (absolute vs. relative), analyze POSIX file permission modes (`r`, `w`, `x`), and explain key operating system kernel responsibilities.

## 2. Work completed
- Inspected the host OS version, kernel architecture, active user session, and disk utilization metrics.
- Examined process models and explained PIDs and process lifecycles.
- Demonstrated relative versus absolute filesystem paths within the assignment hierarchy.
- Decoded POSIX permissions (`-rw-r--r--`) on project files.
- Completed a comprehensive explanation table detailing core OS kernel roles with real-world examples.

## 3. Commands / tools used

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS distribution, Darwin kernel release, and hardware CPU architecture. | macOS 27.2.1, Darwin Kernel 27.2.0, Architecture: `arm64` (Apple Silicon) |
| **Current account identity** | Identifies the logged-in user account executing commands and determining file ownership. | User: `[redacted-student-account]` (UID standard user) |
| **Available and used storage** | Shows mounted APFS root filesystem volume size, used storage, and free capacity. | Root volume size: ~926 GiB, Used: ~13 GiB (system container), Available: ~816 GiB (free space) |
| **System activity snapshot** | Shows live process scheduling, CPU load metrics, and active running program states. | Observed active interactive shell (`zsh`), window server, and application daemon tasks |

---

### Task 3.2 — Understand processes

- **What is a process?**
  A process is an active, executing instance of a computer program. While a program on disk is passive code and static data, a process is dynamic: it possesses allocated memory (code segment, stack, heap), CPU registers, an execution state (running, ready, waiting), open file descriptors, and security privileges.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to each active process when it is spawned (via system calls like `fork()` / `spawn()`). The kernel uses the PID to schedule CPU slices, manage inter-process communication (IPC), assign memory boundaries, and terminate or signal processes.
- **Two examples of processes running on a computer:**
  1. `zsh` or `bash` (interactive command-line shell session handling user input).
  2. `Google Chrome` / `Brave` (multi-process web browser running browser window UI, networking threads, and isolated sandboxed renderer processes).

---

### Task 3.3 — Understand paths and permissions

- **Absolute vs Relative Paths:**
  - **Absolute Path:** The complete, unambiguous location of a file or directory starting from the root of the filesystem (`/`). It does not depend on the user's current working directory.
    - *Example:* `/[redacted]/digital_detective_assignment/terminal-practice/original.txt`
  - **Relative Path:** A path defined relative to the current working directory where the user or command is currently operating, often using `.` (current directory) or `..` (parent directory).
    - *Example (from project root):* `terminal-practice/original.txt`
    - *Example (from inside `terminal-practice/`):* `../README.md`

- **File Permission Analysis:**
  Inspected `terminal-practice/original.txt`:
  ```text
  -rw-r--r--@ 1 [redacted] staff 60 Nov 25 16:49 original.txt
  ```
  - **Owner permissions (`rw-`):** Read (`r`) and Write (`w`) are enabled; Execute (`x`) is not set. The owner can inspect and edit the file, but not execute it as a binary/script.
  - **Group permissions (`r--`):** Read-only. Members of the `staff` group can view contents but cannot modify or execute.
  - **Other / World permissions (`r--`):** Read-only for all other users on the system.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Grants permission to open, view, or copy the file's data stream; on directories, allows reading directory file listings. | Opening a text file with `cat` or `read()`. |
| **w — Write** | Grants permission to modify, overwrite, truncate, or append to file contents; on directories, allows creating/deleting files. | Saving changes to a script or editing a document. |
| **x — Execute** | Permits the kernel to load and execute the file as an application binary or script; on directories, permits traversal into the folder. | Running a Python script (`./script.py`) or navigating into a directory (`cd`). |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Controls the creation, scheduling, execution, and termination of active processes, using a CPU scheduler to allocate processing time slices fairly. | Context-switching the CPU between a web browser, code editor, and music player so they appear to run simultaneously. |
| **Memory management** | Allocates, tracks, and isolates virtual memory spaces (RAM) for running processes, preventing applications from corrupting each other's memory. | Dynamically allocating heap memory when an application opens a large dataset and reclaiming it when closed. |
| **Device management** | Provides standardized driver abstractions so software can interact with diverse hardware peripherals without knowing low-level hardware register details. | Translating a standard OS print command into specific raster data instructions sent over USB/Wi-Fi to an HP or Canon printer. |
| **File management** | Organizes persistent storage into structured files, folders, and metadata (APFS, ext4), managing read/write requests, permissions, and directory trees. | Creating a hierarchical folder structure on an SSD and locating block sectors when a file is opened. |
| **User interface / shell** | Provides a medium for human interaction with the machine, either visually through a Graphical User Interface (GUI) or textually via a Command Line Interface (CLI). | The macOS Aqua desktop / Finder window system, or a zsh terminal prompt accepting user commands. |
| **Security and permissions** | Enforces user access control policies, authenticates identities, isolates kernel and user spaces, and guards unauthorized file/device tampering. | Prompting for biometric Touch ID / password before allowing changes to system security preferences or restricting file access by user permissions. |

## 5. Difficulties faced
No major difficulties. Querying system process lists inside sandboxed sub-shells is restricted, which is a standard security feature of sandboxed environments.

## 6. How I resolved them
Used standardized POSIX filesystem commands (`df`, `uname`, `ls -ld`) and well-documented operating system architectural principles to verify behavior.

## 7. Evidence / files
- Permission observation target: `terminal-practice/original.txt`
- Mission documentation: `mission-03-operating-system/README.md`

## 8. Commit details
- Commit message: `Document operating system and file management`
- Status: Staged and committed locally to `main`.
