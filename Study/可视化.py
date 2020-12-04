from pyecharts import options as opts
from pyecharts.charts import Bar
import xlrd

def open_excel():
    try:
        book = xlrd.open_workbook("知乎热榜.xlsx")
    except:
        print("打开excel文件失败！")
    try:
        sheet = book.sheet_by_name("Sheet")  # excel表中sheet名
        return sheet
    except:
        print("在excel中查找sheet失败！")

list_pm = []
list_rd = []
list_hd = []

sheet = open_excel()
counts = sheet.nrows
for i  in range(1, 11):
    pm = sheet.cell(i, 0).value
    rd = sheet.cell(i, 2).value
    hd = sheet.cell(i, 4).value
    list_pm.append('第' + pm + '名')
    list_rd.append(rd[:-4:])
    list_hd.append(hd)

print(list_pm)
print(list_rd)
print(list_hd)


c = (
    Bar()
    .add_xaxis(
        list_pm
    )
    .add_yaxis("热度(万)", list_rd)
    .add_yaxis("回答数", list_hd)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="知乎热榜", subtitle="热度与回答数对比"),
    )
    .render("bar_rotate_xaxis_label.html")
)

