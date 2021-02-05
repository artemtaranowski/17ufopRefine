# 29.12.2020 відновлено оприлюднення розширеного набору даних ЄДР.
# З цієї дати й принаймні до 01.02.2021 з xml-файлами є проблеми.
# Атрибут record тегу SUBJECT містить неприпустимі &quot;.
# Теги містять неприпустимі коди HTML entities.
# Обробка xml-файлів може перериватися через invalid xml, зокрема:
# xml.etree.ElementTree.ParseError: not well-formed (invalid token).
# Цей код вирішує цю проблему.
# Без претензії на правильність.
# Аби мати хоча б якусь можливість працювати з xml-файлами.
# Для розширеного набору даних ЄДР FULL з data.gov.ua чи nais.gov.ua.
# Безпосередньо перевіралося на оприлюднених 10.01.2021 й 18.01.2021.
# Успішно використовувалося на оприлюднених 25.01.2021 й 01.02.2021.
#
# На вхід: xml-файл зі згаданими проблемами.
# На виході: переписаний xml-файл з refined- на початку назви.
# Також, encoding змінюєтьс з windows-1251 на utf-8.


import sys

def main():
    
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 " + sys.argv[0] + " xml_file")
    
    inputxmlname = sys.argv[1]
    outputxmlname = "refined-" + inputxmlname
    
    inputxml = open(inputxmlname, "r", encoding="windows-1251")
    outputxml = open(outputxmlname, "w")
    
    recordcounter = 0
    
    characterstoexclude = []
    for value in range(32):
        characterstoexclude.append("&#" + str(value) + ";")
    
    headline = inputxml.readline()
    headline = headline.replace("windows-1251","utf-8")
    outputxml.write(headline)
    
    for line in inputxml:
        line = line.replace("&quot;", "\"")
        for value in characterstoexclude:
            line = line.replace(value, "")
        outputxml.write(line)
        recordcounter += 1
        if recordcounter % 1000 == 0:
            print(str(recordcounter // 1000) + "k", end="\r")

    inputxml.close()
    outputxml.close()


if __name__ == "__main__":
    main()
