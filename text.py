# -*- encoding:utf-8 -*-
__author__ = 'cong'
__date__ = '18-12-8 下午3:35'


import re

fp = open('num.txt','r')
fc = fp.read()
# fc.strip(' ')
# fc.replace('\n','')
# print fc
rule = r'[A-Z]'
list = re.findall(rule,fc)
#a = re.split(r'\d+、',fc)
#a.replace('\n','')
print list
fb = open('aaa.txt','r')
fd = fb.readline()
i=1
for line in fb:
    if '）。' in line:
        line.replace('（ ','（'+list[i])
        i=i+1
        print line

print(fb)