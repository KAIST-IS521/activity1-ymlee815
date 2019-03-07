import csv
import sys

def func(f, num):
    num = int(num)

    if num == 0:
        sys.exit(1)

    i = 0 # counter

    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar ='"', quoting = csv.QUOTE_ALL)
    
        for line in reader:
            line = [wd.replace('\r', '') for wd in line]
            line = [wd.replace('\n', '') for wd in line]

            for wd in line:
                i = i + 1
                if i == num:
                    print(wd)
                    sys.exit(0)
        sys.exit(1)


if __name__ == '__main__':

    func(sys.argv[1], sys.argv[2])
