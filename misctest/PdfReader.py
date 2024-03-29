import pdfplumber

# 打开 PDF 文件
with pdfplumber.open('../dbf/example.pdf') as pdf:
    # 遍历 PDF 文件的每一页
    for page in pdf.pages:
        # 提取当前页的文本内容
        text = page.extract_text()
        print(text)