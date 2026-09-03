SHELL := /bin/bash

.PHONY: install run run_sh unlock_files clean create_private_folders generate_dot_env

PYTHON=$(shell which python3)
ifeq ($(PYTHON),)
	PYTHON=$(shell which python)
	ifneq ($(PYTHON),)
		ifeq ($(shell $(PYTHON) -V | grep '^Python 3'),)
			PYTHON=
		endif
	endif
endif


PYTHON = ./.venv/bin/python

WORKDIR=pdf_statements_unlock


install:  ## Install poetry to run on local
	$(MAKE) generate_dot_env
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install poetry
	$(PYTHON) -m poetry install
	poetry run pre-commit install

run: ## run the program
	clear
	PYTHONPATH=$(WORKDIR)/ $(PYTHON) pdf_statements_unlock/main.py

run_sh: ## run the program via the shell wrapper (keeps terminal open)
	bash run.sh

unlock_files: ## batch-unlock all PDFs in private_data/files
	clear
	$(PYTHON) scripts/unlock_files.py

clean:
	rm -rf __pycache__

create_private_folders:  ## Create private_data folder
	@mkdir -p private_data/credit_cards
	@echo "Created folder: private_data/credit_cards"


generate_dot_env:  ## Create .env from template if it does not exist.
	@if [[ ! -e .env ]]; then \
		cp .env.template .env; \
	fi
