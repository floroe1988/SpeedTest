install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py
	pylint --disable=R,C srcc/GetConnectionSpeed.py
	pylint --disable=R,C srcc/StoreConnectionSpeed.py

all: install lint
