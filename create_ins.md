# Module实例代码生成器
&emsp;&emsp;用于自动生成模块的对应实例的代码，可以通过命令行参数配置生成代码的实例名和输出文件名。通过执行create_ins.py -h获取帮助：
```
usage: create_ins.py -f file_name <-o out_file> <-i ins_name>
Options and arguments:
        -f --file_name= : input verilog file with one module inside
        -o --out_file=  : instance code output file
        -i --ins_name=  : input a instance name you want
        -h --help=      : get help
```
输出文件名默认值为："原文件名".inst

输出实例默认名为："模块名"_ins

## Example
使用命令
```
./creat_ins.py -f crc.v -o crc.inst -i crc_inst_0
```
生成[crc](./crc.v)模块的名为crc_inst_0的实例，并输出到[crc.inst](./crc.inst)文件中。生成的实例代码如下：
```
crc #(
	.A(),
	.B()
) crc_inst_0 (
	.clk(),
	.rst_n(),
	.data_in(),
	.data_out()
);
```