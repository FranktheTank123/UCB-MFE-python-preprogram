# Lecture 1

## Goal 
- Use `git` to interact with this repository
- 

## Introduction to Git
- [What Is Git & Why Should You Use It?](https://www.nobledesktop.com/blog/what-is-git-and-why-should-you-use-it)
    - Git is a version control system
    -  ![](https://www.nobledesktop.com/image/blog/git-branches-merge.png)
    - Ways to use git
      - command line interface (CLI)
      - desktop graphic user interface (GUI), such as [Sourcetree](https://www.sourcetreeapp.com/)
    - Local Repository
      - Folder-based, with a `.git` subfolder tracking the changes.
    - Remote Repository
      - ![](https://www.nobledesktop.com/image/blog/git-distributed-workflow-diagram.png)
- [Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Basic concepts & commands
  - Create a git repository
    - create a folder: `mkdir git-intro`
    - go inside the folder `cd git-intro`
    - initialize git: `git init`
  - make a commit
    - create a file: `touch file1.txt`
    - check status: `git status`
      - staged file vs. unstaged file
    - stage a file: `git add file1.txt`
    - check status: `git status`
    - commit a change: `git commit -m 'add file1.txt'`
    - check status: `git status`
    - check Sourcetree history
  - make another commit
    - add a line in `file1.txt`
    - `git status` and `git diff` (and GUI visualization)
    - `git add .` and `git commit -m 'hello world'`
  - create a branch
    - why can't we just iterate on `master`?
    - `git checkout -b branch_1`
    - switching between branches: `git checkout master`
    - create a commit on a branch
    - merge into master
      - `git checkout master`
      - `git merge branch_1`
      - explain via Sourcetree
    - create a commit on both master and branch
    - create a conflict commit on both master and branch
  - Remote repository
    - why do we need a remote repository?
    - create a github account
    - go to [Python Preprogram repo](https://github.com/FranktheTank123/UCB-MFE-python-preprogram)
    - clone the repo: `https://github.com/FranktheTank123/UCB-MFE-python-preprogram.git`
    - how to constantly keep up-to-date?
      - Do `git pull origin main` frequently
  - Pull request 
    - [Why do we need a pull request?](https://co-learning.eu/2017/10/04/why-and-how-do-we-use-pull-request/)
    - create a branch and make some changes
    - push that branch to remote: 
    

## Introduction to Anaconda 


## 