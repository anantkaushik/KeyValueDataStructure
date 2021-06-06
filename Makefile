PYTHON = python3

# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

test:
	${PYTHON} -m unittest test_kv_ds.py

run:
	${PYTHON} service.py
