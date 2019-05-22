import jupytext
import nbformat

class TextFileHandler:

    @classmethod
    def read(cls, path):
        """
        Read a notebook using Jupytext
        """
        assert path.startswith('txt://')
        nb = jupytext.readf(path[6:])
        return nbformat.writes(nb, version=4)

    @classmethod
    def write(cls, file_content, path):
        """
        Write a notebook using Jupytext
        """
        assert path.startswith('txt://')
        nb = nbformat.reads(file_content, as_version=4)
        jupytext.writef(nb, path[6:])

    @classmethod
    def pretty_path(cls, path):
        return path

    @classmethod
    def listdir(cls, path):
        raise NotImplementedError
