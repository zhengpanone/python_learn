# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/26 9:47
"""

# import lib

import qrcode
from PIL import Image
import os


def make_qr(_str, save):
    qr = qrcode.QRCode(
        version=4,  # 生成二维码尺寸的大小 1-40 1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # L:7% M:15% Q:25% H:30%
        box_size=10,  # 每个格子的像素大小
        border=2  # 边框的格子宽度大小
    )
    qr.add_data(_str)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(save)


def make_logo_qr(_str, logo, save):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )
    qr.add_data(_str)
    qr.make(fit=True)
    img = qr.make_image()

    img = img.convert("RGBA")

    if logo and os.path.exists(logo):

        icon = Image.open(logo)
        img_w, img_h = img.size

        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size

        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h

        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        # 计算logo在二维码图中的位置
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)

        # 保存处理后图片
        img.save(save)


if __name__ == '__main__':
    save_path = "log.png"
    logo = "./giphy.gif"
    _str = input('请输入要生成二维码的文本内容：')
    # make_qr(_str, save_path)
    make_logo_qr(_str, logo, save_path)
