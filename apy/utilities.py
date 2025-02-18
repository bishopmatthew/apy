"""Simple utility functions."""

import os


class cd:
    """Context manager for changing the current working directory"""

    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def editor(filepath):
    """Use EDITOR to edit file at given path"""
    import os
    from subprocess import call
    return call([os.environ.get('EDITOR', 'vim'), filepath])

def edit_text(input_text, prefix=None):
    """Use EDITOR to edit text (from a temporary file)"""
    import os
    import tempfile

    if prefix is not None:
        prefix = prefix + "_"

    with tempfile.NamedTemporaryFile(mode='w+',
                                     dir=os.getcwd(),
                                     prefix=prefix,
                                     suffix=".md") as tf:
        tf.write(input_text)
        tf.flush()
        editor(tf.name)
        tf.seek(0)
        edited_message = tf.read().strip()

    return edited_message

def choose(items, text="Choose from list:"):
    """Choose from list of items"""
    import readchar
    import click

    click.echo(text)
    for i, element in enumerate(items):
        click.echo(f"{i+1}: {element}")
    click.echo("> ", nl=False)

    while True:
        choice = readchar.readchar()

        try:
            index = int(choice)
        except ValueError:
            continue

        try:
            reply = items[index-1]
            click.echo(index)
            return reply
        except IndexError:
            continue
