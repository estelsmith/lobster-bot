dist_dir = dist
data_dir = data

deps:
	uv sync

.PHONY: build
build: deps cleanbuild
	pyinstaller main.py

.PHONY: clean
clean: cleanbuild
	rm -rf .venv
	rm -rf ${data_dir}

.PHONY: cleanbuild
cleanbuild:
	rm -rf ${dist_dir}
