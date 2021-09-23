default:
	pip3 install -r packages.txt
	pyinstaller enron_search.py --onefile
build:
	pyinstaller enron_search.py --onefile
clean:
	rm -rf *.spec 
	rm -rf dist build __pycache__
