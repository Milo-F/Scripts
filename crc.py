#! /usr/bin/python3
import sys
import getopt

def crc_gen(argv):
    k = 0 # 有效数据宽度
    n = 0 # 加上校验位之后的总长度
    try:
        opts, args = getopt.getopt(argv, "hk:n:", ["help"])
    except:
        print('Error: get parameter error!')
        print("Format: crc.py -k Integer -n Integer")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('usage: crc.py -k Integer -n Integer')
            print("Options and arguments:")
            print("-k\t\t: width of valid data to be verified")
            print("-n\t\t: Full frame length including check CRC digit")
            print("-h(--help) \t: get help")
            sys.exit()
        else:
            try:
                arg = int(arg)
            except:
                print("Error: Invalid parameters!")
                sys.exit()
            if opt == "-k":
                k = int(arg)
            elif opt == "-n":
                n = int(arg)
            else:
                print('crc.py -k Integer -n Integer')
                sys.exit()
    x = n-k+1
    with open("crc_verilog.txt", "w") as f: 
        # crc多项式
        f.writelines("// 将 #You CRC# 替换你的crc多项式\n")
        f.writelines("localparam [{}:0] crc_num = #Your CRC#;\n".format(x-1))
        # crc_out定义
        f.writelines("\n// wires defination\n")
        f.writelines("wire [{}:0] ".format(x-2)+"crc_out;\n")
        # crc wires定义
        f.writelines("wire [{}:0] ".format(x-1))
        code = "crc_0"
        for i in range(1, n-x+1):
            code = code + ", crc_{}".format(i)
        f.writelines(code+";\n")
        # assign 语句
        f.writelines("\n// logic assign\n")
        code = "assign " + "crc_{} ".format(0) + "= " + "data[{}:{}] ".format(n-1, n-x) + "^ (data[39] ? crc_num : {}'b0)".format(x) + ";\n"
        f.writelines(code)
        for i in range(1, n-x+1):
            code = "assign " + "crc_{} ".format(i) + "= " + "{" + "crc_{}[{}:0], data[{}]".format(i-1, x-2, n-x-i) + "} " + "^ (crc_{}[{}] ? crc_num : {}'b0)".format(i-1, x-2, x) + ";\n"
            f.writelines(code)
        code = "assign " + "crc_out " + "= " + "crc_{}[{}:0]".format(n-x, x-2) + ";\n"
        f.writelines(code)
        print("Finish CRC code generate in file \"crc_verilog.txt\".")
        f.close()    

if __name__ == "__main__":
    crc_gen(sys.argv[1:])
