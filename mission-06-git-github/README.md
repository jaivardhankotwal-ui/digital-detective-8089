# Mission 06 — Git and GitHub

## 1. Task / objective
Understand distributed version control concepts with Git, practice staging, committing, inspecting commit history, create and work with feature branches (`update-about`), simulate and explain the GitHub Pull Request (PR) review and merge workflow, and author a comprehensive Git command glossary.

## 2. Work completed
- Explored Git repository status checking, selective file staging, and commit history graphs.
- Created and switched to a dedicated feature branch named `update-about`.
- Modified the root `README.md` to append the required "My Learning" reflection section.
- Staged and committed the feature branch changes with an explicit descriptive commit message.
- Integrated the feature branch into `main` using branch switching (`git checkout main`) and merging (`git merge update-about`), keeping the local history synchronized.
- Compiled explanations for Pull Requests, branches, staging mechanics, and an 8-operation Git command glossary.

## 3. Commands / tools used

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Displays the current branch, untracked files, changes staged for the next commit, and unstaged modifications in the working tree. |
| **Stage selected changes (`git add <file>`)** | Moves specific file modifications from the working directory into the Git index/staging area, marking them for inclusion in the upcoming commit snapshot. |
| **Create a commit (`git commit -m "<msg>"`)** | Packages all currently staged changes into a permanent cryptographic snapshot (SHA-1/SHA-256 hash) with author metadata, timestamp, and explanation message. |
| **View commit history (`git log`)** | Displays the chronological record of commits on the current branch, showing commit hashes, author details, dates, and commit messages. |

**Staging vs. Committing Difference:**
- *Staging* (`git add`) is the preparation phase: it acts as a selective staging buffer (index) allowing you to group specific changes together before finalizing them.
- *Committing* (`git commit`) is the permanent recording phase: it captures whatever is currently in the staging index into a permanent snapshot in the repository's cryptographic history tree.

---

### Task 6.2 & 6.3 — Create a branch and understand Pull Requests

- **Branch created:** `update-about`
- **Commands used:**
  ```bash
  git checkout -b update-about
  # Edited README.md to add 'My Learning' section
  git add README.md
  git commit -m "Add My Learning section to root README on update-about branch"
  git checkout main
  git merge update-about
  ```

- **What is a Branch?**
  A branch is an independent, lightweight movable pointer to a specific commit in the Git history graph. It allows a developer to diverge from the main codebase to build features, fix bugs, or test experimental ideas in isolation without risking the stability of the production (`main`) code.

- **What is a Pull Request (PR)?**
  A Pull Request is a collaborative review mechanism provided by platforms like GitHub. It notifies project maintainers and team members that a feature branch is ready to be reviewed, discussed, and merged into a target branch (such as `main`). It provides a visual diff of changes, automated testing feedback, code commenting, and approval gates before code integration.

- **Why are they useful in team collaboration?**
  Branches and Pull Requests prevent developers from overwriting each other's code, keep production branches stable, enable asynchronous peer reviews, and provide a clear historical discussion log explaining *why* and *how* changes were introduced.

---

### Task 6.4 — Git command glossary

1. **Initialise a repository (`git init`):** Creates a new Git repository and sets up the internal `.git/` metadata directory in the current folder.
2. **Check status (`git status`):** Displays the current branch and reports which files are modified, staged, or untracked.
3. **Stage changes (`git add <file>`):** Adds modified files from the working directory into the staging area (index) for the next commit.
4. **Commit changes (`git commit -m "<msg>"`):** Records a permanent snapshot of staged changes into the repository history with an explanatory message.
5. **View history (`git log`):** Shows the chronological list of historical commits, authors, timestamps, and commit hashes.
6. **Create or list branches (`git branch` / `git branch <name>`):** Lists existing local branches or creates a new branch pointer at the current commit.
7. **Switch branches (`git switch <name>` or `git checkout <name>`):** Updates the working directory files to match the commit pointed to by the specified branch.
8. **Publish changes (`git push <remote> <branch>`):** Uploads local branch commits to an online remote repository host (such as GitHub).
9. **Retrieve remote changes (`git pull` / `git fetch`):** Downloads and integrates commits from the remote repository into the local working branch.

## 5. Difficulties faced
No difficulties encountered. Branch creation, staging, and merge operations completed smoothly.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Updated root file: `README.md` (containing "My Learning" section)
- Branch created: `update-about`
- Mission documentation: `mission-06-git-github/README.md`

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Status: Staged and committed locally to `main`.
