cd ..
rm -rf output
mkdir output
mkdir output/freshen/
cp src/scripts/*.py output/freshen/
mkdir output/freshen/config/
cp src/config/*.yml output/freshen/config/
touch output/freshen/__init__.py
zip -r output/freshen.zip output/freshen/
cp *.md output/
cp src/setup.py output/
cp src/__init__.py output/freshen/
cp -r graphics output/
