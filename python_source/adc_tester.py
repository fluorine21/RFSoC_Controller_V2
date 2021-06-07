

import rfsoc_board_driver as rbd
import waveform_plotter as wp

portname = "COM15"
num_pulses = 256
dac_chan_num = 0
adc_channel_num = 0
dac_pre_delay = 10
adc_shift = 0
adc_run_cycles = num_pulses + 20


#Set up the ramp for the outgoing DAC channel to the modulator
dac_wave = []


square_wave = [rbd.DAC_MAX_VALUE]*8 + [rbd.DAC_MIN_VALUE]*8

for i in range(0, num_pulses):
    scale = (i+1)/num_pulses
    d_w = [e*scale for e in square_wave]
    dac_wave += d_w
    
#Cast everything to int to avoid later problems
for i in range(0, len(dac_wave)):
    dac_wave[i] = int(dac_wave[i])
    

#set up the dac channel
d_chan = rbd.rfsoc_channel("DAC", dac_chan_num, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
d_chan.mask_enable = 0
d_chan.waveform_samples = dac_wave
d_chan.run_cycles = int(len(dac_wave)/16);
d_chan.pre_delay_cycles = dac_pre_delay
d_chan.post_delay_cycles = 16


#set up the adc channel
a_chan = rbd.rfsoc_channel(
    "ADC", 
    adc_channel_num, 
    0, 
    0, 
    0,
    0,
    0,
    0,
    0,
    "",
    "",
    adc_shift, 
    adc_run_cycles)

#Create the driver object
board_obj = rbd.rfsoc_board(portname)

#Add the ADC and DAC channels to the board driver
board_obj.channel_list = [a_chan, d_chan]

#plot the DAC waveform
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
    
#Plot the adc waveform
adc_data = board_obj.readout_adc(0)
    
if(adc_data == []):
    raise RuntimeError("Error reading out ADC data")
    
    
wp.plot_adc_waveform(adc_data)
