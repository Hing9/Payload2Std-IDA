#-*- coding: utf-8 -*-

from __future__ import print_function
import idaapi
import ida_kernwin



class Payload2StdPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_HIDE
    comment = ""

    help = ""
    wanted_name = "Payload2Std"
    wanted_hotkey = ""




    def init(self):
        
        print("SUCCESS!!!")
        return idaapi.PLUGIN_KEEP


    def run(self, arg):
        pass


    def term(self):
        pass

