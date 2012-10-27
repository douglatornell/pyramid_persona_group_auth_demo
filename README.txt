pyramid_persona_group_auth_demo README
======================================

This is a little Pyramid demo app built on the alchemy scaffold.
It shows how to implement authentication via Mozilla Persona in conjunction
with group-level security in the app.

The code is a companion to a blog post I wrote in Oct-2012:
http://douglatornell.ca/blog/2012/10/27/pyramid-persona-group-level-auth
The post source and screen-shot image files are included in the docs/ directory.


Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/initialize_pyramid_persona_group_auth_demo_db development.ini

- $venv/bin/pserve development.ini
