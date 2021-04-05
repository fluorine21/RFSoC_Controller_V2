

import rfsoc_board_driver as rbd

portname = "COM15"
board_obj = rbd.rfsoc_board(portname)

scale = 0.5

#generate our test waveform for a single pulse

wave_single_pulse = [round(rbd.DAC_MAX_VALUE * scale)]*8 + [0]*8 + [0] * 64
single_pulse_cycles = round(len(wave_single_pulse)/16)

#Set up our test channel
chan = rbd.rfsoc_channel("DAC", 4, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
chan.waveform_samples = wave_single_pulse
chan.run_cycles = single_pulse_cycles


#Add the test channel to the board object
board_obj.channel_list = [chan]

#Configure the board
if(board_obj.configure_all_channels()):
    raise RuntimeError("Error, could not configure channels for amp test")

print("Press any key to trigger board for single pulse test");

dummy = input()

#Trigger the board once
if(board_obj.trigger()):
    raise RuntimeError("Error triggering board")

#Create the ramp pulse train


wave_ramp = []

for i in range(1, 100):
    v = round(rbd.DAC_MAX_VALUE*((100-i)/100) * scale)
    wave_ramp += [v] * 8 + [-1*v] * 8
    
ramp_cycles = round(len(wave_ramp)/16)

#Update our test channel
chan.waveform_samples = wave_ramp
chan.run_cycles = ramp_cycles

#Configure the board
if(board_obj.configure_all_channels()):
    raise RuntimeError("Error, could not configure channels for amp test")

print("Press any key to trigger board for ramp test")


dummy = input()

#Trigger the board once
if(board_obj.trigger()):
    raise RuntimeError("Error triggering board")
    
    
chan.locking_waveform_samples = [round(rbd.DAC_MAX_VALUE * scale)]*8
chan.locking_waveform_samples += [round(rbd.DAC_MAX_VALUE * scale * -1)]*8  

print("Press any key to do continuous pulse test")

dummy = input()

if(board_obj.configure_all_channels()):
    raise RuntimeError("Error, could not configure channels for amp test")

print("Done!")





