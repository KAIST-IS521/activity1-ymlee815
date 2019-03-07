import csv
import sys

def func(f, num):
    num = int(num)

    if num == 0:
        sys.exit(1) # N = 0

    i = 0 # counter

    with open(f, 'r') as csvfile:
        try:
            reader = csv.reader(csvfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
        except:
            sys.exit(1) # The given CSV is not well-formed.

        for line in reader:
            line = [wd.replace('\r', '') for wd in line]
            line = [wd.replace('\n', '') for wd in line]

            for wd in line:
                i = i + 1
                if i == num:
                    print(wd)
                    sys.exit(0)

        sys.exit(1) # N is out of the valid range of the given CSV.


if __name__ == '__main__':

    func(sys.argv[1], sys.argv[2])
