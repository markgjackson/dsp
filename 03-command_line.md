# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

less - view a file
rmdir - remove directory
ls - list directory
apropos - finding help
mkdir - make directory
grep - looking inside files
cd - change directory
hostname - what’s your computer’s name?
rm - removing a file
touch - making empty files

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls lists the files. -a lists all files in the given directory, including those whose names start with "." -l long format, displaying Unix file types, permissions, number of hard links, owner, group, size, last-modified date and filename. -h print sizes in human readable format. (e.g., 1K, 234M, 2G, etc.) 

---


---

What does `xargs` do? Give an example of how to use it.

xargs is used to build and execute command lines from standard input. For example,
find /path -type f -print | xargs rm
In the above example, the find utility feeds the input of xargs with a long list of file names. xargs then splits this list into sublists and calls rm once for every sublist. Yes I took this from Wikipedia but it works.

---

