import glob

def count_revision(file_list):
    rev_count = 0
    for file in file_list:
        #print(file)
        read_f = open(file, 'r')
        lines = read_f.readlines()
        for line in lines:
            #print(line)
            if line.startswith('  <revision'):
                rev_count += 1
    return rev_count

def classified_rev(file_list):
    classified_count = 0
    for file in file_list:
        read_f = open(file, 'r')
        lines = read_f.readlines()
        for line in lines:
            if line.startswith('        <error'):
                if 'xtype="xxx"' or 'xtype="zzz':
                    classified_count += 1
    return classified_count

def count_files(file_list):
    count = 0
    for file in file_list:
        count += 1
    return count

file_list = glob.glob('data/**/.xml')
print('Number of revision:')
print(count_revision(file_list))
print('Number of errors:')
print(classified_rev(file_list))
print('Number of files:')
print(count_files(file_list))
