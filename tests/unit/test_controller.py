# Simple functional check (no C binding): duplicate logic in python for CI demo
def update_controller(lateral_error, gain):
    return -gain * lateral_error

def test_controller_response():
    out = update_controller(0.2, 1.5)
    assert abs(out + 0.3) < 1e-6
