from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note')
to = Element('to')
to.text = 'Tove'
note.append(to)
SubElement(note,'form').text='Jani' # SubElement를 활용하여 자식 노드 추가

note.attrib['data'] = '20120104'

dump(note)