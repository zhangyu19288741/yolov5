import os
import shutil

source_folder = "Dataset/images" #原数据集图像路径
destination_folder = "tra/images" #要训练/验证的数据集路径和image/labels路径
folder_path="autodl-tmp/zz_measure" #加上它变成完整路径

# 遍历源文件夹中的文件
for filename in os.listdir(source_folder):
    source_file_path = os.path.join(source_folder, filename)
    
    # 检查文件名是否以该数字结尾,图片则将后缀改为jpg，标注文件则改为txt
    #用于训练集
    #if filename.endswith("1.txt") or filename.endswith("2.txt")or filename.endswith("4.txt")or filename.endswith("5.txt")or filename.endswith("6.txt")or filename.endswith("7.txt")or filename.endswith("9.txt")or filename.endswith("0.txt"):
    #用于测试集
    if filename.endswith("3.jpg") or filename.endswith("8.jpg"):

        destination_file_path = os.path.join(destination_folder, filename)
        # 复制文件
        shutil.copy(source_file_path, destination_file_path)
        
        print(f"复制文件 {filename} 到目标文件夹")

'''       
# 遍历文件夹中的所有文件和子文件夹
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    
    # 如果是文件，直接删除
    if os.path.isfile(item_path):
        os.remove(item_path)
        print(f"已删除文件 {item}")
    
    # 如果是子文件夹，递归删除子文件夹及其内容
    elif os.path.isdir(item_path):
        shutil.rmtree(item_path)
        print(f"已删除文件夹 {item}")

print("文件夹内容已清空")
''' 