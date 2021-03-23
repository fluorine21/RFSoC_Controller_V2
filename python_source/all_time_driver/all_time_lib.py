# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:09:05 2021

@author: James
"""

import rfsoc_board_driver as rbd
import math

#This file has all of the functions for calibrating and implementing the all time architecture on the RFSoC_V2 platform

EMPTY_VAL = 0xDEADBEEFDEADBEEF

class transfer_function:
    
    input_list = []
    output_list = []
    
    #Adds or overwrites a pair in the list
    #Throws an error if list will be longer than 256
    def add_pair(self, in_p, out_p):

        #Try finding the matching value first to see if we're updating it
        for i in range(0, len(self.input_list)):
            if(self.input_list[i] == in_p):
                self.output_list[i] = out_p
                return
        #If we're here we didn't find anything
        if(len(self.input_list) >= 256):
            raise RuntimeError("Error, transfer function table size cannot be greater than 256")
        self.input_list.append(in_p)
        self.output_list.append(out_p)
        return
        
    #Returns the output and the closest matching input
    def get_pair(self, in_p):
        min_error = 99999999999
        min_err_pos = 0
        for i in range(0, len(self.input_list)):
            err = abs(self.input_list[i]-in_p)
            if(err < min_error):
                min_err = err
                min_err_pos = i
        return self.output_list[i], self.input_list[i]
        
    
    
        


class all_time_obj:
    
    
    #We're computing a + (b*c)
    
    
    #Input to DAC transfer functions
    #256 entrties representing 0
    a_to_dac_tf = None





#Simplified interface between board object and all-time library
class all_time_rfsoc_interface:
    
    #Board object to be used
    board_obj = None
    
    a_im_channel_num = None
    a_pm_channel_num = None
    b_im_channel_num = None
    b_pm_channel_num = None
    c_im_channel_num = None
    c_pm_channel_num = None
    a_atten_channel_num = None
    adc_channel_num = None
    
    
    def __init__(self):
        
        #TODO
        
        return
    
    

    #Inputs are 16-bit values to be fed to DAC
    #im is intensity modulator, pm is phase modulator
    #a_atten is intensity modulator before 50/50
    #a_del is the delay in ns when driving a channel, must be between 0 and 4ns
    #Each output pulse is 4ns
    #adc_avgs is the number of ADC averages to take, must be a power of 2
    def run_exp(self, a_im, a_pm, b_im, b_pm, c_im, c_pm, a_atten, a_del, b_del, c_del, adc_avgs):
        
        if(a_del > 4 or b_del > 4 or c_del > 4 or a_del < 0 or b_del < 0 or c_del < 0):
            raise ValueError("Error, channel delay must be less than 4ns and greater or equal to 0ns")
        #If our adc averages is 0 or not a power of 2
        if(adc_avgs == 0 or math.log(adc_avgs, 2) != round(math.log(adc_avgs, 2))):
            raise ValueError("Error, adc averages must be greater than 0 and a power of 2")
        
        
        #Deal with channel A first
        a_im_wave = self.get_waveform(a_im, a_del)
        a_pm_wave = self.get_waveform(a_pm, a_del)
        a_im_chan = self.setup_channel(a_im_wave, self.a_im_channel_num)
        a_pm_chan = self.setup_channel(a_pm_wave, self.a_pm_channel_num)
        
        b_im_wave = self.get_waveform(b_im, b_del)
        b_pm_wave = self.get_waveform(b_pm, b_del)
        b_im_chan = self.setup_channel(b_im_wave, self.b_im_channel_num)
        b_pm_chan = self.setup_channel(b_pm_wave, self.b_pm_channel_num)
        
        c_im_wave = self.get_waveform(c_im, c_del)
        c_pm_wave = self.get_waveform(c_pm, c_del)
        c_im_chan = self.setup_channel(c_im_wave, self.c_im_channel_num)
        c_pm_chan = self.setup_channel(c_pm_wave, self.c_pm_channel_num)
        
        a_atten_wave = self.get_waveform(a_atten, a_del)
        a_atten_chan = self.setup_channel(a_atten_wave, self.a_atten_channel_num)
        
        #Add the ADC channel

        adc_chan = rbd.rfsoc_channel("ADC", self.adc_channel_num, 0, 0, 0, 0, 8, 1, 1, "", "", math.log(adc_avgs, 2), 32)

        #Clear anything that's currently in the board object and add our channels
        self.board_obj.channel_list =  [a_im_chan, 
                                        a_pm_chan, 
                                        b_im_chan, 
                                        b_pm_chan,
                                        c_im_chan, 
                                        c_pm_chan, 
                                        a_atten_chan,
                                        adc_chan]
        
        #Check to see if the board is up
        
        
        
        
        
    #Generates a constant amplitude waveform for the channel
    def get_waveform(self, amp, delay):
        wf = [0]*16
        d_samp = round(delay * 4)
        samp_num = 0
        for i in range(0, 16):
            #If we're not in the delay still and we haven't had 16 samples (4ns) yet
            if(i >= d_samp and samp_num < 16):
                wf[i] = amp
                samp_num += 1
        return wf
      
    def setup_channel(self, waveform, chann_num):
        chan = rbd.rfsoc_channel("DAC", chann_num, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
        chan.waveform_samples = waveform
        chan.run_cycles = 2
        return chan
        
    #Same as run_exp but now everything is a list of stuff to run sequentially
    #Returns ADC values read out
    def run_exp_list(self, a_im, a_pm, b_im, b_pm, c_im, c_pm, a_atten, a_del, b_del, c_del, adc_avgs):
        
        if(a_del > 4 or b_del > 4 or c_del > 4 or a_del < 0 or b_del < 0 or c_del < 0):
            raise ValueError("Error, channel delay must be less than 4ns and greater or equal to 0ns")
        #If our adc averages is 0 or not a power of 2
        if(adc_avgs == 0 or math.log(adc_avgs, 2) != round(math.log(adc_avgs, 2))):
            raise ValueError("Error, adc averages must be greater than 0 and a power of 2")
        
        #Deal with channel A first
        a_im_wave, a_im_del = self.get_waveform_list(a_im, a_del)
        a_pm_wave, a_pm_del = self.get_waveform_list(a_pm, a_del)
        a_im_chan = self.setup_channel_list(a_im_wave, self.a_im_channel_num, a_im_del)
        a_pm_chan = self.setup_channel_list(a_pm_wave, self.a_pm_channel_num, a_pm_del)
        
        b_im_wave, b_im_del = self.get_waveform_list(b_im, b_del)
        b_pm_wave, b_pm_del = self.get_waveform_list(b_pm, b_del)
        b_im_chan = self.setup_channel_list(b_im_wave, self.b_im_channel_num, b_im_del)
        b_pm_chan = self.setup_channel_list(b_pm_wave, self.b_pm_channel_num, b_pm_del)
        
        c_im_wave, c_im_del = self.get_waveform_list(c_im, c_del)
        c_pm_wave, c_pm_del = self.get_waveform_list(c_pm, c_del)
        c_im_chan = self.setup_channel_list(c_im_wave, self.c_im_channel_num, c_im_del)
        c_pm_chan = self.setup_channel_list(c_pm_wave, self.c_pm_channel_num, c_pm_del)
        
        a_atten_wave, a_atten_del = self.get_waveform_list(a_atten, a_del)
        a_atten_chan = self.setup_channel_list(a_atten_wave, self.a_atten_channel_num, a_atten_del)
        
        #Add the ADC channel

        adc_chan = rbd.rfsoc_channel("ADC", self.adc_channel_num, 0, 0, 0, 0, 8, 1, 1, "", "", math.log(adc_avgs, 2), 32)

        #Clear anything that's currently in the board object and add our channels
        self.board_obj.channel_list =  [a_im_chan, 
                                        a_pm_chan, 
                                        b_im_chan, 
                                        b_pm_chan,
                                        c_im_chan, 
                                        c_pm_chan, 
                                        a_atten_chan,
                                        adc_chan]   
        #Check the status of the clocks
        self.board_obj.board_driver.open_board()
        dac0, dac1, dac2, dac3, adc0, adc1, adc2, adc3 = self.board_obj.board_driver.check_clocks(full_stats = 1)
        self.board_obj.board_driver.close_board()
        if(dac0 or dac1):
            raise RuntimeError("Error, the DAC RF clock for the FPGA was not detected, cannot upload waveforms without an RF clock present")
        if(adc0):
            raise RuntimeError("Error, the ADC RF clock for the FPGA was not detected, cannot read out ADC")
            
        #Load the board with the channels
        if(self.board_obj.configure_all_channels()):
            raise RuntimeError("Error, could not configure channels for DAC test")
        
        adc_num_trigs = math.log2(adc_avgs)
        
        for i in range(0, adc_num_trigs):
            if(self.board_obj.trigger()):
                raise RuntimeError("Error triggering board")
            else:
                print("Trigger #" + str(i))
                
        #Read out the adc
        adc_samples = self.board_obj.readout_adc(self.adc_channel_num);
        return adc_samples
            
            
            
    #Returns coarse delay (in fpga cycles) and then waveform
    def get_waveform_list(self, amp_list, delay):
        
        #Each sample will occupy 4ns of time (16 samples), so our total length is
        coarse_delay = round(delay/4) #in fpga cycles
        fine_delay = int((delay*4)%16) #in samples
        
        wf = [0]*fine_delay
        
        #Build the actual waveform with the correct amplutudes
        #50% duty cycle, 2ns on 2ns off
        for a in amp_list:
            wf += ([a]*8) + ([0]*8)
            
        #Making sure waveform is a multiple of 16 samples so it fits in the fifo correctly
        while(len(wf)%16 != 0):
            wf.append(0)
        
        return coarse_delay, wf
            
            
    def setup_channel_list(self, waveform, chann_num, coarse_delay):
        chan = rbd.rfsoc_channel("DAC", chann_num, 0, 0, 0, 0, 8, 1, 1, "", "", 0, 0)
        chan.mask_enable = 0
        chan.waveform_samples = waveform
        chan.run_cycles = int(len(waveform)/16)
        chan.pre_delay_cycles = coarse_delay
        chan.post_delay_cycles = 16
        return chan  

        
        
        
        