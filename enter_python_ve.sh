#
# Call this script as a bash include. 
# . ./enter_python_ve.py # Note the dot space dot slash

virtualenv ve
. ./ve/bin/activate
pip install -q nose
