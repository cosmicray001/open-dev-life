# Basic Git
---
### Install git from https://git-scm.com/
---
### Configure your Git username/email
You typically configure your global username and email address after installing Git. However, you can do so now if you missed that step or want to make changes. After you set your global configuration, repository-specific configuration is optional.

* Open the command line.

* Set your username:
```
git config --global user.name "FIRST_NAME LAST_NAME"
```
* Set your email address:
```
git config --global user.email "MY_NAME@example.com"
```
---
- turns any directory into a Git repository.
```
git init
```
- git add
```
git add -A
```
- git commit
```
git commit -m "commit message"
```
- git push
```
git push -u origin HEAD
```
- git create branch and checkout
```
git checkout -b my-branch-name
```
- git amend
```
git commit --amend
```
- edit git commit history
```
git commit --amend --no-edit --date "$(date)"
```
- git diff
```
git diff
```
- git log
```
git log
```