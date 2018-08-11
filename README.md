# init virtualenv

virtualenv --python=python3.6 pythonblog
source pythonblog/bin/activate
pip install django~=1.11.0
python manage.py migrate


# run local server

source pythonblog/bin/activate

python manage.py runserver

# look  http://localhost:8000/
