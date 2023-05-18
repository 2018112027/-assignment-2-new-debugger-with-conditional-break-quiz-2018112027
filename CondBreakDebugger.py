from utils import input, next_inputs
import sys
import ast
from typing import Any, Dict, TextIO
from debuggingbook.Debugger import Debugger

class CondBreakDebugger(Debugger):
    def __init__(self, *, file: TextIO = sys.stdout) -> None:
        self.breakvars: Dict[str, Any] = {}
        super().__init__(file = file)

class CondBreakDebugger(CondBreakDebugger):
    def interaction_loop(self) -> None:
        """Interact with the user"""
        self.print_debugger_status(self.frame, self.event, self.arg)  # type: ignore

        self.interact = True
        while self.interact:
            command = input("(debugger) ")
            self.execute(command)  # type: ignore

class CondBreakDebugger(CondBreakDebugger):
    def attr_command(self, arg: str = "") -> None:
        temp = str.split(',')
        OBJ = eval(temp[0].strip())
        VAR = temp[1].strip()
        EXPR = temp[2].strip()
        
        value = eval(EXPR, OBJ.__dict__)
        setattr(OBJ, VAR, value)
        print(f"Set {VAR} to {value} for object {OBJ}")

class CondBreakDebugger(CondBreakDebugger):
    def set_command(self, arg: str = "") -> None:
        token = arg.split('=')
        var = token[0].strip()
        value = token[1].strip()
        
        vars = self.local_vars
        try:
            vars[var] = eval(value, self.frame.f_globals, vars)
        except Exception as err:
            self.log(f"{err.__class__.__name__}: {err}")

class CondBreakDebugger(CondBreakDebugger):
    def break_command(self, arg: str = "") -> None:
        token = arg.split()
        if len(token) == 1:
            self.breakpoints.add(int(arg))
        elif len(token) == 3:
            var = token[0].strip()
            value = token[2].strip()
            self.breakvars[var] = eval(value, self.frame.f_globals, self.breakvars)

class CondBreakDebugger(CondBreakDebugger):
    def stop_here(self) -> bool:
        """Return True if we should stop"""
        if self.breakvars:
            for var, value in self.breakvars:
                if var in self.local_vars:
                    if self.breakvars[var] == value:
                        return True
        return self.stepping or self.frame.f_lineno in self.breakpoints
