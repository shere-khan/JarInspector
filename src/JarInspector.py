'''
Created on Mar 11, 2016

@author: barryjus
'''
import sys
from os.path import os
import zipfile


def main(argv):
    directory = argv[1]
    for dirname, dirnames, filenames in os.walk(directory):
        os.chdir(dirname)
        for filename in filenames:
            if filename.endswith('.jar'):
                print filename
                jar = zipfile.ZipFile(filename, 'r')
                for info in jar.infolist():
                    if info.filename == 'META-INF/MANIFEST.MF':
                        data = jar.read(info.filename)
                        lines = data.splitlines()
                        for line in lines:
                            imp_version = line.find('Implementation-Version')
                            if imp_version != -1:
                                print line + '\n'

if __name__ == '__main__':
    main(sys.argv)