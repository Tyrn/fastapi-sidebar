Google Bookmarks
****************

Netscape Bookmarks parsers
==========================

Doctype: <!DOCTYPE NETSCAPE-Bookmark-file-1>

- JS: `to JSON
  <https://gist.github.com/devster31/4e8c6548fd16ffb75c02e6f24e27f9b9>`__;
  `cheerio <https://github.com/cheeriojs/cheerio>`__,
  `tutorial <https://zetcode.com/javascript/cheerio/>`__
- Python:
  `to HTML <https://github.com/FlyingWolFox/Netscape-Bookmarks-File-Parser>`__

Install and run
===============

- The project makes use of the `nodeenv <https://pypi.org/project/nodeenv/>`__
  package

::

    $ poetry install
    $ poetry shell
    (.venv) $ nodeenv -p
    (.venv) $ nodeenv -r node-requirements.txt --update .venv

- The environment may not be quite ready; exit it (Ctrl-d in case of
  poetry shell) once before regular use.

- Do not use ``poetry run uvicorn ...`` alongside ``nodeenv``.
  Start this way:

::

    $ poetry shell
    (.venv) $ uvicorn <path.to>:<app> --reload

Initial install and freeze
--------------------------

::

    (.venv) $ nodeenv -p
    (.venv) $ npm install -g cheerio
    (.venv) $ freeze node-requirements.txt
