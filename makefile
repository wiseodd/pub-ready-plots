test:
	uv run pytest --cov

ruff:
	-uv run ruff format
	@uv run ruff check --fix

mypy:
	uv run mypy --config-file mypy.ini pub_ready_plots

lint:
	make ruff
	make mypy
