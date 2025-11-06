# Setting-up your environment

Please install Python and the different packages needed for the course
**before the start of the course**.

Several options exist to install Python, we give 3 of them in this document.

<br>  

## Setup using Anaconda 🐍

### Anaconda and Jupyter notebook

[**Anaconda**](https://www.anaconda.com) is an open-source python distribution
that bundles **python 3** along with a large number of useful python modules
such as **SciPy**, **NumPy**, or **Pandas**.

* It also bundles other useful software such as the **conda** package manager
  (which allows easy installation of bioinformatics software) and
  **Jupyter Notebook**.  
* Anaconda is cross-platform and available for Windows, Linux, and MacOS
  operating systems.

[**Jupyter Notebook**](https://jupyter.org) is an open-source application that
runs locally in your web-browser and allows you to create documents that
contain both code and text annotations (in Markdown).

<br>  

### Installing Anaconda

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

<br>  
<br>  

## Setup using Python and `pip` 🌱

1. Download and install Python from its
   [official source](https://www.python.org/downloads).

2. In principle, you should now also have a command named `pip` installed
   (it comes together with Python). You can test it by running:

   ```sh
   python -m pip --version
   python3 -m pip --version   # On some systems, python installs as "python3".
   ```

   > ✨ **Note:** on some systems, Python installs as an executable named
   > `python3`, while on others it installs as `python`.

3. Install the packages needed for the course with `pip`

    ```sh
    pip install -r requirements.txt
    ```

    > 🔥 **Important:** you must be located at the root of the course material
    > directory for the commands to work (in the directory where the
    > `requirements.txt` file is found).

<br>  
<br>  

## Setup using `uv` ⚡

[**`uv`**](https://docs.astral.sh/uv) is a modern Python version and package
manager. To install `uv`, please refer to the
[official documentation](https://docs.astral.sh/uv/#installation).

> ✨ **Note:** using `uv` implies that all your Python package installations
> and command executions will run a so-called "virtual environment". Using
> virtual environments is a good practice, but also adds a (small) extra
> layer of complexity.

<br>

After `uv` is installed, proceed as follow:

1. Install Python, Jupyter notebook and all other Python packages needed the
   course.

    ```sh
    uv sync
    ```

    > 🔥 **Important:** you must be located at the root of the course material
    > directory for the commands to work (in the directory where the
    > `pyproject.toml` file is found).

2. Start a Jupyter Notebook session in the virtual environment.

    ```sh
    uv run jupyter-notebook
    ```

<br>

If at some later point in time you want to update the virtual environment to
the latest version of its Python packages:

```sh
uv sync --upgrade
```
