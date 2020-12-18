import re
import sys

diagnoses_path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Project Hospital\\ProjectHospital_Data\\StreamingAssets\\Database\\Diagnoses'

if len(sys.argv) < 2:
    print('Please enter a diagnoses config name.')
    sys.exit(1)

file_path = f'{diagnoses_path}\\{sys.argv[1]}.xml'

with open(file_path, 'r') as reader:
    data = reader.readlines()

for i, line in enumerate(data):
    if '<InsurancePayment>' in line:
        value_str = ''
        for char in line:
            if char.isdigit():
                value_str += char
        value = int(value_str)
        value *= 2
        data[i] = data[i].replace(value_str, str(value))

with open(file_path, 'w') as writer:
    writer.writelines(data)
