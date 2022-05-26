#! /usr/bin/python3
import sys

if len(sys.argv) != 0:
    k = int(sys.argv[1])
    n = int(sys.argv[2])
else:
    # 数据位长度
    k = 32
    # 总长度
    n = 40
# CRC除数
x = n-k+1

with open("crc_verilog.txt", "w") as f: 
    # crc_out定义
    f.writelines("wire [{}:0] ".format(x-2)+"crc_out;\n")
    # crc wires定义
    f.writelines("wire [{}:0] ".format(x-1))
    code = "crc_0"
    for i in range(1, n-x+1):
        code = code + ", crc_{}".format(i)
    f.writelines(code+";\n")
    # assign 语句
    code = "assign " + "crc_{} ".format(0) + "= " + "data[{}:{}] ".format(n-1, n-x) + "^ (data[39] ? crc_num : {}'b0)".format(x) + ";\n"
    f.writelines(code)
    for i in range(1, n-x+1):
        code = "assign " + "crc_{} ".format(i) + "= " + "{" + "crc_{}[{}:0], data[{}]".format(i-1, x-2, n-x-i) + "} " + "^ (crc_{}[{}] ? crc_num : {}'b0)".format(i-1, x-2, x) + ";\n"
        f.writelines(code)
    code = "assign " + "crc_out " + "= " + "crc_{}[{}:0]".format(n-x, x-2) + ";\n"
    f.writelines(code)
    f.close()
