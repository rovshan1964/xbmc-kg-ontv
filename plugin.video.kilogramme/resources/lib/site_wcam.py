#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2, re, json, xbmc, traceback
from _header import *

BASE_NAME_SAIMA = common.replaceHTMLCodes('&emsp;SAIMA TELECOM&emsp;live.saimanet.kg')
BASE_URL_SAIMA = 'http://live.saimanet.kg/sys/api/get_cams'

BASE_NAME_SMOTRI = common.replaceHTMLCodes('&emsp;SMOTRI.KG')
BASE_URL_SMOTRI = 'http://www.smotri.kg/'

BASE_NAME_KT = common.replaceHTMLCodes('&emsp;KyrgyzTelecom')
BASE_URL_KT = 'http://kt.kg'

BASE_NAME = 'Веб-камеры'
BASE_LABEL = 'wc'


@plugin.route('/site/' + BASE_LABEL)
def wc_index():
    item_list = get_cameras()

    items = [{
                 'label': item['name'],
                 'path': item['url'],
                 'thumbnail': item['icon'],
                 'is_playable': True
             } for item in item_list]

    return items


def get_cameras():
    items = []
    try:
        result = common.fetchPage({'link': BASE_URL_SAIMA})
        if result['status'] == 200:
            data = json.loads(result['content'])
            for item in data:
                try:
                    name = set_color(item['title'], 'bold') + BASE_NAME_SAIMA
                    items.append({'name': common.replaceHTMLCodes(name), 'url': item['url'], 'icon': item['image']})
                except:
                    pass
    except:
        pass
        xbmc.log('Exception : ' + str(traceback.format_exc()))
        xbmc.log('Exit list : ' + str(items))

    try:
        icon = 'http://kt.kg/bitrix/templates/ktnet_copy/images/logo.gif'
        name = set_color(unicode('Чуй - Фонтан', 'utf-8'), 'bold') + BASE_NAME_KT
        items.append({'name': common.replaceHTMLCodes(name), 'url': 'rtmp://213.145.131.243:5010/live', 'icon': icon})
    except:
        pass
        xbmc.log('Exception : ' + str(traceback.format_exc()))
        xbmc.log('Exit list : ' + str(items))
    return items