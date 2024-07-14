.PHONY: run run-test publish-release

run:
	python3 setup.py sdist bdist_wheel
	pip3 install --force-reinstall .

run-tests:
	nose2 -s tests

publish-release:
	rm dist/ -r -f
	python3 setup.py sdist bdist_wheel
	python3 -m  twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --repository-url https://upload.pypi.org/legacy/ dist/*
	@echo 'Do -> git tag -m "0.X.Y" -a 0.X.Y && git push --tags'
