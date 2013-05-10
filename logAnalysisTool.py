#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("keywords", help=" keywords should be like \"keyword1|keyword2|..|keywordN\"")
parser.add_argument("filename", help=" just filename ")


args = parser.parse_args()

egrep="egrep --color=always -i"

colors = ['31','32','33','34','35','36','4;31','4;32','4;33','4;34','4;35','4;36','4']

keywords = args.keywords.split('|')
if len(keywords) > 13:
    print "\033[91mnot support number of keywords more than 13 with different colors"
    

color_setting = 'GREP_COLOR='+"\'"+colors[0]+"\'" 

keyword_1st = '\''+keywords[0]+'|'+'\''

filename = args.filename

sub_command = ' '.join([color_setting, egrep, keyword_1st, filename])

print sub_command

command = ''
command = command + sub_command

for v in range(1,len(keywords[1:])+1):    
    color_setting = 'GREP_COLOR='+"\'"+colors[v%13]+"\'"
    keyword_tmp = '\''+keywords[v]+'|'+'\''    
    sub_command = ' '.join([' | '+color_setting, egrep, keyword_tmp])
    command = command + sub_command


import os
print command
os.system(command)
#grep-color = "egrep --color=always -i"
#GREP_COLOR = '32' 
