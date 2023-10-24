all: check-styles check-types fix-styles test run 

test:
	pytest test_HvertSkalMaeta.py
	pytest test_unit_HvertSkalMaeta.py
	
run:
	@cat data/1.in | python HvertSkalMaeta.py | diff - data/1.ans
	@cat data/2.in | python HvertSkalMaeta.py | diff - data/2.ans
	@echo "All kattis sample test data test done..."

check-types:
	mypy --disallow-untyped-defs --strict HvertSkalMaeta.py
	mypy --disallow-untyped-defs --strict test_HvertSkalMaeta.py
	mypy --disallow-untyped-defs --strict test_unit_HvertSkalMaeta.py

check-styles:
	flake8 HvertSkalMaeta.py
	flake8 test_HvertSkalMaeta.py
	flake8 test_unit_HvertSkalMaeta.py

fix-styles:
	autopep8 HvertSkalMaeta.py
	autopep8 test_HvertSkalMaeta.py
	autopep8 test_unit_HvertSkalMaeta.py

submit-kattis:
	@python ../kattis-cli/submit.py -f -p hvertskalmaeta HvertSkalMaeta.py

