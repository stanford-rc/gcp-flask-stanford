# Views

This folder is provided as a module, with each set of views presented in its own file, and 
named appropriately:

 - [cardinal.py](cardinal.py) for cardinal themed page and login views
 - [main.py](main.py) provides shared views across themes and the base of the site
 - [api.py](api.py): a example API implementation.

For all of the above, the files are imported in [__init__.py](__init__.py)
so you can pick and choose (e.g., delete the entire api.py and remove it's import)
if you don't need this for your application.
