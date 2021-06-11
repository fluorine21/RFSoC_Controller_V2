-- Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2020.2 (win64) Build 3064766 Wed Nov 18 09:12:45 MST 2020
-- Date        : Wed Jun  9 15:11:36 2021
-- Host        : JAMES-FLOOR4 running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
--               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ top_level_system_ila_0_0_stub.vhdl
-- Design      : top_level_system_ila_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xczu29dr-ffvf1760-2-e
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix is
  Port ( 
    clk : in STD_LOGIC;
    probe0 : in STD_LOGIC_VECTOR ( 15 downto 0 );
    SLOT_0_AXIS_tdata : in STD_LOGIC_VECTOR ( 31 downto 0 );
    SLOT_0_AXIS_tlast : in STD_LOGIC;
    SLOT_0_AXIS_tvalid : in STD_LOGIC;
    SLOT_0_AXIS_tready : in STD_LOGIC;
    SLOT_1_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_1_AXIS_tlast : in STD_LOGIC;
    SLOT_1_AXIS_tvalid : in STD_LOGIC;
    SLOT_1_AXIS_tready : in STD_LOGIC;
    SLOT_2_AXIS_tdata : in STD_LOGIC_VECTOR ( 31 downto 0 );
    SLOT_2_AXIS_tlast : in STD_LOGIC;
    SLOT_2_AXIS_tvalid : in STD_LOGIC;
    SLOT_2_AXIS_tready : in STD_LOGIC;
    SLOT_3_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_3_AXIS_tlast : in STD_LOGIC;
    SLOT_3_AXIS_tvalid : in STD_LOGIC;
    SLOT_3_AXIS_tready : in STD_LOGIC;
    SLOT_4_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_4_AXIS_tlast : in STD_LOGIC;
    SLOT_4_AXIS_tvalid : in STD_LOGIC;
    SLOT_4_AXIS_tready : in STD_LOGIC;
    SLOT_5_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_5_AXIS_tlast : in STD_LOGIC;
    SLOT_5_AXIS_tvalid : in STD_LOGIC;
    SLOT_5_AXIS_tready : in STD_LOGIC;
    SLOT_6_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_6_AXIS_tlast : in STD_LOGIC;
    SLOT_6_AXIS_tvalid : in STD_LOGIC;
    SLOT_6_AXIS_tready : in STD_LOGIC;
    SLOT_7_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_7_AXIS_tlast : in STD_LOGIC;
    SLOT_7_AXIS_tvalid : in STD_LOGIC;
    SLOT_7_AXIS_tready : in STD_LOGIC;
    SLOT_8_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_8_AXIS_tlast : in STD_LOGIC;
    SLOT_8_AXIS_tvalid : in STD_LOGIC;
    SLOT_8_AXIS_tready : in STD_LOGIC;
    SLOT_9_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_9_AXIS_tlast : in STD_LOGIC;
    SLOT_9_AXIS_tvalid : in STD_LOGIC;
    SLOT_9_AXIS_tready : in STD_LOGIC;
    SLOT_10_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_10_AXIS_tlast : in STD_LOGIC;
    SLOT_10_AXIS_tvalid : in STD_LOGIC;
    SLOT_10_AXIS_tready : in STD_LOGIC;
    SLOT_11_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_11_AXIS_tlast : in STD_LOGIC;
    SLOT_11_AXIS_tvalid : in STD_LOGIC;
    SLOT_11_AXIS_tready : in STD_LOGIC;
    SLOT_12_AXIS_tdata : in STD_LOGIC_VECTOR ( 255 downto 0 );
    SLOT_12_AXIS_tlast : in STD_LOGIC;
    SLOT_12_AXIS_tvalid : in STD_LOGIC;
    SLOT_12_AXIS_tready : in STD_LOGIC;
    SLOT_13_AXIS_tdata : in STD_LOGIC_VECTOR ( 127 downto 0 );
    SLOT_13_AXIS_tlast : in STD_LOGIC;
    SLOT_13_AXIS_tvalid : in STD_LOGIC;
    SLOT_13_AXIS_tready : in STD_LOGIC;
    resetn : in STD_LOGIC
  );

end decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix;

architecture stub of decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "clk,probe0[15:0],SLOT_0_AXIS_tdata[31:0],SLOT_0_AXIS_tlast,SLOT_0_AXIS_tvalid,SLOT_0_AXIS_tready,SLOT_1_AXIS_tdata[255:0],SLOT_1_AXIS_tlast,SLOT_1_AXIS_tvalid,SLOT_1_AXIS_tready,SLOT_2_AXIS_tdata[31:0],SLOT_2_AXIS_tlast,SLOT_2_AXIS_tvalid,SLOT_2_AXIS_tready,SLOT_3_AXIS_tdata[255:0],SLOT_3_AXIS_tlast,SLOT_3_AXIS_tvalid,SLOT_3_AXIS_tready,SLOT_4_AXIS_tdata[255:0],SLOT_4_AXIS_tlast,SLOT_4_AXIS_tvalid,SLOT_4_AXIS_tready,SLOT_5_AXIS_tdata[255:0],SLOT_5_AXIS_tlast,SLOT_5_AXIS_tvalid,SLOT_5_AXIS_tready,SLOT_6_AXIS_tdata[255:0],SLOT_6_AXIS_tlast,SLOT_6_AXIS_tvalid,SLOT_6_AXIS_tready,SLOT_7_AXIS_tdata[255:0],SLOT_7_AXIS_tlast,SLOT_7_AXIS_tvalid,SLOT_7_AXIS_tready,SLOT_8_AXIS_tdata[255:0],SLOT_8_AXIS_tlast,SLOT_8_AXIS_tvalid,SLOT_8_AXIS_tready,SLOT_9_AXIS_tdata[255:0],SLOT_9_AXIS_tlast,SLOT_9_AXIS_tvalid,SLOT_9_AXIS_tready,SLOT_10_AXIS_tdata[255:0],SLOT_10_AXIS_tlast,SLOT_10_AXIS_tvalid,SLOT_10_AXIS_tready,SLOT_11_AXIS_tdata[255:0],SLOT_11_AXIS_tlast,SLOT_11_AXIS_tvalid,SLOT_11_AXIS_tready,SLOT_12_AXIS_tdata[255:0],SLOT_12_AXIS_tlast,SLOT_12_AXIS_tvalid,SLOT_12_AXIS_tready,SLOT_13_AXIS_tdata[127:0],SLOT_13_AXIS_tlast,SLOT_13_AXIS_tvalid,SLOT_13_AXIS_tready,resetn";
attribute X_CORE_INFO : string;
attribute X_CORE_INFO of stub : architecture is "bd_9bbd,Vivado 2020.2";
begin
end;
