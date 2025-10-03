# Setting-up your environment

Please install the following software on your personal laptop
**before the start of the course**.

<br/>  
<br/>  

## Setup using Anaconda

### Anaconda and Jupyter notebook

[**Anaconda**](https://www.anaconda.com) is an open-source python distribution
that bundles **python3** along with a large number of useful python modules
such as **SciPy**, **NumPy**, or **Pandas**.

* It also bundles other useful software such as the **conda** package manager
  (which allows easy installation of bioinformatics software) and
  **Jupyter Notebook**.  
* Anaconda is cross-platform and available for Windows, Linux, and MacOS
  operating systems.

[**Jupyter Notebook**](https://jupyter.org) is an open-source application that
runs locally in your web-browser and allows you to create documents that
contain both code and text annotations (in Markdown).

<br/>  
<br/>  

### Installing Anaconda

**To install Anaconda:**

* Go to <https://www.anaconda.com/products/individual>.
* Download the version of Anaconda matching your operating system.
* Follow the installer's instructions.

**To test whether your installation is working**, try to launch Jupyter
Notebook:

* Linux/MacOS: open a terminal and type `jupyter-notebook`.
* Windows: in the start menu, search for "Jupyter Notebook (Anaconda)" and
  start the application.

Launching the application should open a new tab in your default web-browser
with the Jupyter Notebook launch page. From there you can browse your computer
for existing notebooks (`.ipynb` files), or you can click on `new` > `Python3`
to open a new empty notebook.

An introduction to Jupyter Notebook will be given at the start of the lecture,
so installing Anaconda and checking that Jupyter Notebook is running is all you
need to do for now.

<br/>  
<br/>  

## Setup 

### Installing Python packages using `pip`

Installing Python packages globally c

### Installing Python packages using `uv`

If you already have Python installed on your system.
[uv]()


```sh
# Create a virtual environment and populate it with all Python packages
# needed for the course.
uv sync

# Start a Jupyter Notebook session in the virtual environment.
uv run jupyter-notebook

# Update virtual environment to the latest version of its Python packages. 
uv sync --upgrade
```