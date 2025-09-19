"""
Simple controller skeleton for LKA demo.
"""

class Controller:
    def __init__(self, gain=1.0):
        self.gain = gain

    def compute_control(self, lateral_error_m):
        """
        Compute simple proportional control output (steering command).
        """
        # saturation example
        cmd = self.gain * lateral_error_m
        if cmd > 1.0:
            cmd = 1.0
        if cmd < -1.0:
            cmd = -1.0
        return cmd

if __name__ == "__main__":
    c = Controller(gain=0.5)
    print("control for 0.2m error:", c.compute_control(0.2))
