import xlrd
from xml.dom import minidom

def load_excel_data_as_dict(f_path):
    dict_content = {}

    workbook = xlrd.open_workbook("numbers.xls")
    sheet_name = workbook.sheet_names()[0]
    print(sheet_name)
    sheet = workbook.sheet_by_name(sheet_name)

    for row in range(sheet.nrows):
        dict_content[str(row+1)] = sheet.row_values(row)[1:]


    return dict_content

def write_data_to_xml(dict_content):
    xml_doc = minidom.Document()

    root = xml_doc.createElement('root')

    xml_doc.appendChild(root)

    cities = xml_doc.createElement('numbers')

    root.appendChild(cities)

    comment = xml_doc.createComment("数字信息\n")

    cities.appendChild(comment)

    content = xml_doc.createTextNode(str(dict_content))

    cities.appendChild(content)

    with open("numbers.xml",'wb') as f:
        f.write(xml_doc.toprettyxml(encoding="utf-8"))

def main():
    f_path = "numbers.xls"
    d = load_excel_data_as_dict(f_path)
    write_data_to_xml(d)
if __name__ == "__main__":
    main()
