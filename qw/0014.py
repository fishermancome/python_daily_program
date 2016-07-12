import xlwt as ExcelWrite

def write_XLS(filename):
    dict1 = {
        "1":["张三",150,120,100],
        "2":["李四",90,99,95],
        "3":["王五",60,66,68]
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

    for i in range(0,3):
        for j in range(0,4):
            sheet.write(i,j+1,values[i][j])

    xls.save(filename)

if __name__ == "__main__":
    write_XLS("student.xls")
