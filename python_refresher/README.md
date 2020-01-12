# Core Python

## Installing Jupyter Notebooks

In order to make our python class easier to understand we're going to use [jupyter](https://jupyter.org/) to go over the lesson plans. Jupyter provides an incredibly convenient and easy way to write and run python code line by line on an interactive system shell. 

To install jupyter we'll first need to install Python3 and something known as the **Python package manager** (known as PIP). To install python and pip please follow the instructions for your OS:

### Installing Python on WINDOWS:

1. To install python on Windows travel over on over to the Python for Windows [download](https://www.python.org/downloads/windows/) page. 

2. Once there Please download **Python3** version 3.7.4

![installpython](./images/installpython.jpeg)

3. **If you are on the Windows 10 operating system** then ideally at this point you should install and enable **bash**. If you've enabled the wsl then just open up a CMD prompt and type `bash` into the terminal.

4. First try typing the command `python --version` into your command line. You should get a response. Please try typing in `python3 --version` here as well. If python3 returns a version then you're good to go with python.

4. Once **bash** is enabled (although you could also do this from **powershell** if you prefer) type in `pip --version`. If you get a response on this then congrats! You have pip installed and we're ready to go!

### Installing Python on Mac/Linux

1. Install [homebrew](https://brew.sh/) for mac by pasting the installation script into a command prompt

2. Run this command on your command line: `brew install python3`

3. Type in `python3 --version`

4. Also please run `brew install pipenv` (we'll be using this later). 

5. Just to make certain (although it comes standard with the install) also go ahead and type in `pip3 --version`. If you get a version return then we're successful!

## Installing Jupyter notebooks and Anaconda

1. Next we have to install [jupyter](https://jupyter.readthedocs.io/en/latest/install.html) which is recommended through [Anaconda](https://www.anaconda.com/distribution/). Why Anaconda? Well...if anyone wants to do data science and machine learning with Python- Jupyter notebooks and Anaconda are kind of the "go to" methods for this!

2. Obviously download the 3.7 version here. 

![anaconda](./images/anaconda.png)

3. Now that we're set up here let's work on getting everything pointed to the correct place! When you launch **Anaconda** you will get a screen that looks like this:

![introscreen](./images/introscreen.png)

4. We're after **jupyter notebooks** here. When we click on "launch" we should get a web interface that points to our home directory. NOW we just need to get the material for this to point at! 

5. [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository (or, if you can't do that, download the zip file and open it locally). This should give you all of our materials that you can find in the github repository here. 

6. NOW we just need to get this system to point at the right directory (if you put this data in your home directory you can skip this step; your home directory is usually **//Users//{yourname}**). 

7. IF NOT...go to your command line (Windows OR mac) and type in the following command: `jupyter notebook --notebook-dir={CompletePathToyourNotebookProbablyEndingWithPythonFundamentals}`.

8. That should open up a screen that looks like this:

![jupytersuccess](./images/jupytersuccess.png)

9. Now click on **Python Fundamentals Day 1.ipynb** and you should be off to the races!

# Please let me know if you are having trouble with the above sections!

Obviously on Virtual Learning platforms it's hard for me to simply "walk over to your desk and help out" so we're going to take a fairly long break after this so that anyone that was struggling can catch up. Please help each other out where possible and don't hesitate to put questions in the chat! 



