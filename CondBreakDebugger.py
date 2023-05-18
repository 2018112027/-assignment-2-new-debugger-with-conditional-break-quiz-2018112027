from utils import next_inputs, input
import sys
import ast
from debuggingbook.Debugger import Debugger

class CondBreakDebugger(Debugger):
    def set_command(self, arg: str = "") -> None:
        token = arg.split('=')
        var = token[0].strip()
        value = token[1].strip()
        
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            pass
            
        if var in self.local_vars:
            self.frame.f_locals[var] = value
            print(f"Set {var} to {value}")
        else:
            print(f"Variable {var} not found")
