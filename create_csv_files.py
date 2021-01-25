csvfile = open('Batch_Job_CSV_files/ADNI_all_locations-Copy1.csv', 'r').readlines()
filename = 1
for i in range(len(csvfile)):
     if i % 32 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+32])
        filename += 1
