import csv
with open('test_file.csv', 'rt') as csvfile:
    CV_file = csv.reader(csvfile)
    CV_List = list(CV_file)
    # print(next(CV_file))
    print(CV_List)