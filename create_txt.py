import os
import xml.etree.ElementTree as ET

def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x *= dw
    w *= dw
    y *= dh
    h *= dh
    return x, y, w, h

def convert_xml_to_txt(xml_folder, txt_folder, classes):
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            image_size = root.find('size')
            image_width = int(image_size.find('width').text)
            image_height = int(image_size.find('height').text)

            txt_file_path = os.path.join(txt_folder, xml_file.replace('.xml', '.txt'))
            with open(txt_file_path, 'w') as txt_file:
                for obj in root.findall('object'):
                    class_name = obj.find('name').text
                    if class_name not in classes:
                        continue

                    class_id = classes.index(class_name)

                    box = obj.find('bndbox')
                    x_min = float(box.find('xmin').text)
                    y_min = float(box.find('ymin').text)
                    x_max = float(box.find('xmax').text)
                    y_max = float(box.find('ymax').text)

                    x, y, w, h = convert_coordinates((image_width, image_height), (x_min, x_max, y_min, y_max))
                    txt_file.write(f'{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n')

# 要转换的XML标注文件夹路径
xml_folder = 'Z:/Dataset/Annotations'
# TXT输出文件夹路径
txt_folder = 'Z:/Dataset/labels'
# 类别列表，按照实际类别顺序添加
classes  = ["1","2"]
convert_xml_to_txt(xml_folder, txt_folder, classes)