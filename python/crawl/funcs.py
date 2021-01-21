def listToStr(list, sep):
    strr = ''
    for item in list:
        strr += item.get_text().strip() + sep
    strr = None if strr == '' else strr[:len(strr)-1]
    return strr
