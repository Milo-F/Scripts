module crc #(
    A=7
)(
    input       wire                                        clk,
    input       wire                                        rst_n,
    input       wire        [31:0]                          data_in,
    output      reg         [39:0]                          data_out
);
    
    wire                    [39:0]                          data_out_nxt;
    wire                    [39:0]                          data;
    assign data              = {data_in, 8'b0};
    localparam [8:0] crc_num = 8'b1_0011_0001;
    wire                    [7:0]                           crc_out;
    wire                    [8:0]                           crc_0,crc_1,crc_2,crc_3,crc_4,crc_5,crc_6,crc_7,crc_8,crc_9,crc_10,crc_11,crc_12,crc_13,crc_14,crc_15,crc_16,crc_17,crc_18,crc_19,crc_20,crc_21,crc_22,crc_23,crc_24,crc_25,crc_26,crc_27,crc_28,crc_29,crc_30,crc_31;
    assign crc_0   = data[39:31] ^ (data[39] ? crc_num : 9'b0);
    assign crc_1   = {crc_0[7:0], data[30]} ^ (crc_0[7] ? crc_num : 9'b0);
    assign crc_2   = {crc_1[7:0], data[29]} ^ (crc_1[7] ? crc_num : 9'b0);
    assign crc_3   = {crc_2[7:0], data[28]} ^ (crc_2[7] ? crc_num : 9'b0);
    assign crc_4   = {crc_3[7:0], data[27]} ^ (crc_3[7] ? crc_num : 9'b0);
    assign crc_5   = {crc_4[7:0], data[26]} ^ (crc_4[7] ? crc_num : 9'b0);
    assign crc_6   = {crc_5[7:0], data[25]} ^ (crc_5[7] ? crc_num : 9'b0);
    assign crc_7   = {crc_6[7:0], data[24]} ^ (crc_6[7] ? crc_num : 9'b0);
    assign crc_8   = {crc_7[7:0], data[23]} ^ (crc_7[7] ? crc_num : 9'b0);
    assign crc_9   = {crc_8[7:0], data[22]} ^ (crc_8[7] ? crc_num : 9'b0);
    assign crc_10  = {crc_9[7:0], data[21]} ^ (crc_9[7] ? crc_num : 9'b0);
    assign crc_11  = {crc_10[7:0], data[20]} ^ (crc_10[7] ? crc_num : 9'b0);
    assign crc_12  = {crc_11[7:0], data[19]} ^ (crc_11[7] ? crc_num : 9'b0);
    assign crc_13  = {crc_12[7:0], data[18]} ^ (crc_12[7] ? crc_num : 9'b0);
    assign crc_14  = {crc_13[7:0], data[17]} ^ (crc_13[7] ? crc_num : 9'b0);
    assign crc_15  = {crc_14[7:0], data[16]} ^ (crc_14[7] ? crc_num : 9'b0);
    assign crc_16  = {crc_15[7:0], data[15]} ^ (crc_15[7] ? crc_num : 9'b0);
    assign crc_17  = {crc_16[7:0], data[14]} ^ (crc_16[7] ? crc_num : 9'b0);
    assign crc_18  = {crc_17[7:0], data[13]} ^ (crc_17[7] ? crc_num : 9'b0);
    assign crc_19  = {crc_18[7:0], data[12]} ^ (crc_18[7] ? crc_num : 9'b0);
    assign crc_20  = {crc_19[7:0], data[11]} ^ (crc_19[7] ? crc_num : 9'b0);
    assign crc_21  = {crc_20[7:0], data[10]} ^ (crc_20[7] ? crc_num : 9'b0);
    assign crc_22  = {crc_21[7:0], data[9]} ^ (crc_21[7] ? crc_num : 9'b0);
    assign crc_23  = {crc_22[7:0], data[8]} ^ (crc_22[7] ? crc_num : 9'b0);
    assign crc_24  = {crc_23[7:0], data[7]} ^ (crc_23[7] ? crc_num : 9'b0);
    assign crc_25  = {crc_24[7:0], data[6]} ^ (crc_24[7] ? crc_num : 9'b0);
    assign crc_26  = {crc_25[7:0], data[5]} ^ (crc_25[7] ? crc_num : 9'b0);
    assign crc_27  = {crc_26[7:0], data[4]} ^ (crc_26[7] ? crc_num : 9'b0);
    assign crc_28  = {crc_27[7:0], data[3]} ^ (crc_27[7] ? crc_num : 9'b0);
    assign crc_29  = {crc_28[7:0], data[2]} ^ (crc_28[7] ? crc_num : 9'b0);
    assign crc_30  = {crc_29[7:0], data[1]} ^ (crc_29[7] ? crc_num : 9'b0);
    assign crc_31  = {crc_30[7:0], data[0]} ^ (crc_30[7] ? crc_num : 9'b0);
    assign crc_out = crc_31[7:0];
    
    
    
    
    assign data_out_nxt = {data_in, crc_out};
    
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            data_out <= 0;
        end
        else begin
            data_out <= data_out_nxt;
        end
    end
    
endmodule
