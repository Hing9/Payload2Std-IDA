from __future__ import print_function
import idaapi



def PLUGIN_ENTRY():
    from Payload2Std.plugin import Payload2StdPlugin
    return Payload2StdPlugin()
	
	
	
