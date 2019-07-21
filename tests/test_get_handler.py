import papermill_jupytext
from papermill import iorw


def test_get_handler(path='txt://script.py'):
    handler = iorw.papermill_io.get_handler(path)
    assert handler == papermill_jupytext.TextFileHandler
