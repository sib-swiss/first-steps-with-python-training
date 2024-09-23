# Setting-up your environment

Please install the following software on your personal laptop
**before the start of the course**.

<br/>  
<br/>  

## Anaconda and Jupyter notebook

[**Anaconda**](https://www.anaconda.com) is an open-source python distribution
that bundles **python3** along with a large number of useful python modules
such as **SciPy**, **NumPy**, or **Pandas**.

* It also bundles other useful software such as the **conda** package manager
  (which allows easy installation of bioinformatics software) and
  **Jupyter Notebook**.  
* Anaconda is cross-platform and available for Windows, Linux, and MacOS
  operating systems.
  
> According to anaconda [Terms of Services](https://legal.anaconda.com/policies/en/#purchased-vs-free-offerings), the [use of the conda software is free BUT the use of the "conda channel" is not](https://www.anaconda.com/blog/is-conda-free) except in very specific conditions and so users relying on the default channels could eventually get billed (or rather, their university department may). This is why in the instructions below we point to the conda-forge installer which sets up the free conda-forge channel instead of the default.

<br/>  

[**Jupyter Notebook**](https://jupyter.org) is an open-source application that
runs locally in your web-browser and allows you to create documents that
contain both code and text annotations (in Markdown).

<br/>  
<br/>  

## Installing anaconda

**To install anaconda:**

* Go to <https://conda-forge.org/download/>.
* Download the version of conda-forge matching your operating system.
* Follow the installer's instructions.

**To test whether your installation is working**, try to launch Jupyter
Notebook:

* Linux/MacOS: open a terminal and type `jupyter-notebook`.
* Windows: in the start menu, search for "Jupyter Notebook (Anaconda)" and
  start the application.
  
> if the command above fails, or if you are not able to find the Jupyter Notebook application, then it is possible that you have to first install a library. You can either use the command line (mac or linux)
>
> `conda install -y -c conda-forge ipykernel` 
> 
> or use the [anaconda navigation GUI](https://docs.anaconda.com/navigator/getting-started/#managing-packages) to install the ipykernel package 
>


Launching the application should open a new tab in your default web-browser
with the Jupyter Notebook launch page. From there you can browse your computer
for existing notebooks (`.ipynb` files), or you can click on `new` > `Python3`
to open a new empty notebook.

An introduction to Jupyter Notebook will be given at the start of the lecture,
so installing anaconda and checking that Jupyter Notebook is running is all you
need to do for now.
