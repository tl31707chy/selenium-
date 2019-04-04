import  xlrd
data=xlrd.open_workbook('C:/a.xlsx')
# 获取excl表中数据 []代表excl表中的页数  0=sheet1  1=sheet2   3=sheet
sheet=data.sheets()[0]
print(sheet)
# 查看sheet的名字
Sheet_name=sheet.name
print(Sheet_name)
# 以行查询数据
row_value= sheet.row_values(2)
print(row_value)
# 以列查询数据
col_value = sheet.col_values(2)
print(col_value)
# 总行数
nrows = sheet.nrows
print(nrows)
# 总列数
nclos = sheet.ncols
print(nclos)
# 以行的形式查询数据
for i in range(0,sheet.nrows):
        print(sheet.row_values(i))
# 以列的形式查询数据
for i in range(0,sheet.ncols):
	    print(sheet.col_values(i))
# 通过单元格的形式查询
cellvalue = sheet.cell(0,0).value
print(cellvalue)
cellvalue = sheet.cell_value(1,2)
print(cellvalue)







