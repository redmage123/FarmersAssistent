# Makefile for Farmers Assistant Flask Application

# Define commands
PYTHON = python
PIP = pip
FLASK = flask
BLACK = black
FLAKE8 = flake8

# Define paths
REPO_ROOT = /workspaces/codespace_demo/farmersassistent
VENV_DIR = $(REPO_ROOT)/.venv
APP_DIR = $(REPO_ROOT)/farmers_assistant
SRC_DIR = $(APP_DIR)/farmers_assistant

# Default target executed when no arguments are given to make.
default: run

# Setup the Python Virtual Environment
setup:
	@echo "Setting up Python virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(VENV_DIR)/bin/$(PIP) install -r $(REPO_ROOT)/requirements.txt

# Function to check if the virtual environment is active
define check_venv
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Activating virtual environment..."; \
		. $(VENV_DIR)/bin/activate; \
	fi;
endef

# Rebuild requirements.txt from the current virtual environment
rebuild-requirements:
	$(call check_venv)
	@echo "Rebuilding requirements.txt..."
	$(VENV_DIR)/bin/$(PIP) freeze > $(REPO_ROOT)/requirements.txt

# Run the Flask application
run:
	$(call check_venv)
	@echo "Running Flask application..."
	FLASK_APP=$(SRC_DIR)/main.py $(FLASK) run

# Lint the code
lint:
	$(call check_venv)
	@echo "Linting the code..."
	$(FLAKE8) $(SRC_DIR)

# Format the code
format:
	$(call check_venv)
	@echo "Formatting the code..."
	$(BLACK) $(SRC_DIR)

# Clean up the project (e.g., remove virtual environment)
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)

# Help command to display available commands
help:
	@echo "Available commands:"
	@echo "  setup                - Set up the Python virtual environment and install dependencies"
	@echo "  run                  - Run the Flask application"
	@echo "  lint                 - Lint the code using flake8"
	@echo "  format               - Format the code using black"
	@echo "  rebuild-requirements - Rebuild requirements.txt from the current virtual environment"
	@echo "  clean                - Clean up the project (remove virtual environment)"
	@echo "  help                 - Display this help message"

# Phony targets are not files
.PHONY: default setup run lint format rebuild-requirements clean help

