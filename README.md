## 0x03. AirBnB clone - Deploy static

For this project, students are expected to look at this concept:

    AirBnB clone

Background Context

Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

Before starting, please fork the repository AirBnB_clone_v2 from your partner if you don’t have it

![alt load-balancing](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/288/aribnb_diagram_0.jpg?cache=off)

Resources

Read or watch:

    How to use Fabric
    How to use Fabric in Python
    Fabric and command line options
    CI/CD concept page
    Nginx configuration for beginners
    Difference between root and alias on NGINX
    Fabric for Python 3
    Fabric Documentation

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What is Fabric
    How to deploy code to a server easily
    What is a tgz archive
    How to execute Fabric command locally
    How to execute Fabric command remotely
    How to transfer files with Fabric
    How to manage Nginx configuration
    What is the difference between root and alias in a Nginx configuration

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file at the root of the folder of the project is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    Your Fabric file must work with Fabric 3 version 1.14.post1 (installation instruction below)
    All your files must be executable
    The length of your files will be tested using wc
    All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

Bash Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 14.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    All your Bash script files must be executable
    Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing

More Info
Install Fabric for Python 3 - version 1.14.post1

$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install Fabric3==1.14.post1


Andrew Godwin