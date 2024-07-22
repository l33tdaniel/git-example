# Git Example:

Authored by Daniel Neugent

I start the repo by typing `git init` which initializes a new local empty repository. if you have any files in the repo, you might notice them turning green in Visual Studio Code. <br>
I create a new file called `testfile.txt` and another file called `.gitignore`. You'll notice that they both turn green, however, if you type `testfile.txt` into .gitignore, you'll notice it turns grey. The reason for this is that it will now be ignored by our local git repo. This is important for files such as secrets or keys, or anyting you don't want to have uploaded (like node_modules)<br><br>

Next, I make a file called `main.py`. I want to write some cool code. It should turn green upon you making it. I typed hello world in it, and now I'm ready to try pushing it up.


Helpful commands to memorize:

For starting up:<br>
    git init<br>
    git config --global user.name "[firstname lastname]"<br>
    git config --global user.email "[valid email]"<br>
    How to add SSH key: https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html

Helpful commands:

    `git branch` Lists all current branches and also allows you to make a new one if you type the name of a brach after the word branch
    `git checkout` allows you to checkout another branch
    `git merge "branch-name"` merges a branch into your current branch
    `git add` allows you to stage files for a commit
    `git commit -m"message"` making a new commit
    `git push git@github.com:username/reponame.git branch-name


For a full reading: https://education.github.com/git-cheat-sheet-education.pdf<br>
Slightly cringe explanation but is helpful lol: https://www.youtube.com/watch?v=wpISo9TNjfU<br>
Background on SSH: https://www.youtube.com/watch?v=5JvLV2-ngCI<br>


