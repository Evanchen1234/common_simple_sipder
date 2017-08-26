# -*- coding: utf-8 -*-
"""
Created on 2017/8/26 上午11:15

@author: Evan Chan
"""
from HtmlParser import HtmlParse
from HtmlDownload import htmlDownlaod
import time

class spider:

    def __init__(self):
        self.HtmlParser=HtmlParse()
        self.HtmlDownload=htmlDownlaod()

    def craw(self,root_url_list,date):
        moive_dict_list=[]
        for idx in range(len(root_url_list)):
            html_cont=self.HtmlDownload.download(root_url_list[idx])
            moive_dict=self.HtmlParser.parse(html_cont,date[idx])


def dateRange(bgn, end):
    fmt = '%Y%m%d'
    bgn = int(time.mktime(time.strptime(bgn,fmt)))
    end = int(time.mktime(time.strptime(end,fmt)))
    return [time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]

date_list=dateRange("20130101","20170823")

prefix="https://box.maoyan.com/promovie/api/box/second.json?beginDate="
url_list=[prefix+date_list[i] for i in range(len(date_list))]

spd=spider()
spd.craw(url_list,date_list)

