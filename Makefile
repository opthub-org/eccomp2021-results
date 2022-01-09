all: venv data scores submissions

venv:
	python -m venv venv
	. venv/bin/activate; \
	pip install -U pip; \
	pip install -r requirements.txt

data: venv
	mkdir -p data
	. venv/bin/activate; \
	for i in `seq 41 46`; do echo $$i; python match.py $$i > data/$$i.json; done; \
	for i in 2021-{10..12}-{01..31}; do echo $$i; python stats.py $$i > data/stats_$$i.json; done

scores: data
	mkdir -p scores
	. venv/bin/activate; \
	python scores.py

submissions: data
	mkdir -p submissions
	. venv/bin/activate; \
	python submissions.py

clean:
	$(RM) -rf venv data scores submissions
