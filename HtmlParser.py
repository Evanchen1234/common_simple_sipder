# -*- coding: utf-8 -*-
"""
Created on 2017/8/26 上午11:14

@author: Evan Chan
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import pandas as pd
import json
class HtmlParse:

    def parse_catear(self,html_cont):
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        moive_name_node=soup.find('div',class_="celeInfo-right clearfix").find('h3')
        categroy_nodes=soup.find_all('li',class_="ellipsis")

        #3维
        attri_list=[]
        for node in categroy_nodes:
            temp = str(node.get_text())
            temp = temp.strip().replace('\n','').replace('          / ',' ')
            attri_list.append(temp)
        moive_list=[attri_list[0],attri_list[1],attri_list[2]]
        return moive_list

    def parse(self,html_cont,date):
        if html_cont is None:
            return

        moive_info=json.loads(html_cont)
        moive_df = []

        for i in moive_info['data']['list']:
            moive_df.append(i.values())
        moive_df = pd.DataFrame(moive_df,columns=moive_info['data']['list'][0].keys())

        moive_df.to_csv(r"/Users/ch_cmpter/Desktop/2016/moive_"+date+".csv",encoding='utf-8')
        return

