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
    epd.sleep()
    return ''

def text(draw, text):
    font20 = ImageFont.truetype(os.path.join(picdir, 'amiga4everpro2.ttf'), text['size'])
    draw.text((text['pos']['x'], text['pos']['y']), text['text'], font = font20, fill = 0)

def line(draw, line):
    draw.line((line['from']['x'], line['from']['y'], line['to']['x'], line['to']['y']), fill = line['fill'])

def rectangle(draw, rectangle):
    draw.rectangle((rectangle['from']['x'], rectangle['from']['y'], rectangle['to']['x'], rectangle['to']['y']), outline = rectangle.get('outline'), fill = rectangle.get('fill'))

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

def pie(draw, pie):
    draw.pieslice((pie['from']['x'], pie['from']['y'], pie['to']['x'], pie['to']['y']), pie['start'], pie['end'], fill = pie['fill'])

REQUIRED_FIELDS = {
    'TEXT': ['pos', 'size', 'text'],
    'LINE': ['from', 'to', 'fill'],
    'RECTANGLE': ['from', 'to'],
    'ARC': ['from', 'to', 'start', 'end', 'fill'],
    'CHORD': ['from', 'to', 'start', 'end', 'fill'],
    'PIE': ['from', 'to', 'start', 'end', 'fill'],
    'POLYGON': ['points', 'fill'],
    'IMG': ['pos', 'img'],
}

def validate(content):
    if not isinstance(content, dict) or not isinstance(content.get('operations'), list):
        return 'body must be a JSON object with an "operations" list'
    for n, op in enumerate(content['operations']):
        if not isinstance(op, dict):
            return 'operation %d must be an object' % n
        if op.get('type') not in REQUIRED_FIELDS:
            return 'operation %d: unknown type %r' % (n, op.get('type'))
        missing = [f for f in ['color'] + REQUIRED_FIELDS[op['type']] if f not in op]
        if missing:
            return 'operation %d (%s): missing %s' % (n, op['type'], ', '.join(missing))
        for f in ('pos', 'from', 'to'):
            if f in op and not (isinstance(op[f], dict) and 'x' in op[f] and 'y' in op[f]):
                return 'operation %d (%s): %s must be {"x": ..., "y": ...}' % (n, op['type'], f)
    return None


@app.route('/json', methods=['POST'])
def json():
    logging.basicConfig(level=logging.DEBUG)
    content = request.get_json(silent=True)
    error = validate(content)
    if error:
        return error, 400

    epd = epd2in13b_V3.EPD()
    epd.init()
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)

    for i in content["operations"]:
        color = drawry
        image = HRYimage
        if i['color'] == 'BLACK':
            color = drawblack
            image = HBlackimage

        logging.debug('operation: %s', i['type'])
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
        if i['type'] == 'PIE':
            pie(color, i)
        if i['type'] == 'IMG':
            img(image,i)

    if(content.get("flip", False)):
        HBlackimage = HBlackimage.transpose(Image.ROTATE_180)
        HRYimage = HRYimage.transpose(Image.ROTATE_180)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    # Deep sleep between draws: Waveshare warns that leaving the panel powered
    # can damage it. The next request's epd.init() wakes it again.
    epd.sleep()
    return 'OK'
