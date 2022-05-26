# CRC校验代码生成
&emsp;&emsp;[crc.py](./crc.py)用于产生给定数据长度和帧长度的CRC校验逻辑代，通过执行./crc.py -h可以得到如下
```
usage: crc.py -k Integer -n Integer
Options and arguments:
        -k              : width of valid data to be verified
        -n              : Full frame length including check CRC digit
        -h --help       : get help
```
使用命令
```
./crc.py -k 5 -n 8
```
通过该生成器生成的CRC verilog代码如下：
```
// 将 #You CRC# 替换你的crc多项式
localparam [3:0] crc_num = #Your CRC#;

// wires defination
wire [2:0] crc_out;
wire [3:0] crc_0, crc_1, crc_2, crc_3, crc_4;

// logic assign
assign crc_0 = data[7:4] ^ (data[7] ? crc_num : 4'b0);
assign crc_1 = {crc_0[2:0], data[3]} ^ (crc_0[2] ? crc_num : 4'b0);
assign crc_2 = {crc_1[2:0], data[2]} ^ (crc_1[2] ? crc_num : 4'b0);
assign crc_3 = {crc_2[2:0], data[1]} ^ (crc_2[2] ? crc_num : 4'b0);
assign crc_4 = {crc_3[2:0], data[0]} ^ (crc_3[2] ? crc_num : 4'b0);
assign crc_out = crc_4[2:0];
```
上述代码会保存在当前目录的[crc_verilog.txt](./crc_verilog.txt)中。