
file_names = ['1.txt', '2.txt', '3.txt']
dict_files = []

for file_name in file_names:
    with open(file_name, encoding='UTF-8') as file:
        text = file.readlines()
        dict_files.append((file_name, len(text), ''.join(text)))

for i in sorted(dict_files, key=lambda x: x[1]):
    print(*i, sep='\n')
    print()





# with open('1.txt', encoding='UTF-8') as file_1:
#     with open('2.txt', encoding='UTF-8') as file_2:
#         with open('3.txt', encoding='UTF-8') as file_3:
#
#             lines_ext_1 = sum(1 for line in file_1)
#             lines_text_2 = sum(1 for line in file_2)
#             lines_text_3 = sum(1 for line in file_3)




