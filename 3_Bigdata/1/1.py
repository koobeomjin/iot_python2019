from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note', date='20120104', to='Tove')
# to = Element('to')
# to.text = 'Tove'
# note.append(to)
SubElement(note,'form').text='Jani' # SubElement를 활용하여 자식 노드 추가

dump(note)