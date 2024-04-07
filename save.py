import glob, os, shutil
file_exe = input("what is the exension of our files in the downloads to sort\n") # Extension with out the "."
uname = os.getenv("USERNAME")
source_dir = "C:/Users/"+uname+"/Downloads"
dest_dir = "C:/Users/"+uname+"/Downloads/"+file_exe

files = glob.iglob(os.path.join(source_dir, "*."+file_exe))
if not os.path.exists(source_dir+"/"+file_exe):
    os.mkdir(dest_dir)
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dest_dir)
else:
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dest_dir)
