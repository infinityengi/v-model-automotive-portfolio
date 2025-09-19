import tempfile
import os
import cv2
from code.perception import run_pipeline as rp

def create_blank_image(path, name="frame1.png", w=320, h=240):
    img = 255 * ( (0*0) + 1 )  # white
    import numpy as np
    blank = (255 * np.ones((h, w, 3))).astype('uint8')
    cv2.imwrite(os.path.join(path, name), blank)

def test_run_pipeline_creates_output(tmp_path):
    in_dir = tmp_path / "in"
    out_dir = tmp_path / "out"
    in_dir.mkdir()
    out_dir.mkdir()
    create_blank_image(str(in_dir))
    rp.run(str(in_dir), str(out_dir))
    # assert at least one file exists in output
    out_files = list(out_dir.iterdir())
    assert len(out_files) >= 1
