import xlrd
from xml.dom import minidom

def load_excel_data_as_dict(f_path): #读取数字，以dict形式返回
    dict_content = {}

    workbook = xlrd.open_workbook('student.xls')
    sheet_name = workbook.sheet_names()[0]
    print(sheet_name)
    sheet = workbook.sheet_by_name(sheet_name)
    

    for row in range(sheet.nrows):
        dict_content[str(row+1)] = sheet.row_values(row)[1:]

    return dict_content

def write_data_to_xml(dict_content):
    xml_doc = minidom.Document() # 新建 Document 对象

    root = xml_doc.createElement('root')# 创建根节点

    xml_doc.appendChild(root) # 追加根节点到 Document 对象上

    students = xml_doc.createElement('student') # 创建 students 节点

    root.appendChild(students) # 追加 students 节点到 Document 对象上

    comment = xml_doc.createComment("学生信息表\"id\":[名字,数学,语文,英语]")# 创建注释节点

    students.appendChild(comment) # 追加注释节点到 students 节点上

    content = xml_doc.createTextNode(str(dict_content)) # 创建文本节点

    students.appendChild(content) # 追加文本节点到 students 节点上

    with open("studnet.xml",'wb') as f: # 将数据写入 xml 文件中
        f.write(xml_doc.toprettyxml(encoding='utf-8'))

def main():
    f_path = 'student.xls'
    d = load_excel_data_as_dict(f_path)
    write_data_to_xml(d)

if __name__ == "__main__":
    main()
