# Parametrize and run scripts as notebooks with jupytext and papermill

This is on-going research on how to run scripts as notebooks using Jupytext and Papermill. 

The corresponding GitHub issues are
- https://github.com/mwouts/jupytext/issues/231
- https://github.com/nteract/papermill/issues/365

Open and run this document on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mwouts/papermill_jupytext/master?filepath=README.md)

```bash
cd demo
```

## Jupytext and Papermill

It is possible to convert a script to a notebook using Jupytext, and then to run it using Papermill. However, we have to set the kernel information manually:

```bash
jupytext script.py -o notebook.ipynb --update-metadata '{"kernelspec":{"name":"python3", "display_name":"Python 3", "language": "python"}}'
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

Papermill requires kernel information, even if we do not execute the notebook. Since we do not use the kernel here, we may skip the name and display_name fields. However, the language field is required.

```bash
jupytext script.py -o notebook.ipynb --update-metadata '{"kernelspec":{"name":"", "display_name":"", "language": "python"}}'
```

```bash
papermill notebook.ipynb notebook_with_parameters.ipynb --prepare-only -p integer 3 -p text 'updated text, v3'
jupytext notebook_with_parameters.ipynb -o script_with_parameters.py --update-metadata '{"kernelspec":null, "jupytext":null}'
```

```bash
cat script_with_parameters.py
```

```bash
python script_with_parameters.py
```

## Towards Papermill + Jupytext?

With the `papermill_jupytext` package, we can open Jupytext scripts with the `txt://` address. Again, before we can open a script as a notebook with `papermill`, we need to inject a kernel information into it:

```bash
jupytext script.py -o script_with_kernel_info.py --update-metadata '{"kernelspec":{"name":"python3", "display_name":"Python 3", "language": "python"}}'
```

```bash
papermill txt://script_with_kernel_info.py executed_notebook.ipynb  -p integer 4 -p text 'updated text, v4'
```

```bash
python -c "import nbformat
with open('executed_notebook.ipynb') as fp:
    nb = nbformat.read(fp, as_version=4)
print(nb.cells[-1]['outputs'][0]['text'])"
```
