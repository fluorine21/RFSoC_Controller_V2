import waveform_plotter as wp


import rfsoc_board_driver as rbd

i_chan_num = 0
q_chan_num = 1

#In number of samples
i_del = 0
q_del = 0

#Construct the test waveforms

i_wave = [];
q_wave = [];

#Need to do some calibration since the actual I and Q readings will be a mixture of each other given the path to the detector isn't locked

#Start by sending out a max amp i pulse
for i in range(0, 16):
    i_wave += [rbd.DAC_MAX_VALUE]*8 + [rbd.DAC_MIN_VALUE]*8
    q_wave += [0]*16
    
#add a dead time
i_wave += [0]*16*16
q_wave += [0]*16*16
    
#Then send out a max amp q pulse
for i in range(0, 16):
    q_wave += [rbd.DAC_MAX_VALUE]*8 + [rbd.DAC_MIN_VALUE]*8
    i_wave += [0]*16
    
#add a dead time
i_wave += [0]*16*16
q_wave += [0]*16*16
    
#Then do an i ramp
for i in range(0, 256)
    val_p = int(((i+1)/256)*rbd.DAC_MAX_VALUE)
    val_n = int(((i+1)/256)*rbd.DAC_MIN_VALUE)
    i_wave += [val_p]*8 + [val_n]*8
    q_wave += [0]*16
    
#add a dead time
i_wave += [0]*16*16
q_wave += [0]*16*16
    
#Then to a q ramp
for i in range(0, 256)
    val_p = int(((i+1)/256)*rbd.DAC_MAX_VALUE)
    val_n = int(((i+1)/256)*rbd.DAC_MIN_VALUE)
    q_wave += [val_p]*8 + [val_n]*8
    i_wave += [0]*16

#add a dead time
i_wave += [0]*16*16
q_wave += [0]*16*16

#Now rotate I and Q in a circle
freq = 2*math.pi*(1/256)
#Should go around circle 1 time
for i in range(0, 256)
    val_i = int(math.cos(freq*i)*rbd.DAC_MAX_VALUE)
    val_p = int(math.sin(freq*i)*rbd.DAC_MAX_VALUE)
    q_wave += [val_q]*8 + [val_q*-1]*8
    i_wave += [val_i]*8 + [val_i*-1]*8 
    
    
#Finalize the waveforms with the correct delays
i_c = int(i_del/16)
q_c = int(q_del/16)
i_del = i_del % 16
q_del = q_del % 16
i_wave_f = [0]*i_del + i_wave + [0]*(16-i_del)
q_wave_f = [0]*q_del + q_wave + [0]*(16-q_del)

#Board object to be used
board_obj = rbd.rfsoc_board(portname)

#Set up the channel object
i_chan = rbd.rfsoc_channel("DAC", i_chan_num, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
i_chan.mask_enable = 0
i_chan.waveform_samples = i_wave_f
i_chan.run_cycles = int(len(i_wave)/16);
i_chan.pre_delay_cycles = i_c
i_chan.post_delay_cycles = 16

#Set up the channel object
q_chan = rbd.rfsoc_channel("DAC", q_chan_num, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
q_chan.mask_enable = 0
q_chan.waveform_samples = q_wave_f
q_chan.run_cycles = int(len(q_wave)/16);
q_chan.pre_delay_cycles = q_c
q_chan.post_delay_cycles = 16
    
#Add the channels to the rfsoc object
board_obj.channel_list = [i_chan, q_chan];  


wp.plot_dac_waveforms(board_obj.channel_list)

#Check the status of the clocks
board_obj.board_driver.open_board()
dac_status, adc_status = board_obj.board_driver.check_clocks()
board_obj.board_driver.close_board()
if(dac_status):
    raise RuntimeError("Error, the DAC RF clock for the FPGA was not detected, cannot upload waveforms without an RF clock present")
    
#Configure the board
if(board_obj.configure_all_channels()):
    raise RuntimeError("Error, could not configure channels for DAC test")
    
#Trigger the board once
if(board_obj.trigger()):
    raise RuntimeError("Error triggering board")
    
if(board_obj.trigger()):
    raise RuntimeError("Error triggering board")
    
     