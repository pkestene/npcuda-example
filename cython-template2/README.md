# cython wrapped CUDA/C++ class with templates

This code makes an explicit cython class that wraps the C++ class, exposing it in python. It involves a little bit more repitition than the swig code in principle, but
in practice it's MUCH easier.

Template are handled at python level using generated code (inspired by project pysph
https://bitbucket.org/pysph/pysph)

## build and install

`$ python setup.py install`

or

`$ python setup.py install --user`

if you want to install in $PYTHONUSERBASE

## test

`$ nosetests`

you need a relatively recent version of cython (>=0.16).



