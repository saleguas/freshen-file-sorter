rm -rf dist
rm dist.zip
mkdir dist
cp -r src/scripts/*.py dist/
mkdir dist/config
cp src/config/filegroups.yml dist/config/
zip -r dist.zip dist