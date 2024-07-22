'''
- Main and master should ALWAYS be working
- Each feature has its own branch
    -	Once finished, to merge into main need to make a pull request
        -	Pull request are basically asking dev op to check code and if it’s good then merge into main/master or any other major branches
-	Local repo(personal computer) -> github (remote repo) -> cloud (deployed)
-	Git commands
    	1. Git init : initializing an empty git repo
    	2. Git add : adds it to a commit
    	    Git add * (adds everything except git ignore)
    	3. Git commit -m “message” –:committing
    	4. Git push git@github.com:userName/RepoName.git branchName : pushes to github
    	Git checkout -b branchName : creates a new branch	
•	Git ignore – add file names that you don’t want to push (like keys, tokens, and libraries)
'''