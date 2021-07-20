import zipfile
import os
import time


def zip_dir(dirname, zipfilename):
    filelist = []

    if os.path.isdir(dirname):
        # print(list(os.walk(dirname)))
        for root, dirs, files in os.walk(dirname):
            print(root, dirs, files)
            for dir in dirs:
                filelist.append(os.path.join(root, dir))
            for name in files:
                filelist.append(os.path.join(root, name))
        with zipfile.ZipFile(zipfilename, "w") as zf:
            print(filelist)
            for tar in filelist:
                arcname = tar[len(dirname):]
                # print arcname
                zf.write(tar, arcname)
    else:
        # 此时dirname是文件
        filelist.append(dirname)
        with zipfile.ZipFile(zipfilename, "w") as zf:
            print(filelist)
            zf.write(dirname, os.path.basename(dirname))
            print(zf.pwd)



def zip_file(name, zipfilename, pwd=None):
    os.chdir(os.path.dirname(name))
    name = os.path.basename(name)
    print(name)
    print(zipfilename)
    if pwd:
        cmd = f'zip -P {pwd} -r {zipfilename} {name}'
    else:
        cmd = f'zip -r {zipfilename} {name}'
    res = os.system(cmd)
    print(res)


if __name__ == '__main__':
    print(time.time())
    root = '/Users/ltc/Downloads/测试/测试'
    dirname = os.path.join(root, '测试')
    zipfilename = os.path.join(root, '测试1.zip')
    # zip_dir(dirname, zipfilename)
    zip_file(dirname, zipfilename, pwd='123')
    print(time.time())
