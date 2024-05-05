# Learn

<!-- Basic Commands
Check Status: Always check the status before performing any action.
Branch Naming Convention
Feature Branches: feature/
Bugfix Branches: bugfix/
Release Branches: release/
Hotfix Branches (for Production): hotfix/
Branch Operations
Create New Branch: git checkout -b <Branch Name>
Pushing Changes
Push Branch Changes:
sql
Copy code
git add .
git commit -m "Message"
git push origin <Branch Name>
Merging
Merge Branches:
php
Copy code
git checkout <Target Branch>
git pull origin <Target Branch>
git flow feature start <Feature Branch>
git pull origin <Other Branches>
git status
git push origin <Other Branches> (if correction)
git push origin <Feature Branch>
Deleting Remote Branch
Delete Remote Branch: git push origin --delete <Branch Name>
Additional Operations
View Log Details: git log
Adding Another Origin:
csharp
Copy code
git init
git remote add origin <URL>
git push -u origin --all
Rare Use Cases
Create Temporary Branch (Stash):
arduino
Copy code
git stash (for local temporary storage)
git stash pop (put changes in a new branch)
Merge:
php
Copy code
git checkout <Target Branch>
git merge <Branch to Merge>
git push origin <Branch to Merge>
This README serves as a quick reference for Git commands commonly used in this project. For more detailed instructions, refer to Git documentation or project-specific guidelines.

give the code in copyable formate 
ChatGPT
Certainly! Below is the same Git commands cheat sheet in copyable format:

markdown
Copy code -->
### Git Commands Cheat Sheet

This README provides a quick reference guide for common Git commands used in this project.

#### Basic Commands

- **Check Status**: Always check the status before performing any action.
  
#### Branch Naming Convention

- **Feature Branches**: `feature/`
- **Bugfix Branches**: `bugfix/`
- **Release Branches**: `release/`
- **Hotfix Branches (for Production)**: `hotfix/`

#### Branch Operations

- **Create New Branch**: `git checkout -b <Branch Name>`
  
#### Pushing Changes

- **Push Branch Changes**:
git add .
git commit -m "Message"
git push origin <Branch Name>

markdown
Copy code

#### Merging

- **Merge Branches**:
git checkout <Target Branch>
git pull origin <Target Branch>
git flow feature start <Feature Branch>
git pull origin <Other Branches>
git status
git push origin <Other Branches> (if correction)
git push origin <Feature Branch>

markdown
Copy code

#### Deleting Remote Branch

- **Delete Remote Branch**: `git push origin --delete <Branch Name>`

#### Additional Operations

- **View Log Details**: `git log`
- **Adding Another Origin**: 
git init
git remote add origin <URL>
git push -u origin --all

markdown
Copy code

#### Rare Use Cases

- **Create Temporary Branch (Stash)**:
git stash (for local temporary storage)
git stash pop (put changes in a new branch)

markdown
Copy code

- **Merge**:
git checkout <Target Branch>
git merge <Branch to Merge>
git push origin <Branch to Merge>

kotlin
Copy code

This README serves as a quick reference for Git commands commonly used in this project. For more detailed instructions, refer to Git documentation or project-specific guidelines.
You can copy the entire content above and paste it into your README file.