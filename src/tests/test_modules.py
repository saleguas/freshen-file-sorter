import os,sys,glob,shutil
import pytest
import yaml
import random

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))


import modules
# we want to test the modules in the scripts folder
# methods are sortbyType, sortByExtension, sortByDate, extract
# use test_dir to create dummy files
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'test_dir'))

def clear_test_dir():
    files = glob.glob(os.path.join(test_path, '*'))
    for f in files:
        # remove all directories and files
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

def test_sortByType(path):
    clear_test_dir()
    # make a ton of dummy files in the test_dir
    # read the filegroups.yml file to get the filegroups
    with open(os.path.join(os.path.dirname(__file__), '..', 'config/', 'filegroups.yml')) as f:
        file_types = yaml.safe_load(f)['type_sort']
    print(file_types)

    # # make a file for each type, and make two files for every even numbered file
    for type in file_types:
        for i in range(len(file_types[type])):
            with open(os.path.join(test_path, '{}_{}.{}'.format(type, i, file_types[type][i])), 'w') as f:
                f.write('test')
            if i % 2 == 0:
                with open(os.path.join(test_path, '{}_{}2.{}'.format(type, i, file_types[type][i])), 'w') as f:
                    f.write('test')
    with open(os.path.join(test_path, 'test'), 'w') as f:
        f.write('test')

    # test the sortByType method
    modules.sortByType(test_path)

    # check that the files are in the correct folder
    folders = os.listdir(test_path)
    for folder in folders:
        for file in os.listdir(os.path.join(test_path, folder)):
            if folder == "Others":
                for type in file_types:
                    assert os.path.splitext(file)[1][1:] not in file_types[type]
            else:
                assert os.path.splitext(file)[1][1:] in file_types[folder]

def test_sortByExtension(path):
    clear_test_dir()
    extensions = ['txt', 'py', 'pyc', 'c', 'cpp', 'h', 'hpp', 'java', 'js', 'json', 'md', 'php', 'rb', 'sh', 'sql', 'xml', 'yml']

    # make a random number of files for each extension
    for ext in extensions:
        for i in range(random.randint(1,10)):
            with open(os.path.join(test_path, '{}_{}.{}'.format(ext, i, ext)), 'w') as f:
                f.write('test')

    # test the sortByExtension method
    modules.sortByExtension(test_path)
    # check that the files are in the correct folder
    folders = os.listdir(test_path)
    for folder in folders:
        for file in os.listdir(os.path.join(test_path, folder)):
            assert os.path.splitext(file)[1] == folder[1:]

# not testing the other sort methods b/c i'm pretty sure they work

def test_extract(path):
    clear_test_dir()
    # make a ton of random directories and files

    files = 50
    dirs = 50
    # make a ton of nested directories and save their paths
    for i in range(dirs):
        # make a directory and make another directory in it
        new_path = os.path.join(test_path, '{}'.format(i))
        os.mkdir(new_path)
        for j in range(files):
            # make a file in the directory
            with open(os.path.join(new_path, '{}.test'.format(j)), 'w') as f:
                f.write('test')

    # test the extract method
    modules.extractAll(test_path, test_path)
    # make sure there are 100 * 100 files
    assert len(os.listdir(test_path)) == files * dirs



if __name__ == '__main__':
    test_sortByExtension(test_path)






