Instagram-DL
===========

A simple package to download videos, and reels from Instagram. Easily save public content or your own account data by providing the post URL.


Split your code into packages, modules, and functions
-----------------------------------------------------

- All code should be inside some function (except perhaps ``if __name__ == '__main__':``).
- Split long functions into smaller functions.
- If you need to scroll through a function over several screens, it is probably too long.
- Functions should do one thing and one thing only.
- Hide internals with underscores.
- Organize related functions into modules.
- If modules grow too large, split them.
- Import from other modules under ``somepackage/`` using ``from .somemodule import something``.
- Do file I/O on the "outside" of your code, not deep inside.


Classes vs. functions
---------------------

- Do not overuse classes.
- Prefer immutable data structures.
- Prefer pure functions.


Naming
------

- Give the subdirectory the same name as your package.
- Before you name your package, check that the name is not taken on https://pypi.org
  (you may want to upload your package to PyPI one day).


Interfaces
----------

- In ``somepackage/__init__.py`` define what should be visible to the outside.
- Use https://semver.org.


Testing
-------

- Test all non-trivial code. I recommend to use https://pytest.org.
- Use Travis CI: https://docs.travis-ci.com/user/languages/python/.


Dependency management
---------------------

- Package dependencies for developers should be listed in ``requirements.txt``.
- Alternatively, consider using http://pipenv.readthedocs.io.
- Package dependencies for users of your code (who will probably install via pip) should be listed in ``setup.py``.


Code style
----------

- Follow PEP8: https://www.python.org/dev/peps/pep-0008/
- Use ``pycodestyle`` to automatically check for PEP8.


Type checking
-------------

- Consider using type hints: https://docs.python.org/3/library/typing.html
- Consider using http://mypy-lang.org.
- Consider verifying type annotations at runtime: https://github.com/RussBaz/enforce


Share your package
------------------

- Choose a license and add a LICENSE file.
- Share your package on PyPI. For this you can follow https://github.com/bast/pypi-howto.


Documentation
-------------

I used to recommend reStructuredText for READMEs in contrast to Markdown but
PyPI no longer requires reStructuredText. You can use Markdown as noted on
https://pypi.org/help/ under "How can I upload a project description in a
different format?".

Example shown here: https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py


Suggestions? Corrections? Pull requests?
----------------------------------------

Yes please!
