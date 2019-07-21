import jupytext
import papermill as pm


def test_inject_param_in_script(tmpdir):
    tmp_py = str(tmpdir.join('script.py'))

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
        'txt://' + tmp_py,
        parameters=dict(integer=2),
        prepare_only=True
    )

    nb = jupytext.read(tmp_py, as_version=4)
    assert len(nb.cells) == 3
    assert 'integer = 2' in nb.cells[1].source
