Git Fundamentals Exercises
==========================

These exercises will provide a basic working familiarity with git and using git with teams.

Task 1: Clone a repo
--------------------

Goals:
   1. Learn how to clone (make a local working copy of) a git repo
   2. Have a local checkout of the class repo on your local system

Process: 
   1. Clone the repo located at: https://github.com/dannykansas/lessonplans
   2. Navigate and open the file 'WeekOne/W1D1/git-exercises'
   3. Realize you've already done this, as you're already reading this file

Success means:
   - Being able to read this file!


Task Two - Create and Track a New File
--------------------------------------

Goals:
   1. Know how to create and have git track files in an existing local repo
   2. Know how to commit those new files/changes to your local repository

Process:
   1. Create a new file under 'WeekOne/W1D1/'
        - name it with your first initial and last name
        - add a fun factoid about yourself as the contents of the file
   2. Tell git to start tracking this file
   3. Commit the new file

Success means:
   1. The required file exists
   2. Running 'git status' reports 'no changes to be committed'


Task Three - Branching and merging
----------------------------------

Goals:
    1. Know how to create and switch between branches
    2. Know how to merge changes into another branch

Process:
    1. Create a new branch named: w1d1/FirstInitialLastName
    2. Switch to this branch
    3. Add some lines of gibberish to the file you made in Task Two
    4. Commit the changes
    5. Merge your new branch back into the 'master' branch
    6. Switch back to the 'master' branch

Success means:
    1. You have a branch named as required
    2. The 'git status' command says you are currently on 'origin/master' 
    3. Your lines of gibberish exist in your file on the master branch


Task Four - Working with Teams
------------------------------

Goals:
    1. Know how to push your changes to a remote
    2. Know how to fetch changes from a remote

Process:
    1. Fetch and merge in any changes from the remote 'origin/master'
    2. Push your master branch to 'origin/master'

Success means:
    1. Your changes to master are on the remote server
    2. You have a new file located at 'WeekOne/W1D1/ohlook.txt'
 
