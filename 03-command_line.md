# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. apropos = find what man page is appropriate
2. mkdir -d = make entire path even if all directories don't exist
3. pushd = Push directory to stack
4. popd = Pop directory from stack
5. ls -lR = shows all subdirectories, not just one level down
6. cp -r = copy directories with files in them to another directory
7. rm -rf = recursively removes everything in directory
8. $>>$ = takes output of command on left and appends it to file on right
9. $|$ = takes output from command on left and pipes it to command on right
10. find . -name "*.txt" -print = finds all files with name that has .txt in it in current directory and prints it out
---

###Q2.  List Files in Unix   

What do the following commands do:  
> > 
`ls` = lists visible files and folders in directory
`ls -a` = lists all files and folders including hidden files starting with .
`ls -l` = uses a long listing format that includes permissions, owner, size, and date of files and folders in directory
`ls -lh` = shows detailed list as above with -l with human readable sizes
`ls -lah` = shows detailed list with human readable sizes of all files including files starting with .
`ls -t` = shows files and folders sorted by modification time with the newest first
`ls -Glp` = shows detailed list without group names and it appends indicator (i.e. slash) to directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
'ls -R' = shows subdirectories as well
'ls - d' = displays only directories
'ls -pq' = displays all nonprinting characters like ? and displays directories with /
'ls -m' = displays names as comma-separated list
'ls -u' = displays files by file access time
 

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs reads from standard input (separated by blanks) and executes command on these inputs 
 'find . -name "*.txt" -print0 | xargs -0 rm -rf' = removes all files in current directory that are .txt (even the ones that have white space or new lines in name)
 

