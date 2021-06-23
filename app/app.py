#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13b_V3
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import base64
import json
import io
from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key='abc'


@app.route('/clear',methods=['GET'])
def clear():
    epd = epd2in13b_V3.EPD()
    epd.init()
    epd.Clear()
    return ''

def text(draw, text):
    font20 = ImageFont.truetype(os.path.join(picdir, 'amiga4everpro2.ttf'), text['size'])
    draw.text((text['pos']['x'], text['pos']['y']), text['text'], font = font20, fill = 0)

def line(draw, line):
    draw.line((line['from']['x'], line['from']['y'], line['to']['x'], line['to']['y']), fill = line['fill'])

def rectangle(draw, rectangle):
    if('outline' in rectangle):
        draw.rectangle((rectangle['from']['x'], rectangle['from']['y'], rectangle['to']['x'], rectangle['to']['y']), outline = rectangle['outline'])
    if('fill' in rectangle):
        draw.rectangle((rectangle['from']['x'], rectangle['from']['y'], rectangle['to']['x'], rectangle['to']['y']), fill = rectangle['fill'])
    else:
        draw.rectangle((rectangle['from']['x'], rectangle['from']['y'], rectangle['to']['x'], rectangle['to']['y']))

def arc(draw, arc):
    draw.arc((arc['from']['x'], arc['from']['y'], arc['to']['x'], arc['to']['y']), arc['start'], arc['end'], fill = arc['fill'])

def chord(draw, chord):
    draw.chord((chord['from']['x'], chord['from']['y'], chord['to']['x'], chord['to']['y']), chord['start'], chord['end'], fill = chord['fill'])

def polygon(draw, polygon):
    draw.polygon(polygon['points'], polygon['fill'])

def img(image, img):
    base64_img_bytes = img['img'].encode('utf-8')
    
    newimage = Image.open(io.BytesIO(base64.b64decode(base64_img_bytes)))
    image.paste(newimage, (img["pos"]["x"],img["pos"]["y"]))



@app.route('/json', methods=['POST'])
def json():
    logging.basicConfig(level=logging.DEBUG)
    epd = epd2in13b_V3.EPD()
    epd.init()
    epd.Clear()
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)

    content = request.json

    for i in content["operations"]:
        color = drawry
        image = HRYimage
        if i['color'] == 'BLACK':
            color = drawblack
            image = HBlackimage
        if i['type'] == 'TEXT':
            text(color, i)
        if i['type'] == 'LINE':
            line(color, i)
        if i['type'] == 'RECTANGLE':
            rectangle(color, i)
        if i['type'] == 'ARC':
            arc(color, i)
        if i['type'] == 'CHORD':
            chord(color, i)
        if i['type'] == 'POLYGON':
            polygon(color, i)
        if i['type'] == 'IMG':
            img(image,i)

    if(content["flip"]):
        HBlackimage = HBlackimage.transpose(Image.ROTATE_180)
        HRYimage = HRYimage.transpose(Image.ROTATE_180)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    return 'OK'
