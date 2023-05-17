from utils import next_inputs, input
import bookutils
import sys
from Debugger import Debugger

class CondBreakDebugger(Debugger):
    def set_command(self, arg: str = "") -> None:
    temp = arg.split(' ')
    var = temp[0]
    value = temp[2] 
    self.frame.f_locals[var] = value
class cbDebugger(Debugger):
    def attr_command(self, arg: str = "") -> None:
        temp = str.split(' ')
        OBJ = temp[0]
        VAR = temp[1]
        EXPR = temp[2] 
        
    
