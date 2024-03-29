import csv


def read_file_csv(path) -> list:
    with open(path, 'r', newline='') as csv_file:
        date = csv.reader(csv_file, delimiter=',', quotechar='|')

        res = []
        for line in date:
            res_line = []
            for l in line[:4] + [line[5]]:
                l = l.strip('"')
                if l.find('.') != -1:
                    l = float(l)
                elif l.isdigit():
                    l = int(l)
                res_line.append(l)
            res.append(res_line)

    return res
