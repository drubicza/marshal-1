import os
import time

m11 = '\033[1m'
m00 = '\033[0;0m'
m31 = '\033[31m'
m32 = '\033[32m'
m33 = '\033[33m'
m34 = '\033[34m'
m35 = '\033[35m'
m36 = '\033[36m'
m37 = '\033[37m'
m90 = '\033[90m'
m91 = '\033[91m'
m92 = '\033[92m'
m93 = '\033[93m'
m94 = '\033[94m'
m95 = '\033[95m'
m96 = '\033[96m'
m97 = '\033[97m'
flag = '\033[1;97;41m'

def logo():
    os.system("clear");time.sleep(1)
    print(f"""\n\n{m11}{m96}
  ┬─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ┬─┐┌─┐┌┬┐┌─┐┬┬  ┌─┐┬─┐
  ├─┘└┬┘ │ ├─┤│ ││││  │  │ ││││├─┘││  ├┤ ├┬┘
  ┴   ┴  ┴ ┴ ┴└─┘┘└┘  └─┘└─┘┴ ┴┴  ┴┴─┘└─┘┴└─
  {flag} Simple marshal compiler by NjankSoekamti {m00}
  {m11}{m95}------------------------------------------{m00}""");time.sleep(0.1)

def out():
    time.sleep(0.1)
    print(f"  {m00}[{m91}x{m00}] {m91}Thanks for using this tool");os.system("xdg-open https://youtube.com/NjankSoekamti");
    time.sleep(0.1)
    exit(f"  {m00}[{m91}x{m00}] {m91}Exit!\n")

try:
    logo()
    print(f"  [{m92}+{m00}] {m92}What your python version{m00} \n");time.sleep(0.1)
    print(f"    {m00}  [{m36}1{m00}] {m36}Python ");time.sleep(0.1)
    print(f"    {m00}  [{m36}2{m00}] {m36}Python2 ");time.sleep(0.1)
    print(f"    {m00}  [{m31}0{m00}] {m31}Exit \n ");time.sleep(0.1)
    ask = input(f"  {m92}>>>{m00} ");time.sleep(0.1)
    if ask == "1":
        os.system("python .py3")
    elif ask == "2":
        os.system("python2 .py2")
    else:
        out()

except KeyboardInterrupt:
    out()
