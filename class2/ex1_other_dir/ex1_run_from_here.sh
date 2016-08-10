#!/bin/env bash

echo " "
echo "RUN WITH MY_FUNC IN RANDOM DIRECTORY (../other_lib_dir)"
echo " "
PYTHONPATH=/home/prebert/repos/pynet_cert/class2/other_lib_dir
./ex1_top.py
PYTHONPATH=""

echo " "
echo "RUN WITH MY_FUNC IN ~/applied_python/lib/python2.7/site-packages"
echo ""
cp ../my_func.py ~/applied_python/lib/python2.7/site-packages
./ex1_top.py
rm ~/applied_python/lib/python2.7/site-packages/my_func.py*
exit
