#! /usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys, getopt

def get_help():
    print("usage: create_ins.py -f file_name <-o out_file> <-i ins_name>")
    print("Options and arguments:")
    print("\t-f --file_name=\t: input verilog file with one module inside")
    print("\t-o --out_file=\t: instance code output file")
    print("\t-i --ins_name=\t: input a instance name you want")
    print("\t-h --help=\t: get help")
    sys.exit()

def create_ins(argv):
    module_name = "" # 模块名字
    ins_name = "" # 实例名字
    given_ins_name = False # 是否指定了实例名字
    module_def = "" # 模块定义语句块
    params_def = "" # 参数定义语句块
    ports_def = "" # 端口定义语句块
    param_exist = False # 是否是参数化的模块
    output_list = [] # 输出实例调用
    param_list = [] # 参数名列表
    ports_list = [] # 端口名列表
    if len(argv) == 0:
        print("Error: missing parameters!")
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "hf:o:i:", ["help", "file_name=", "out_file=", "ins_name="])
    except:
        print("Error: get parameters error!")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            get_help()

        if opt in ("-f", "--file_name"):
            input_file = arg
        output_file = input_file.replace(".v", ".inst")
        if opt in ("-o", "--out_file"):
            output_file = arg
        if opt in ("-i", "--ins_name") :
            given_ins_name = True
            ins_name = arg

    with open(input_file, "r") as f:
        # 提取module name
        for line in f.readlines():
            line = line.strip()
            # 判断参数是否存在
            if re.compile(r"#").search(line):
                param_exist = True
            # 包含关键字module
            if re.compile(r"\bmodule\b").search(line):
                # 包含"("或者"#("
                if re.compile(r"[#]?\(").search(line):
                    module_def = re.search(r"\Amodule\b *\w*\b", line).group()
                    break
                else:    
                    module_def = module_def + line
            else:
                if re.compile(r"[#]?\(").search(line):
                    if re.compile(r"\w*").search(line):
                        module_def = module_def + " " + re.search(r"\w*", line).group()
                    break
                else:
                    module_def = module_def + " " + line
        module_name = re.search(r"\b\w*\b\Z", module_def).group()
        if not given_ins_name:
            ins_name = module_name + "_ins"
        print(ins_name)

        # 提取参数列表
        print (param_exist)
        if param_exist:
            pass


        f.close()

# mian
if __name__ == "__main__":
    create_ins(sys.argv[1:])