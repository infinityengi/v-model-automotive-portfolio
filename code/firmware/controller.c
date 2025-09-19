// Minimal controller pseudocode - for demo only
#include <stdint.h>
#include <math.h>

float update_controller(float lateral_error, float gain) {
    // simple proportional controller
    return -gain * lateral_error;
}
