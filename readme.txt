python3 -m venv env
source env/bin/activate
# make sure requirements.txt has ipykernel in it
pip3 install -r requirements.txt
python -m ipykernel install --user --name=env
