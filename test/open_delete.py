import os, time

if __name__ == '__main__':
    f = open('delete.test', 'r+')
    os.remove('delete.test')
    time.sleep(5)
    data = f.read()
    print(data)
    f.write('sdfsdddddddd')
    f.close()
