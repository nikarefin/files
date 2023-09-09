files_list = []
merged_list = []

for i in range(1, 4):
    with open(f'files/{i}.txt') as f:
        file = f.readlines()
        info = f'{i}.txt\nСтрок: {len(file)}\n'
        file.insert(0, info)
        files_list.append(file)

files_list.sort(key=lambda x: len(x))

for file in files_list:
    file_string = ''.join(file)
    merged_list.append(file_string)

merged_files = '\n\n'.join(merged_list)

with open('merged_files.txt', 'w') as f:
    f.writelines(merged_files)
