
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8376825.svg)](https://doi.org/10.5281/zenodo.8376825)

# First steps with Python in Life Sciences

This is the course material of the "First Steps with Python in Life Science"
three-day course of [SIB-training](https://www.sib.swiss/training/who-can-benefit)

The course is addressed to beginners wanting to become familiar with the
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

## Citation

If you use/reuse this material, please cite as:

Robin Engler, Wandrille Duchemin, & Topalov, O. (2023, September 25). Course material First steps with Python in Life Sciences. Zenodo. https://doi.org/10.5281/zenodo.8376825
