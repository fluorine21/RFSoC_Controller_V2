
import rfsoc_board_driver as rbd

portname = "COM4"
board_obj = rbd.rfsoc_board(portname)


#generate our test waveform for a single pulse

wave_single_pulse = [rbd.DAC_MAX_VALUE]*8 + [0]*8 + [0] * 64
single_pulse_cycles = round(len(wave_single_pulse)/16)

#Set up our test channel
chan = rbd.rfsoc_channel("DAC", 0, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
chan.waveform_samples = wave_single_pulse
chan.run_cycles = single_pulse_cycles


#Add the test channel to the board object
board_obj.channel_list.append(chan)

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

for i in range(100, 1):
    wave_ramp += [round(rbd.DAC_MAX_VALUE*(i/100))] * 8 + [0] * 8
    
ramp_cycles = round(len(wave_ramp)/16)

#Update our test channel
chan.waveform_samples = wave_ramp
chan.run_cycles = ramp_cycles

#Configure the board
if(board_obj.configure_all_channels()):
    raise RuntimeError("Error, could not configure channels for amp test")

print("Press any key to trigger board for single pulse test")

dummy = input()

print("Done!")





