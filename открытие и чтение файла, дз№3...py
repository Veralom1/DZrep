
file_names = ['1.txt', '2.txt', '3.txt']
list_files = {}
for i in file_names:
    name = f'{i}'
    with open(name, 'r', encoding='utf-8') as file:
        list_files[name] = [x for x in file.read().splitlines() if x]

with open('final_file.txt', 'w', encoding='utf-8') as final_file:
    for k, v in sorted(list_files.items(), key=lambda x: x[1], reverse=True):
        final_file.write(k + '\n')
        final_file.write(str(len(v)) + '\n')
        final_file.write('\n'.join(v))
        final_file.write('\n')
