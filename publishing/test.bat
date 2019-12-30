pip uninstall freshen-sorter
cd ../output
python setup.py bdist_wheel
cd ..
python -m pip install output/dist/freshen_sorter-1.3.8-py3-none-any.whl
cd publishing
