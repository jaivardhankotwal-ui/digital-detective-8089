# Mission 01 — Computer Fundamentals and IPOS

## 1. Task / objective
Investigate and explain how a general-purpose computer processes data using the Input-Process-Output-Storage (IPOS) model, categorize hardware and software components with their respective functions, and identify everyday computer-based systems.

## 2. Work completed
- Detailed an IPOS cycle for a practical real-world scenario (capturing, editing, and saving a voice note / audio recording).
- Created a comprehensive classification table identifying at least four hardware devices and four distinct software packages across Operating Systems, Application Software, and Utility Software.
- Documented three everyday dedicated/embedded computer-based systems outlining their primary purpose, primary input, and primary output.

## 3. Commands / tools used
- Text editor / Markdown formatting tools for structured table synthesis.
- Hardware and software system inspection utilities.

## 4. My understanding

### Task 1.1 — Trace one activity using IPOS
**Chosen Activity:** Recording and saving a voice lecture note.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | Acoustic sound waves from user speech are captured and converted into analog electrical signals, which an analog-to-digital converter (ADC) transforms into digital samples. | Microphone / Audio interface |
| **Processing** | The CPU runs audio processing routines, applies noise cancellation filters, compresses the raw audio stream into AAC format, and buffers data in system RAM. | CPU (Processor) and RAM (Memory) |
| **Output** | Real-time audio waveform visualizer is rendered on display, and audio feedback is streamed through speakers/headphones. | Display Screen / Speakers |
| **Storage** | The finalized `.m4a` compressed audio recording file is written to persistent flash memory blocks for long-term retention. | Solid State Drive (SSD) / Cloud Storage |

**Cycle Explanation:**
The activity begins at the **Input** stage where physical speech is digitized by the microphone hardware. The digitized signal passes through the system bus into system memory (RAM). The **Processing** stage takes over as the CPU executes audio-compression algorithms, structuring the digitized stream into a recognized audio container format. While processing occurs, the system provides immediate **Output** via visual audio waveforms on the screen and audio monitoring to confirm clear sound capture. Finally, upon hitting "Save", the operating system's file system commits the memory buffer into permanent **Storage** (SSD), allowing retrieval even after the computer powers down.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical Keyboard** | Hardware | Not applicable | Captures tactile physical keystrokes and transmits ASCII/scancode signals to the computer. |
| **Solid State Drive (NVMe SSD)** | Hardware | Not applicable | Provides high-speed, non-volatile persistent data storage using flash memory cells. |
| **Graphics Processing Unit (GPU)** | Hardware | Not applicable | Accelerates parallel mathematical matrix calculations for display rendering and compute workloads. |
| **Optical Mouse** | Hardware | Not applicable | Detects two-dimensional surface motion to control graphical cursor coordinates on screen. |
| **macOS / Linux Kernel** | Software | Operating System | Manages hardware abstractions, CPU scheduling, memory allocation, and peripheral access. |
| **Visual Studio Code** | Software | Application Software | Facilitates code authoring, syntax highlighting, and software development workflows. |
| **Brave / Google Chrome** | Software | Application Software | Interprets HTML, CSS, and JavaScript to render interactive web pages over HTTP/HTTPS. |
| **Disk Utility / Disk Management** | Software | Utility Software | Diagnoses, partitions, repairs, and formats storage volumes and partition tables. |
| **Terminal (zsh)** | Software | Utility Software | Provides a command-line interface shell to interactively invoke system binaries and scripts. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Authenticates bank customers and dispenses cash securely while updating account ledgers. | Numeric PIN keypad / Chip card reader | Physical cash dispenser / Printed transaction slip |
| **Smart Traffic Signal Controller** | Dynamically regulates vehicle flow through busy intersections based on traffic congestion. | Inductive road-loop sensors / Motion camera | Red, Yellow, and Green LED signal light arrays |
| **Digital Microwave Oven** | Regulates magnetron heating power and countdown duration to cook or heat food evenly. | Tactile numeric membrane keypad / Door sensor | Segmented LCD countdown display / High-pitch beeper |

## 5. Difficulties faced
No major difficulties encountered; categorizing system software vs utility software required ensuring clear distinction between core OS kernels and supporting maintenance utilities.

## 6. How I resolved them
Clarified that utility software serves maintenance, diagnostics, and operational support (e.g., Disk Utility, Archive Utility), whereas operating system software provides the foundational resource management abstraction (e.g., Darwin kernel / OS scheduler).

## 7. Evidence / files
- Mission 01 report: `mission-01-computer-basics/README.md`

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Status: Staged and committed locally to `main`.
