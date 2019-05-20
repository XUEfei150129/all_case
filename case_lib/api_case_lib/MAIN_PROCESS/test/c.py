#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/5/15 11:23
# @Author : XueFei
import base64

image = '1.jpg'
print(type(image))


def imageToStr(image):
    with open(image, 'rb') as f:
        image_byte = base64.b64encode(f.read())
        print(type(image_byte))
    image_str = image_byte.decode('ascii')  # byte类型转换为str
    print(type(image_str))
    return image_str


image1 = imageToStr("d:\\1.png")
print(type(image1))

data = {
    "engineeringdata": {
        "date": 12,
        "value": "59.3;98.5",
        "image": image1
    }
}


def strToImage(str, filename):
    image_str = str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)  # 将图片存到当前文件的fileimage文件中
    image_json.close()
    print(1)


# file_address = "./fileimage/" + data['engineeringdata']['date'] + r".jpg"
strToImage(data['engineeringdata']['image'], "d:\\1.png")
