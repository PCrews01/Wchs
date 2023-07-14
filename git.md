<!-- MD FOR CREATING GIT COMMANDS -->

<!-- SHOW ALL BRANCHES -->
git branch -a 

<!-- CHECK ITEMS IN THE STAGING AREA -->
git status

<!-- MERGE BRANCHES// BE SURE TO BE ON THE BRANCH YOU WANT TO MERGE TO  -->
git merge [name] -m "[message]"

<!--  CHECK LOG HISTORY -->
git log 

<!-- LOG GRAPH TO SEE VISUALIZED LOGS -->
git log --oneline --graph

<!-- DELETE BRANCH// BE SURE TO MERGE NEEDED CONTENT BEFORE DELETING -->
git branch -d [branch]

<!-- LINK TO NETWORK -->
git remote add origin [url]
git push -u origin main

<!-- SEWND CHANGES TO NETWORK -->
git push