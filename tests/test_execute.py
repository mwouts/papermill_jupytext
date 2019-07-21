import os
import nbformat
import papermill as pm


def test_execute_markdown(tmpdir):
    tmp_md = str(tmpdir.join('markdown.md'))
    tmp_ipynb = str(tmpdir.join('executed.ipynb'))

    with open(tmp_md, 'w') as fp:
        fp.write("""```python tags=["parameters"]
# This cell defines the default value for parameters
integer = 1
text = "default"
```

```python
print('Parameters are {}'.format({'integer': integer, 'text': text}))
```
""")

    pm.execute_notebook(
        'txt://' + tmp_md,
        tmp_ipynb,
        parameters=dict(integer=2)
    )

    assert os.path.isfile(tmp_ipynb)
    nb = nbformat.read(tmp_ipynb, as_version=4)
    assert len(nb.cells) == 3


def test_execute_script(tmpdir):
    tmp_py = str(tmpdir.join('script.py'))
    tmp_ipynb = str(tmpdir.join('executed.ipynb'))

    with open(tmp_py, 'w') as fp:
        fp.write("""# %% {"tags": ["parameters"]}
# This cell defines the default value for parameters
integer = 1
text = "default"

# %%
print('Parameters are {}'.format({'integer': integer, 'text': text}))
""")

    pm.execute_notebook(
        'txt://' + tmp_py,
        tmp_ipynb,
        parameters=dict(integer=2)
    )

    assert os.path.isfile(tmp_ipynb)
    nb = nbformat.read(tmp_ipynb, as_version=4)
    assert len(nb.cells) == 3
