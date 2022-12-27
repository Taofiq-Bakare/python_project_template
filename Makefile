# To automate my development process


# generate hashes from the .in file 
# and add output it to the requirements file
get-requirements:
	python -m piptools compile --generate-hashes requirements/prod_requirements.in --output-file requirements/prod_requirements.txt &&\
	python -m piptools compile --generate-hashes requirements/dev_requirements.in --output-file requirements/dev_requirements.txt 

# install the basic tools needed for the environment
install:
	python -m pip install --upgrade pip &&\
	python -m pip install --upgrade pip-tools

install-prod: get-requirements install 
	python -m pip install -r requirements/prod_requirements.txt

install-dev: get-requirements 
	python -m pip install -r requirements/dev_requirements.txt

install-all: get-requirements install-dev install-prod

