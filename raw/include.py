import re,os

def get_lines(file):
    f=open(file,encoding="utf-8")
    lines=f.readlines()
    f.close()
    return lines

def include(lines,i,file):
    lines[i:i+1]=get_lines(file)
    return lines

def check_include(file,outputs):
    print("check"+file)
    f=open(file,encoding="utf-8")
    lines=f.readlines()
    f.close()
    included=False
    i=0
    while(i<len(lines)):
        inc=re.match("<include .*>",lines[i])
        if inc is not None:
            i_file=inc.group()[9:-1]
            include(lines,i,i_file)
            included=True
        i+=1
    if included==True:
        print("included"+file)
        path=outputs+file[2:]

        f=open(path,mode="w",encoding="utf-8")
        f.writelines(lines)
        f.close()

def output(dir,outputs="../"):
    print(dir)
    for f in sorted(os.listdir(dir)):
        if dir=="./":
            path=dir+f
        else:
            path=dir+"/"+f
        if os.path.isdir(path):
            if path!=outputs and path!="./include":
                os.makedirs(outputs+path[2:], exist_ok=True)
                output(path,outputs)
        else:
            if path!="./include.py":
                check_include(path,outputs)

output("./")
