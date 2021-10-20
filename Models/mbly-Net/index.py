import os

if not os.path.exists("./experiments"):
    os.mkdir("./experiments")
folders = os.listdir("./experiments")
exp_num = []
for folder in folders:
    exp_num.append(int(folder.split("#")[1]))

if len(exp_num) == 0:
    exp_path = "./experiments/exp#0"
else:
    exp_path = "./experiments/exp#"+str(max(exp_num)+1)
os.mkdir(exp_path)
os.mkdir(os.path.join(exp_path, "results"))
os.mkdir(os.path.join(exp_path, "weights"))
