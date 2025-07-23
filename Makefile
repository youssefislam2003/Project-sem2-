.PHONY: test run clean

# Run pytest on all test files
test:
	@echo "Running tests..."
	@venv/bin/pytest -v

# Run the main program
run:
	@echo "Running main program..."
	@venv/bin/python Main_class.py

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -f output.txt multi_output.txt
	rm -rf __pycache__ .pytest_cache
