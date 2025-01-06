
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10829064.svg)](https://doi.org/10.5281/zenodo.10829064)

# First steps with Python in Life Sciences

This is the course material of the "First Steps with Python in Life Science"
three-day course of [SIB-training](https://www.sib.swiss/training/who-can-benefit)

The course is addressed to **beginners** wanting to become familiar with the
Python syntax, environment, and the most common commands.

This course material provides an introduction to [python](https://www.python.org)
and [jupyter notebooks](https://www.jupyter.org), a web based notebook system
for creating and sharing computational documents in an interactive manner.

<br>

## Prerequisites installation

Please ensure you have installed all the required software as indicated in the
**[environment setup](setting_up_your_environment.md)** section
**before the start of the course**.

<br>

## Useful links

* **Course material**: the easiest way to get the course material is to
  download the `.zip` file of the latest release that is available by
  **[clicking on this link](https://github.com/sib-swiss/first-steps-with-python-training/releases/latest)**.
* **[Google doc](https://docs.google.com/document/d/1S8Pbm6AaA_J6SNCLURmvGQRRSFHA43wVJR-P9ZQQYzo/edit?usp=sharing)**:
  can be used to ask questions (especially for courses taught online) or
  otherwise provide a mean of communication between participants and trainers
  (e.g. to share code snippets).

<br>

## Course material organization

The course revolves around a series of jupyter notebooks that take you on your
first steps in you python journey.

Each jupyter notebook interleaves theory, code examples and exercises. We
heartily recommend you execute and play around with these bits of code as you
follow along: in programming, perhaps more than anywhere else, practice makes
perfect.

Additionally, each notebook is associated with a number of **exercises**
(generally in a separate notebook). **Corrections are provided** for all
exercises.

If you are attending this course with a teacher (or if you are just curious),
you can take a look at our [schedule](schedule_and_structure.md).

In short, lessons 0 to 4 deal with general aspect of the python language,
while notebooks 5 to 8 present some of the most common modules used in data
analysis and/or life sciences.

The [`notebooks/`](notebooks/) directory contains each lesson:

* [00_jupyter_setup](notebooks/00_jupyter_setup.ipynb)
* [01_python_basics](notebooks/01_python_basics.ipynb)
* [02_python_structures](notebooks/02_python_structures.ipynb)
* [03_reading_writing_files](notebooks/03_reading_writing_files.ipynb)
* [04_modules](notebooks/04_modules.ipynb)
* [05_module_pandas](notebooks/05_module_pandas.ipynb): handle tabular data
  data-frames with [pandas](https://pandas.pydata.org/)
* [06_module_matplotlib](notebooks/06_module_matplotlib.ipynb): create nice
  graphics and plots with [matplotlib](https://matplotlib.org/)
* [07_module_biopython](notebooks/07_module_biopython.ipynb) : do all kind of
  bioinformatics with [biopython]](<https://biopython.org/>)
* [08_module_numpy_and_scipy](notebooks/08_module_numpy_and_scipy.ipynb): fast
  numerical computations with [numpy](https://numpy.org/) + a bit of statistics
  with [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html).

Exercise notebooks:

* [01_python_basics_exercises](notebooks/01_python_basics_exercises.ipynb)
* [02_python_structures_exercises](notebooks/02_python_structures_exercises.ipynb)
* [03_reading_writing_files_exercises](notebooks/03_reading_writing_files_exercises.ipynb)
* [04_modules_exercises](notebooks/04_modules_exercises.ipynb)
* [05_module_pandas_exercises](notebooks/05_module_pandas_exercises.ipynb)
* [06_module_matplotlib_exercises](notebooks/06_module_matplotlib_exercises.ipynb)
* [07_module_biopython_exercises](notebooks/07_module_biopython_exercises.ipynb)

Data and solutions:

* The data used in the practicals can be found in the
[`notebooks/data`](notebooks/data/) directory.
* Solutions can be found in the [`notebooks/solutions/`](notebooks/solutions/)
  directory, but can also be loaded directly from the exercise notebooks.

<br>

## Course description

### Overview

Have you ever been stuck with a file format that doesn't precisely conform to
your needs, found yourself doing annoyingly repetitive data manipulations, or
struggled to efficiently manage and explore your data? Python to the rescue!

Python is an **open-source and general-purpose programming language** which
runs on all major operating systems. It was designed to be easily read and
written with a comparatively simple syntax, and is thus a good choice for
beginners in programming.

Python is applied in many disciplines and is
**one of the most common languages for bioinformatics**. The Python community
enthusiastically maintains a rich collection of libraries/modules for
everything from web development to machine learning.

In this **3-days course for beginners**, participants will learn the basic
concepts, data types and code structures necessary to solve routine data
manipulation tasks.
It also covers the concepts, terminology, and approach to documentation
required to further develop skills in Python programming independently, helping
participants to take control of their research questions in an independent
manner.

Topics covered by this course include:

* A basic introduction to Python and computing in general.
* Overview of the basic data types in python, such as strings, numbers, lists,
  tuples, and dictionaries.
* Overview of the basic code structures: if/else, for loops and functions.
* Writing your own functions.
* Reading from and writing to files.
* Best practices in Python programming.
* Debugging and documentation.
* Installing and importing external libraries/modules.
* Introduction to some useful python libraries in data science: pandas,
  matplotlib, scipy, numpy, biopython (note: participants can elect the modules
  they wish to look at, so not everyone will go through all libraries).

### Audience

The course is addressed to **beginners** who want to become familiar with
writing Python code to accomplish common tasks such as automated data parsing,
basic statistical operations and graphical representations.

For people who are proficient in programming: this course might be on the
**slow side** for you and an intermediate python class is recommended (check
regularly our upcoming training courses).

### Learning objectives

By the end of this course, participants will be familiar with the following
basic python concepts:

* Basic data types in python (strings, numbers, lists,  tuples, dictionaries).
* Basic code structures: if/else, for loops and functions.
* Writing functions.
* Reading from and writing to files.
* Installing and importing external libraries/modules.
* Debugging and documentation.

Participants will also gain an overview of the Python ecosystem and some of
its popular libraries in data science and bioinformatics. The basic concepts
learned in the course should also enable them to further self-study specific
topics of interest and/or attend more advanced python training courses.

### Prerequisites

#### Knowledge / competencies

This course is designed for beginners; there is no requirement for previous
knowledge in Python or programming. However, we encourage people to be have
some familiarity with basic shell/terminal commands (e.g. navigating the
filesystem in command line). For people with no experience of shell commands,
we recommend either taking the SIB's "First Steps with UNIX" course, or
completing the SIB's ["First Steps with UNIX" e-learning module](https://edu.sib.swiss/pluginfile.php/2878/mod_resource/content/4/couselab-html/content.html).
Basic concepts of algorithmics is also a plus for this course.

#### Technical

Participants are required to have their own laptop with a reasonably recent
version of Python installed (version `>= 3.10`), as well as the
[jupyter notebook](https://jupyter.org) environment.

For this course, we suggest to install Python via
[Anaconda](https://docs.continuum.io) - a free and
operating system (OS)-agnostic platform for installing Python libraries and
environments. Anaconda is bundled with Anaconda Navigator, a graphical user
interface which will help ease you into what Python makes possible. For
details, please see the **[environment setup](setting_up_your_environment.md)**
section of the course webpage.

<br>

## Citation

If you use/reuse this material, please cite as:

Robin Engler, Wandrille Duchemin, & Orlin Topalov. (2024, March 18). Course
material First steps with Python in Life Sciences.
Zenodo, https://doi.org/10.5281/zenodo.10829064.
