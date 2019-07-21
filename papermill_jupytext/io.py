import os
import nbformat
import jupytext
from jupytext.kernels import kernelspec_from_language


def _resolved_handler(resolved_path):
    import papermill
    return papermill.iorw.papermill_io.get_handler(resolved_path)


class TextFileHandler:
    @classmethod
    def extract_format(cls, path):
        if not path.startswith('txt://'):
            raise ValueError('Expected a path of the form txt://[s3://]path/to/script.py, but got {}'.format(path))

        return path[6:], os.path.splitext(path)[1]

    @classmethod
    def read(cls, path):
        resolved_path, fmt = cls.extract_format(path)
        text = _resolved_handler(resolved_path).read(resolved_path)

        # Read the document
        nb = jupytext.reads(text, fmt=fmt)

        # Set a kernel if there was none
        if nb.metadata.get('kernelspec', {}).get('name') is None:
            language = nb.metadata.get('jupytext', {}).get('main_language') or nb.metadata['kernelspec']['language']
            if not language:
                raise ValueError('Cannot infer a kernel as the document language is not defined')

            kernelspec = kernelspec_from_language(language)
            if not kernelspec:
                raise ValueError('Found no kernel for {}'.format(language))

            nb.metadata['kernelspec'] = kernelspec

        # Return the notebook as a JSON string
        return nbformat.writes(nb)

    @classmethod
    def write(cls, buf, path):
        resolved_path, fmt = cls.extract_format(path)

        # Read the notebook from its JSON representation
        nb = nbformat.reads(buf, as_version=4)

        # Write the notebook in its Jupytext representation
        text = jupytext.writes(nb, fmt=fmt)

        return _resolved_handler(resolved_path).write(text, resolved_path)

    @classmethod
    def pretty_path(cls, path):
        resolved_path, _ = cls.extract_format(path)
        pretty_path = _resolved_handler(resolved_path).pretty_path(resolved_path)
        return 'txt://' + pretty_path

    @classmethod
    def listdir(cls, path):
        resolved_path, _ = cls.extract_format(path)
        return _resolved_handler(resolved_path).listdir(resolved_path)
