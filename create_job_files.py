import shutil
import re
for count in range(1,123):
    shutil.copyfile('fs_base.job', 'Job_files/fs_{}.job'.format(count))
    filename='Job_files/fs_{}.job'.format(count)
    with open(filename, 'r+') as f:
        text = f.read()
        #print(text)
        text = re.sub('location_base_image.csv', '{}.csv'.format(count), text)
        f.seek(0)
        f.write(text)
        f.truncate()
