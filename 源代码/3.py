#读station_realtime.csv文件，以HTML展示部分内容
seg1 = '''
<!DOCTYPE HTML>\n<html>\n<head>\n<meta charset="gb2312">\n
<title>CSV转为HTML表格</title>\n</head>\n<body>\n
<h2 align='center'>城市环境指数</h2>\n<table border="2" align="center" width="60%">\n
<tr bgcolor="#bfa">\n'''

seg2="</tr>\n"

seg3="</table>\n</body>\n</html>"
#填充数据
def fill_data(locls):  #*locls 0 1 3 5 9 11 13 15 19 21 
    seg="<tr>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td>\
    <td align='center'>{}</td></tr>\n".format(locls[0],locls[1]
                    ,locls[3],locls[5],locls[9],locls[11],locls[13]
                    ,locls[15],locls[19],locls[21])
    return seg

fr = open("station_realtime.csv","rt")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
    
fr.close()
fw = open("station_realtime.html","w")
fw.write(seg1)
#构造表头
fw.write("<th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n\
         <th width='25%'>{}</th>\n".format(ls[0][0],ls[0][1],
                    ls[0][3],ls[0][5],ls[0][9],ls[0][11],ls[0][13],
                    ls[0][15],ls[0][19],ls[0][21]))      #*ls[0]

fw.write(seg2)      

#for i in range(len(ls)-1): 
for i in range(5000):
    fw.write(fill_data(ls[i+1])) #从第二行开始
fw.write(seg3)
fw.close()
