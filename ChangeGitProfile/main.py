import sys
import shutil
import os

import initializer

args = sys.argv

home = str(os.environ['HOME'])
gitconfigs = home + "/.gitconfigs"

if not os.path.exists(gitconfigs):
    print("It seems that you are running this script at first time.")
    print("Would you like to setup? [y/n]")
    if input().lower() == "y":
        initializer.setup()

if not len(args) == 2:
    print("Error!")
    raise IndexError("Please specify only one argument")

if not os.path.exists(gitconfigs + "/" + args[1]):
    print("Configure '{}' not found".format(args[1]))
    exit()

else:
    if os.path.exists(home + "/.gitconfig"):
        try:
            os.remove(home + "/.gitconfig")
        except:
            print("Failed to remove '.gitconfig'.")
            exit()
    try:
        shutil.copy(gitconfigs + "/" + args[1], home + "/.gitconfig")
        print("Success!")
    except:
        print("Failed to copy '{}'.".format(args[1]))
        exit()
