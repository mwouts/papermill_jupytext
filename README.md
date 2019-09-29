# Parametrize and run scripts as notebooks with jupytext and papermill

[![Build Status](https://travis-ci.com/mwouts/papermill_jupytext.svg?branch=master)](https://travis-ci.com/mwouts/papermill_jupytext)
[![codecov.io](https://codecov.io/github/mwouts/papermill_jupytext/coverage.svg?branch=master)](https://codecov.io/github/mwouts/papermill_jupytext?branch=master)
[![Language grade: Python](https://img.shields.io/badge/lgtm-A+-brightgreen.svg)](https://lgtm.com/projects/g/mwouts/papermill_jupytext/context:python)
[![Pypi](https://img.shields.io/pypi/v/papermill_jupytext.svg)](https://pypi.python.org/pypi/papermill_jupytext)
[![pyversions](https://img.shields.io/pypi/pyversions/papermill_jupytext.svg)](https://pypi.python.org/pypi/papermill_jupytext)
[![CFM insights](https://img.shields.io/badge/CFM%20insights-Jupytext%20&%20Papermill-00ab6c.svg)](https://medium.com/capital-fund-management/automated-reports-with-jupyter-notebooks-using-jupytext-and-papermill-619e60c37330)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mwouts/papermill_jupytext/master?filepath=README.md)

This is on-going research on how to run scripts as notebooks using Jupytext and Papermill. 

The corresponding GitHub issues are [Jupytext #231](https://github.com/mwouts/jupytext/issues/231) and [Papermill #365](https://github.com/nteract/papermill/issues/365). See also our article on [Jupytext and Papermill](https://medium.com/capital-fund-management/automated-reports-with-jupyter-notebooks-using-jupytext-and-papermill-619e60c37330) in _CFM Insights_.

Note that the below is a Bash Jupyter notebook that is [tested on our CI](https://github.com/mwouts/papermill_jupytext/blob/10dd863304614dd0c6328c859a077b52ba3c9822/.travis.yml#L29). If you wish, you can also open and run it interactively on [Binder](https://mybinder.org/v2/gh/mwouts/papermill_jupytext/master?filepath=README.md).

```bash
cd demo
```

## Jupytext and Papermill

It is possible to convert a script to a notebook using Jupytext, and then to run it using Papermill. Here we use `--set-kernel -` to use the kernel that matches the current Python environment.

```bash
jupytext script.py -o notebook.ipynb --set-kernel -
```

```bash
papermill notebook.ipynb executed_notebook.ipynb -p integer 2 -p text 'updated text'
```

```bash
python -c "import nbformat
with open('executed_notebook.ipynb') as fp:
    nb = nbformat.read(fp, as_version=4)
print(nb.cells[-1]['outputs'][0]['text'])"
```

## Inject parameters in a script using Papermill

Papermill needs the language information in the kernel to inject the parameters in the notebooks, so in this case we also need to set a kernel for the notebook.

```bash
jupytext script.py -o notebook.ipynb --set-kernel -
```

```bash
papermill notebook.ipynb notebook_with_parameters.ipynb --prepare-only -p integer 3 -p text 'updated text, v3'
```

Once the parameters have been injected, we can convert back the notebook to a script, and drop the kernel information:

```bash
jupytext notebook_with_parameters.ipynb -o script_with_parameters.py --update-metadata '{"kernelspec":null, "jupytext":null}'
```

```bash
cat script_with_parameters.py
```

And finally, we run the script using the Python interpreter:

```bash
python script_with_parameters.py
```

## Towards Papermill + Jupytext?

With the `papermill_jupytext` package, we can open Jupytext scripts with the `txt://` address. A kernel pointing to the current Python environment is injected in the documents that have no kernel.

```bash
papermill txt://script.py executed_notebook.ipynb  -p integer 4 -p text 'updated text, v4'
```

```bash
python -c "import nbformat
with open('executed_notebook.ipynb') as fp:
    nb = nbformat.read(fp, as_version=4)
print(nb.cells[-1]['outputs'][0]['text'])"
```
