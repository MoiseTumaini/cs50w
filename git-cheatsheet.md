# Git Commands Cheat Sheet

A practical reference for Git commands, scenarios, and shortcuts.

---

## 1. Initialize and Check Repository

| Command                      | Description                                                   | Scenario                             |
| ---------------------------- | ------------------------------------------------------------- | ------------------------------------ |
| `git init`                   | Initialize a new Git repository in the current folder         | Starting a new project               |
| `git clone <repo_url>`       | Clone an existing repository                                  | Start working on an existing project |
| `git status`                 | Show current branch, staged/unstaged changes, untracked files | Check the state of your repo         |
| `git log`                    | Show commit history                                           | Review previous commits              |
| `git branch`                 | List branches                                                 | Check which branch you are on        |
| `git branch <branch_name>`   | Create a new branch                                           | Start a new feature or fix           |
| `git checkout <branch_name>` | Switch to another branch                                      | Move between branches                |
| `git switch <branch_name>`   | Modern alternative to checkout                                | Move between branches                |

---

## 2. Staging Changes

| Command                | Description                                                  | Scenario                                              |
| ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| `git add <file>`       | Stage a single file                                          | Add a new file or modified file to commit             |
| `git add .`            | Stage all changes (tracked + untracked) except ignored files | Prepare all changes for commit                        |
| `git add -A`           | Stage all changes including deletions                        | Prepare all changes, including removed files          |
| `git restore <file>`   | Discard changes to a file                                    | Undo modifications to a tracked file                  |
| `git reset <file>`     | Unstage a file                                               | Remove a file from staging without discarding changes |
| `git status --ignored` | Show ignored files                                           | Verify which files are ignored by `.gitignore`        |

---

## 3. Committing Changes

| Command                               | Description                                                    | Scenario                                                       |
| ------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `git commit -m "message"`             | Commit staged changes with a message                           | Standard commit after `git add`                                |
| `git commit -am "message"`            | Stage and commit all **modified tracked files** with a message | Quick commit of modified files, does **not include new files** |
| `git commit --amend -m "new message"` | Modify the last commit message or include additional changes   | Fix typos in last commit or add forgotten files                |

---

## 4. Pushing and Pulling

| Command                       | Description                                     | Scenario                                |
| ----------------------------- | ----------------------------------------------- | --------------------------------------- |
| `git push`                    | Push committed changes to the remote repository | Share your work with team or GitHub     |
| `git push -u origin <branch>` | Push branch and set upstream                    | First push of a new branch              |
| `git pull`                    | Pull latest changes from remote                 | Update local branch with remote changes |
| `git fetch`                   | Fetch remote changes without merging            | Inspect changes before merging          |
| `git merge <branch>`          | Merge another branch into current branch        | Combine feature branch into main branch |

---

## 5. Branching & Merging

| Command                  | Description                              | Scenario                                  |
| ------------------------ | ---------------------------------------- | ----------------------------------------- |
| `git branch`             | List branches                            | Check current branches                    |
| `git branch -d <branch>` | Delete a branch                          | Remove a merged branch                    |
| `git branch -D <branch>` | Force delete a branch                    | Remove unmerged branch (use with caution) |
| `git merge <branch>`     | Merge a branch into current              | Integrate changes from another branch     |
| `git rebase <branch>`    | Reapply commits on top of another branch | Keep a cleaner history                    |
| `git mergetool`          | Open merge tool to resolve conflicts     | Resolve conflicts after a merge           |
| `git status`             | Check which files have conflicts         | Identify files with merge conflicts       |
| `git diff`               | Show differences including conflicts     | Inspect conflicting changes               |

---

## 6. Undo & Revert

| Command                     | Description                                         | Scenario                                           |
| --------------------------- | --------------------------------------------------- | -------------------------------------------------- |
| `git checkout -- <file>`    | Discard changes in a file                           | Undo local modifications                           |
| `git reset HEAD <file>`     | Unstage a staged file                               | Remove file from commit preparation                |
| `git reset --soft <commit>` | Move HEAD to a previous commit, keep changes staged | Undo last commit but keep changes for a new commit |
| `git reset --hard <commit>` | Reset branch to a commit, discard changes           | Completely discard commits and changes (dangerous) |
| `git revert <commit>`       | Create a new commit that undoes a previous commit   | Safely undo changes without altering history       |

---

## 7. Ignoring Files

* Create a `.gitignore` file in the root of your repo.
* Example for Django:

```gitignore
# Django
db.sqlite3
/staticfiles/
/media/
__pycache__/
venv/
```

* Use `git status --ignored` to check ignored files.

---

## 8. Common Shortcuts

| Shortcut | Meaning                              | Notes                                  |
| -------- | ------------------------------------ | -------------------------------------- |
| `-m`     | Commit message inline                | `git commit -m "message"`              |
| `-a`     | Stage all **modified tracked files** | Does **not** stage new untracked files |
| `-am`    | Combination of `-a` and `-m`         | Quick commit for tracked files         |
| `-u`     | Set upstream branch when pushing     | `git push -u origin main`              |
| `-d`     | Delete branch                        | `git branch -d branch_name`            |
| `-D`     | Force delete branch                  | Danger: deletes unmerged branches      |

---

## 9. Scenario Examples

1. **New project**:

```bash
git init
git add .
git commit -m "Initial commit"
```

2. **Clone existing project**:

```bash
git clone <repo_url>
cd project_folder
```

3. **Work on a feature branch**:

```bash
git checkout -b feature/login
# make changes
git add .
git commit -m "Add login feature"
git push -u origin feature/login
```

4. **Quick commit for tracked files**:

```bash
# edit settings.py
git commit -am "Update settings"
```

5. **Discard local changes to a file**:

```bash
git restore lesson3/settings.py
```

6. **Undo last commit**:

```bash
git reset --soft HEAD~1   # undo commit but keep changes staged
```

7. **Delete branch after merging**:

```bash
git branch -d feature/login
```

8. **Resolving merge conflicts**:

```bash
git merge feature/branch2
# if conflicts occur:
git status  # check conflicting files
git diff    # view differences
# edit files to resolve conflicts
git add <resolved_file>
git commit  # complete the merge
```

---

This cheat sheet covers most common Git commands, shortcuts, scenarios, and handling merge conflicts in Django or general development workflows.
