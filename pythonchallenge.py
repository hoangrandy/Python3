# stage 1
# print(2**38)

#stage 2
# not quite right but this is how I did it
# from string import ascii_lowercase
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# list = []
#
# for letter in string:
#     position = alphabet.find(letter)
#     if position == -1:
#         list.append(" ")
#     else:
#         newposition = (position + 2) % 26
#
#         newChar = alphabet[newposition]
#         list.append(newChar)
# print(list)

# The right way


# alpha = 'abcdefghijklmnopqrstuvwxyz'
# alpha2= 'cdefghijklmnopqrstuvwxyzab'
# secret = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# trans = str.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
# print(secret.translate(trans))
# print("map".translate(trans))
