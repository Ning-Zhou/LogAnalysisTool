#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='For anything you want to contact the author, try this e-mail: nathon.py@gmail.com')
parser.add_argument("-hl","--highlight", help="just to highlight, otherwise it's filter", action = "store_true")
parser.add_argument("keywords", help=" keywords should be like \"keyword1|keyword2|..|keywordN\"")
parser.add_argument("filename", help=" just filename ")


args = parser.parse_args()

egrep="egrep --color=always -i"

colors = ['31','32','33','34','35','36','4;31','4;32','4;33','4;34','4;35','4;36','4']

keywords = args.keywords.split('|')
if len(keywords) > 13:
    print "\033[91mnot support number of keywords more than 13 with different colors"
    

color_setting = 'GREP_COLOR='+"\'"+colors[0]+"\'" 
filename = args.filename
command = ''


if not args.highlight:
    sub_command = ' '.join([ 'egrep -i' ,'\''+args.keywords+'\'', filename])
    
else:
    sub_command = ' '.join(['cat',filename])
command = command + sub_command

for v in range(0,len(keywords)):    
    color_setting = 'GREP_COLOR='+"\'"+colors[v%13]+"\'"
    keyword_tmp = '\''+keywords[v]+'|'+'\''    
    sub_command = ' '.join([' | '+color_setting, egrep, keyword_tmp])
    command = command + sub_command




import os
os.system(command)
os.system('echo ' +'"' + command + '"' + ' | cat > ' + 'filter.' + filename + '.sh')
os.system('chmod 755 ' + 'filter.' + filename + '.sh')
