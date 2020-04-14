import sys
import shutil
import os

home = str(os.environ['HOME'])
gitconfigs = home + "/.gitconfigs"

def setup():
    # Check if '.gitconfigs' exists under $HOME
    # If not, make it
    if not os.path.exists(gitconfigs):
        os.mkdir(gitconfigs)

    # Check if executable python file 'main.py' exists under $HOME/.gitconfigs
    # If not, copy 'main.py' to there
    if not os.path.exists(gitconfigs+"/main.py"):
        print(gitconfigs+"/main.py")
        shutil.copy('main.py', gitconfigs+"/main.py")
        shutil.copy('initializer.py', gitconfigs+"/initializer.py")

    if os.path.exists(home + "/.gitconfig"):
        shutil.copy(home+"/.gitconfig", gitconfigs+"/default")

    print("Setup all done!")
    print("We recommend you to add 'python {}' to your '.zshrc' as a alias.".format(gitconfigs + "/main.py"))
    exit()

if __name__ == "__main__":
    setup()