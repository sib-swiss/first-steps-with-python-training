

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6541379.svg)](https://doi.org/10.5281/zenodo.6541379)


# First steps with Python in Life Sciences

This course material is part of the "First Steps with Python in Life Science" three-day course of [SIB-training](https://www.sib.swiss/training/who-can-benefit) and is addressed to beginners wanting to become familiar with the Python syntax, environment, and the most common commands.

This course material provides an introduction to [python](https://www.python.org/) and [jupyter notebooks](https://www.jupyter.org/) (a web based notebook system for creating and sharing computational documents) in an interactive manner. 


## prerequisite installation

You can find [tips and instructions](setting_up_your_environment.md) to ensure you have installed all the required software before starting the course.

## course material organization

The course revolves around a sery of jupyter notebooks which take you on your first steps in you python journey.

Each jupyter notebook interleaves theory and examples of codes. We heartily recommend you execute and play around with these bits of code as you follow along : in programming, perhaps even more than anywhere else, practice makes perfect.

Additionally, each notebook is associated with a number of exercises (often in a separate notebook) of varying difficulty, with associated corrections.

If you are attending this course with a teacher (or if you are just curious), you can take a look at our [schedule](schedule_and_structure.md).
In short, lessons 00 to 04 deals with generalistic aspect of the python language, while notebooks 05 or 08 present some of the most common modules used in data analysis and/or life sciences.

The [`notebooks/`](notebooks/) folder contains each lesson:
 * [00_jupyter_setup](notebooks/00_jupyter_setup.ipynb)
 * [01_python_basics](notebooks/01_python_basics.ipynb)
 * [02_python_structures](notebooks/02_python_structures.ipynb)
 * [03_reading_writing_files](notebooks/03_reading_writing_files.ipynb)
 * [04_modules](notebooks/04_modules.ipynb)
 * [05_module_pandas](notebooks/05_module_pandas.ipynb) : handle tabular data data-frames with [pandas](https://pandas.pydata.org/)
 * [06_module_matplotlib](notebooks/06_module_matplotlib.ipynb) : create nice graphics and plots with [matplotlib](https://matplotlib.org/)
 * [07_module_biopython](notebooks/07_module_biopython.ipynb) : do all kind of bioinformatics with [biopython]](https://biopython.org/)
 * [08_module_numpy_and_scipy](notebooks/08_module_numpy_and_scipy.ipynb) : fast numerical computations with [numpy](https://numpy.org/) + a bit of statistics with [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) 


Exercise notebooks:
 * [01_python_basics_exercises](notebooks/01_python_basics_exercises.ipynb)
 * [02_python_structures_exercises](notebooks/02_python_structures_exercises.ipynb)
 * [03_reading_writing_files_exercises](notebooks/03_reading_writing_files_exercises.ipynb)
 * [04_modules_exercises](notebooks/04_modules_exercises.ipynb)
 * [05_module_pandas_exercises](notebooks/05_module_pandas_exercises.ipynb)
 * [06_module_matplotlib_exercises](notebooks/06_module_matplotlib_exercises.ipynb)
 * [07_module_biopython_exercises](notebooks/07_module_biopython_exercises.ipynb)

The data used in the practicals can be found in the data [`notebooks/data`](notebooks/data/) folder, and
solutions codes can be found in the [`notebooks/solutions/`](notebooks/solutions/) folder (NB: micro-exercises do not have a correction).


## citation

If you use/reuse this material, please cite as:
Robin Engler, Wandrille Duchemin, & Orlin Topalov. (2022, May 12). Course material First steps with Python in Life Sciences. Zenodo. https://doi.org/10.5281/zenodo.6541379
