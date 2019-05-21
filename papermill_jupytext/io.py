import jupytext


class TextFileHandler:

    @classmethod
    def read(cls, path):
        """
        Read a notebook using Jupytext
        """
        return jupytext.readf(path)

    @classmethod
    def write(cls, file_content, path):
        """
        Write a notebook using Jupytext
        """
        jupytext.writef(file_content, path)

    @classmethod
    def pretty_path(cls, path):
        return path

    @classmethod
    def listdir(cls, path):
        raise NotImplementedError
