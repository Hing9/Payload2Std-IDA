#-*- coding: utf-8 -*-

import idaapi


UTIL_VERSION = 100

PLUGIN_NAME = "Payload2Std"
PLUGIN_VERSION = [0,0,1]
IS_DEBUG = False


inf = idaapi.get_inf_structure()
WORD_SIZE = 2
if inf.is_32bit():
    WORD_SIZE = 4
elif inf.is_64bit():
    WORD_SIZE = 8



def debugline(msg):
    if IS_DEBUG:
        print("[DEBUG:%s] %s"%(PLUGIN_NAME, msg))

def writeline(msg):
    print("[%s] %s"%(PLUGIN_NAME, msg))

def strToHex(string):
    try:
        return ''.join(["%02X" % ord(x) for x in string])
    except:
        return "??"

def readMemory(address, size):
    if idaapi.dbg_can_query():
        val = idaapi.dbg_read_memory(address, size)

        return val
    return None
        



class HotKeyManager():
    def __init__(self):
        self.keys = []

    def add(self, hotkey, func):
        hk = idaapi.add_hotkey(hotkey, func)
        if hk is None:
            debugline("hot key %s load fail" % hotkey)
            del hk
            return False
        else:
            self.keys.append((hotkey, func,))
            return True



class ActionHandler(idaapi.action_handler_t):
    def __init__(self, id, callback):
        idaapi.action_handler_t.__init__(self)
        self.callback = callback
        self.id = id


    def activate(self, ctx):
        return self.callback()


    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS


class ActionManager():
    def __init__(self):
        self._actions = {}

    def register(self, id, content, callback, icon=-1, shortcut=None):
        nid = self._convert(id)
        action = idaapi.action_desc_t(nid, content, ActionHandler(nid, callback), shortcut, None, icon)
        self._actions[id] = action
        idaapi.register_action(action)
    
    def get(self, id):
        return self._convert(id)

    def cleanup(self):
        for i in self._actions:
            idaapi.unregister_action(i)
    
    def _convert(self, id):
        return PLUGIN_NAME + ":" + id
    
    





class UIHook(idaapi.UI_Hooks):
    def __init__(self):
        idaapi.UI_Hooks.__init__(self)
        
        self.popups = []


    def finish_populating_tform_popup(self, form, popup):
        #formtype = idaapi.get_tform_type(form)

        #if formtype == idaapi.BWN_DISASM or idaapi.BWN_DUMP:

        for action, position, condition in self.popups:
            if condition(form):
                idaapi.attach_action_to_popup(form, popup, action, position)


    def addPopup(self, action, position="", condition = lambda f:True):
        self.popups.append((action, position, condition))
