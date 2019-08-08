from xml.etree.ElementTree import parse

tree = parse('note2.xml')
note = tree.getroot()

print('특정 태그 멀티 레벨 자식 노드 접근')
for parent in note.getiterator("parent"):
    for child in parent.getiterator("child"):
        for grand_child in child.getiterator("grand_child"):
            print(grand_child.text)