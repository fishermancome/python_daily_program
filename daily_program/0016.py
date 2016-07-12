import xlwt as ExcelWrite

def write_XLS(filename):
    numbers = [[1, 82, 65535], [20, 90, 13],[26, 809, 1024]]

#获取一个对象
    xls = ExcelWrite.Workbook()
#添加一个sheet
    sheet = xls.add_sheet("Sheet1")
#向sheet中写入数据
    for i in range(0,3):
        for j in range(len(numbers)):
            sheet.write(i,j,numbers[i][j])
#保存
    xls.save(filename)

if __name__ == "__main__":
    write_XLS("numbers.xls")


