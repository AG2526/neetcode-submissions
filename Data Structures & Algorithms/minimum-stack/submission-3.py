class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')  # keep a separate stack for running minimum 


    def push(self, val: int) -> None:
         if not self.stack : 
            self.stack.append(0) 
            self.min = val 
         else : 
            self.stack.append(val-self.min) 
            if val <self.min: 
                self.min = val 

    def pop(self) -> None:
         if not self.stack: 
            return 
         pop = self.stack.pop()
         if pop< 0 : 
            self.min = self.min - pop 
           

    def top(self) -> int:
        top = self.stack[-1]
        if top>0 : 
            return top+ self.min
        else: 
            return self.min


    def getMin(self) -> int:
        return self.min
# ---------------------------------------------------------------
# NOTES: one-stack MinStack (difference encoding)
# ---------------------------------------------------------------
# Each entry stores (val - min) instead of val, where min is the
# minimum BEFORE this push.
#
#   encoded >= 0  -> val is not a new min, min stays the same
#   encoded <  0  -> val IS a new min (negative = "min changed" flag)
#
# push(val): append val - min, then min = val if val < min
#            (first push: append 0 and set min = val)
#
# top():     encoded > 0  -> real value = encoded + min
#            encoded <= 0 -> real value = min
#
# pop():     if the popped entry is negative, restore the old min:
#                min = min - encoded
#            (because encoded = new_min - old_min)
#
# getMin():  return min
#
# Example: push(-2), push(0), push(-3)
#   stack = [0, 2, -1], min = -3
#   pop() -> -1 is negative -> min = -3 - (-1) = -2 (old min back)
# ---------------------------------------------------------------
        
