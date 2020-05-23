make:
	python -m venv venv
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
		python -m eel main.py web --onefile --noconsole; \
	)

clean:
	rm -rf build dist __pycache__ venv
