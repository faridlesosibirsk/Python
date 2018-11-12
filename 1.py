import re

def reader(filename):

    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.read()

        ips_list = re.findall(regexp,log)

    print(ips_list)

if __name__ == '__main__':
    reader('access.log.1')
