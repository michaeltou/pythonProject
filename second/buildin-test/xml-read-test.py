
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('Start element:', name, 'attributes:',attrs)

    def end_element(self, name):
        print('End element:', name)

    def char_data(self, data):
        print('char_data:', data.strip())


xml = r'''<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>XML Example</title>
</head>
<body>
<h1>XML Example</h1>
<p>This is an example of XML.</p>
</body>
abc
</html>
'''


handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
