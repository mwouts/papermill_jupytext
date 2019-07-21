# Parametrize and run scripts as notebooks with jupytext and papermill

This is on-going research on how to run scripts as notebooks using Jupytext and Papermill. 

The corresponding GitHub issues are [Jupytext #231](https://github.com/mwouts/jupytext/issues/231) and [Papermill #365](https://github.com/nteract/papermill/issues/365).

Open this document and run it as a notebook on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mwouts/papermill_jupytext/master?filepath=README.md)

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

With the `papermill_jupytext` package, we can open Jupytext scripts with the `txt://` address. Again, before we can open a script as a notebook with `papermill`, we need to inject a kernel information into it:

```bash
jupytext script.py -o script_with_kernel_info.py --set-kernel -
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
