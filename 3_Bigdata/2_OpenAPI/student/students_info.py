from xml.etree.ElementTree import parse, Element, dump, ElementTree

print('<전체 학생 데이터>')
def whole_xml():
   tree = parse("students_info.xml")
   note = tree.getroot()
   for parent in note.getiterator("student"):
       print("* %s"%parent.get("name"))
       print("- 성별: %s"%parent.get("sex"))
       print("- 나이: %s"%parent.findtext("age"))
       print("- 전공: %s"%parent.findtext("major"))
       for language_value in parent.getiterator("language"):
           if language_value:
               for period_value in language_value.getiterator("period"):
                   print("> %s 학습기간:%s,level:%s"%(language_value.get("name"),period_value.get("value"),language_value.get("level")))

   print("")

whole_xml()