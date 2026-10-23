import re,sys
core=open('page_core.html',encoding='utf-8').read()
GF='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Iansui&family=Chiron+GoRound+TC:wght@400;500&display=swap">\n'
head='''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>小藝繪本｜孩子當主角的科普繪本</title>
<meta name="description" content="注音科普繪本，讓孩子自己發現答案，再加上爸媽的陪伴。第 1 本《為什麼我會長大？》現正預購。">
<meta property="og:title" content="小藝繪本｜孩子當主角的科普繪本">
<meta property="og:description" content="孩子問的每個為什麼，都值得一本以他為主角的書。">
<meta property="og:image" content="img/grow/A/cover.webp">
'''+GF+'''<link rel="stylesheet" href="assets/fonts/font.css">
</head>
<body id="body">
'''
open('index.html','w',encoding='utf-8').write(head+core+'\n</body>\n</html>\n')
art='<title>小藝繪本</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'+GF+'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Huninn&display=swap">\n'+core
open('page.html','w',encoding='utf-8').write(art)
# local test copy: fontsource instead of Google Fonts
t=open('index.html',encoding='utf-8').read()
t=t.replace(GF,'<link rel="stylesheet" href="file:///tmp/fonts/node_modules/@fontsource/iansui/index.css"><link rel="stylesheet" href="file:///tmp/fonts/node_modules/@fontsource/chiron-goround-tc/400.css">\n')
open('test.html','w',encoding='utf-8').write(t)
