import xml.etree.ElementTree as ET

tree = ET.parse('./cashsecurityclosemd_20180419.xml')
root = tree.getroot()
print('根节点是:',root)
for record in root:
    print(f'记录:{record.tag}:{record.attrib}')
    for item in record:
        print(f'******元素：{item.tag}: {item.text}')