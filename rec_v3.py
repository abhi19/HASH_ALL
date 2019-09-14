import os
import time
import filecmp
from os import listdir, getcwd
from os.path import isfile, join, normpath, basename
import hashlib

def get_files():
    path = dirName
    return [join(path, f) for f in listdir(path) if isfile(join(path, f))]

def get_hashes():
    files = get_files()
    list_of_hashes = []
    for each_file in files:
        hash = hashlib.md5()
        with open(each_file, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):# Read and update hash in chunks/blocks of 4K(usefull for large files)
                hash.update(block)
        list_of_hashes.append('File name: {}\tHash value: {}\n'.format(basename(each_file), hash.hexdigest()))
        
    return list_of_hashes

#this function which will be checking hashes every time & then writing it in hash_list2
def foo():
    hash2 = get_hashes() #will check again hashes
    with open('hash_list2.txt', 'a') as f:
        
            for md5_hash in hash2:
                f.write(md5_hash)
    f.close()
       
#writing hashes to a hash_list one for the first time
def write_hashes():
    hashes = get_hashes()
    with open('hash_list.txt', 'a') as f:
        for md5_hash in hashes:
            f.write(md5_hash)
    f.close() 
       
 #MAIN           
if __name__ == '__main__':
    #setting up directory to begin hashing from
    rootDir = raw_input("Please enter directory: ")
    #rootDir = '/opt/sublime_text_3'
    #rootDir = 'e:\\Abhi/Vedant/new'
    #to clear hash logs from hash_file
    f = open('hash_list.txt', 'w+')
    f.truncate(0)
    f.close
    f = open('hash_list2.txt', 'w+')
    f.truncate(0)
    f.close
    print("Writing Hashes Wait !!!")
    time.sleep(1)
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        write_hashes()
        for fname in fileList:
            print('\t%s' % fname)
           
    print("Now checking hashes in real time")
    
    while True:
        for dirName, subdirList, fileList in os.walk(rootDir):
            foo()
            #compare 2 hash files       
        if filecmp.cmp('hash_list.txt','hash_list2.txt'):
            print('Hashes matched !!! Okay')
            print time.ctime()
        else:
            print('Alert !!! Hash values changed')
            print time.ctime()
        time.sleep(5)
        f = open('hash_list2.txt', 'r+')
        f.truncate(0)
        f.close
        