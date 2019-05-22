# Parametrize and run scripts as notebooks with jupytext and papermill

This is an experiment for running scripts as notebooks using Jupytext and Papermill.

```bash
cd demo
```

## Jupytext and Papermill

We need to set the kernel information on the script.

```bash
jupytext script.py -o notebook.ipynb --update-metadata '{"kernelspec":{"name":"python3", "display_name":"Python 3", "language": "python"}}'
papermill notebook.ipynb executed_notebook.ipynb -p integer 2 -p text 'updated text'
cat executed_notebook.ipynb
```

## Inject parameters in a script using Papermill

Fake kernel information is required...

```bash
jupytext script.py -o notebook.ipynb --update-metadata '{"kernelspec":{"name":"", "display_name":"", "language": "python"}}'
papermill notebook.ipynb notebook_with_parameters.ipynb --prepare-only -p integer 3 -p text 'updated text, v3'
jupytext notebook_with_parameters.ipynb -o script_with_parameters.py --update-metadata '{"kernelspec":null, "jupytext":null}'
cat script_with_parameters.py
python script_with_parameters.py
```

## Towards Papermill + Jupytext?

Requires `papermill_jupytext`.

```bash
jupytext script.py -o script_with_kernel_info.py --update-metadata '{"kernelspec":{"name":"python3", "display_name":"Python 3", "language": "python"}}'
papermill txt://script_with_kernel_info.py executed_notebook.ipynb  -p integer 4 -p text 'updated text, v4'
cat executed_notebook.ipynb
```
