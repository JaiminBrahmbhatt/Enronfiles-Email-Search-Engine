## Assignment 3
**Homework 3: Email Analysis**

This assignment we have built a tool that can search for terms in the Enron email data set and, for any search results, return the sender's email address and the date and time the message was sent by using the From: and Date: headers, respectively.
We have implemented in python using default packages namely mailbox, os, re and sys. Firstly , we take search term as system argument and make it search over the mail body portion which in return gives us the From: and Date: headers of the mbox of the same email where search term was found.

##  Packages Used

Packages to be used are given in the file packages.txt
 - pyinstaller==4.2
 - pyinstaller-hooks-contrib==2020.11
 ***Note : To install these packages run the makefile*** 
 `make`
  ***or run this command: ***
 ` pip3 install -r packages.txt` for python 3  
 ` pip install -r packages.txt` for python 2

## How to run
The source code directory looks like:

.
├── enron (directory of the .mbox files)
├── enron_search.py
├── makefile
├── packages.txt
├── readme.md
└── readme.txt

**Step 1:** Adding Environment Varible or else mbox files

Commands : 
`ENRON_FILE='directory path to the mbox files'` ## Declare environment variable
`export ENRON_FILE`  ## Set and export environment varible
`env | grep ENRON_FILE` ## Check if it exists

If you are using the enron.mbox files directly make sure files are kept under directory:
enron/
Commands : `cp -r source/. ../enron`

**Step 2:** Run the make file

Command: `make`
Make file should create three directories pycache / build / dist
.
├── __pycache__
├── build
├── dist
├── enron
├── enron_search.py
├── enron_search.spec
├── makefile
├── packages.txt
├── readme.md
└── readme.txt

**Step 3:** Go to folder dist to find the executable file
Command : `cd dist`

**Step 4:** Run the executable using the following command:
Command: `./enron_search term`

## Sample Output
`./enron_search Raised your issue`
1.Phillip K Allen <phillip.allen@enron.com> Mon, 19 Mar 2001 01:36:00 -0800 (PST)
2.Phillip K Allen <phillip.allen@enron.com> Mon, 26 Mar 2001 02:58:00 -0800 (PST)
3.Phillip K Allen <phillip.allen@enron.com> Tue, 26 Sep 2000 09:26:00 -0700 (PDT)
4.Phillip K Allen <phillip.allen@enron.com> Fri, 26 May 2000 07:19:00 -0700 (PDT)
5.Phillip K Allen <phillip.allen@enron.com> Tue, 27 Mar 2001 03:37:00 -0800 (PST)
6.Phillip K Allen <phillip.allen@enron.com> Tue, 26 Sep 2000 09:28:00 -0700 (PDT)
7.Phillip K Allen <phillip.allen@enron.com> Thu, 11 Jan 2001 05:49:00 -0800 (PST)
8.Phillip K Allen <phillip.allen@enron.com> Fri, 17 Nov 2000 00:27:00 -0800 (PST)
9.Phillip K Allen <phillip.allen@enron.com> Thu, 18 Jan 2001 02:08:00 -0800 (PST)
10.Phillip K Allen <phillip.allen@enron.com> Sun, 18 Feb 2001 11:50:00 -0800 (PST)
11.Phillip K Allen <phillip.allen@enron.com> Fri, 16 Feb 2001 00:52:00 -0800 (PST)
12.Phillip K Allen <phillip.allen@enron.com> Tue, 24 Oct 2000 06:29:00 -0700 (PDT)
Results found: 12

## Authors
 1. Aiswarya Annem (aannem1@islander.tamucc.edu)
 2. Abhilash Mukesh (amukesh@islander.tamucc.edu)
 3. Jaimin Brahmbhatt (jbrahmbhatt@islander.tamucc.edu)
