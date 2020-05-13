def msg(pathmessage):
    list1 = pathmessage.partition("echo?msg=")
    rest = list1[2].replace("+", " ")
    return rest


def check_on(message):
    mensaje = msg(message)
    normal = mensaje.replace("&chk=on", "")
    return normal.upper()

print(check_on("echo?msg=hello+how+are+you+doing&chk=on"))
