import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_dir = os.path.join(BASE_DIR, 'img')

os.makedirs(file_dir, exist_ok=True)

my_txt = range(0,12)

for i in my_txt:
    fname =f"{i}.txt"
    file_path = os.path.join(file_dir, fname)
    if os.path.exists(file_path):
        print(f"skip: {i}.txt")
        continue
    with open(file_path,"w") as f:
        f.write(f"test{i}")
    
    