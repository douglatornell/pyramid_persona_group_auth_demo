import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_persona',
    ]

setup(name='pyramid_persona_group_auth_demo',
      version='0.0',
      description='pyramid_persona_group_auth_demo',
      long_description=README,
      classifiers=[
        "Programming Language :: Python :: 2.7",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_persona_group_auth_demo',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyramid_persona_group_auth_demo:main
      [console_scripts]
      initialize_pyramid_persona_group_auth_demo_db = pyramid_persona_group_auth_demo.scripts.initializedb:main
      """,
      )
