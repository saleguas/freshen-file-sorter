rm -rf dist/
mkdir dist/
cp src/scripts/*.py dist/
mkdir dist/config/
cp src/config/*.yml dist/config/
zip -r dist.zip dist/
rm -rf dist
