.PHONY: init

env:
	python -m venv env; \
	./env/Scripts/activate;

init: env
	pip install -r requirements.txt

