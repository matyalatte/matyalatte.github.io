import re,os

def get_lines(file):
    f=open(file,encoding="utf-8")
    lines=f.readlines()
    f.close()
    return lines

def include(lines,i,file):
    lines[i:i+1]=get_lines(file)
    return lines

dir_=[".","qrcoder","memo","petitcom","qr_make",
      "qr_make_array","qr_cal_size","qr_make_from_slot",
      "qr_extract_txt","qr_set_color","qr_get_color",
      "qr_set_show_info","qr_get_show_info","reference","sample",
      "qr_make_txt","softbody","danmaku","ballfall"]
dir_n=["トップ","QR CODER","勉強メモ","プチコン作品一覧","QR_MAKE",
       "QR_MAKE_ARRAY","QR_CAL_SIZE","QR_MAKE_FROM_SLOT",
       "QR_EXTRACT_TXT","QR_SET_COLOR","QR_GET_COLOR",
       "QR_SET_SHOW_INFO","QR_GET_SHOW_INFO","リファレンス","サンプル",
       "QR_MAKE_TXT","SOFTBODYsimulator","弾幕ボスバトル","BALLFALL"]
def get_ref(dir):
    global dir_,dir_n
    for j in range(len(dir_)):
        if dir==dir_[j]:
            return dir_n[j]
    return "***"

def include_tree(lines,i,file):
    f=file.split("/")
    line=""
    ur="<a href=\"https://matyalatte.github.io/"
    l="\">"
    max_i=len(f)-2
    for j in range(max_i+1):
        if j==0:
            path=ur+l
        elif j==max_i:
            path="&gt"
        else:
            path="&gt"+ur+"/".join(f[1:j+1])+l
        line=line+path+get_ref(f[j])
        if j!=max_i:
            line=line+"</a>"
    lines[i:i+1]=line
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
            lines=include(lines,i,i_file)
            included=True
            continue
        tree=re.match("<tree here>",lines[i])
        if tree is not None:
            lines=include_tree(lines,i,file)
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
