install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py
	pylint --disable=R,C src/GetConnectionSpeed.py
	pylint --disable=R,C src/StoreConnectionSpeed.py

all: install lint
