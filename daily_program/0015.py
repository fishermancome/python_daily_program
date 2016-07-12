import xlwt as ExcelWrite

def write_XLS(filename):
    dict1 = {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }

    xls = ExcelWrite.Workbook()

    sheet = xls.add_sheet("Sheet1")

    keys = []
    values = []
    for k in dict1.keys():
        keys.append(k)
        values.append(dict1[k])
    keys.sort()
    values.sort()

    for i in range(len(dict1)):
        sheet.write(i,0,keys[i])

    for j in range(0,3):
            sheet.write(j,1,values[j])

    xls.save(filename)

if __name__ == "__main__":
    write_XLS("city.xls")
