import os

#克隆 YoloV5 仓库并安装依赖,如果已经下载了yolov5，则忽略这三行代码
#os.system("git clone https://github.com/ultralytics/yolov5.git")
#os.chdir("yolov5")
#os.system("pip install -U -r requirements.txt")

# 步骤 4：训练模型
train_command = (
    "python yolov5/train.py --img-size 640 --batch-size 16 --epochs 50 --hyp yolov5/data/hyps/hyp.scratch-low.yaml "
    "--data custom.yaml --cfg my_yolov5m.yaml --weights yolov5m.pt"
)
os.system(train_command)

# 步骤 5：在测试集上评估训练好的模型
eval_command = (
    "python yolov5/val.py --img-size 640 --batch-size 16 "
    "--data custom.yaml --weights best.pt"
)
os.system(eval_command)