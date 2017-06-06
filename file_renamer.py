import os
import glob

def list_files_in_dir(base_dir, target_file):
        for root, dirs, files in os.walk(base_dir):
            for name in files:
                if(name == target_file):
                    print(os.path.join(root, name))

def replace_all(base_dir, target_file, new_name):
        for root, dirs, files in os.walk(base_dir):
            for name in files:
                if(name == target_file):
                    print '[Old Fileame] ' +os.path.join(root, name)
                    rename(os.path.join(root, name), os.path.join(root, new_name))
                    print '[New Fileame] ' + os.path.join(root, new_name)

def rename(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except Exception,e:
        print str(e)



def main():
    base_dir = raw_input('Enter Base Directory: ')
    target_file = raw_input('Enter Target Filename: ')
    list_files_in_dir(base_dir, target_file)

    new_name = raw_input('Enter New Filename: ')
    replace_all(base_dir, target_file, new_name)

if __name__ == '__main__':
    main()
