./buildOutput.sh
cd ../output
python3 setup.py sdist bdist_wheel
twine upload dist/*
