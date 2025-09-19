#!/usr/bin/env python3
"""
Minimal placeholder perception pipeline for LKA case-study.

Usage:
    python run_pipeline.py --input data/frames --output output/annotated
"""

import argparse
import os
import cv2

def process_frame(img):
    # Simple placeholder: draw a sample lane-ish overlay rectangle
    h, w = img.shape[:2]
    overlay = img.copy()
    # draw left and right lane markers (placeholder)
    cv2.line(overlay, (int(w*0.2), h), (int(w*0.45), int(h*0.5)), (0,255,0), 4)
    cv2.line(overlay, (int(w*0.8), h), (int(w*0.55), int(h*0.5)), (0,255,0), 4)
    # combine with alpha
    alpha = 0.7
    cv2.addWeighted(overlay, alpha, img, 1-alpha, 0, img)
    return img

def run(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    imgs = [f for f in os.listdir(input_dir) if f.lower().endswith((".png",".jpg",".jpeg"))]
    for i, name in enumerate(sorted(imgs)):
        src = os.path.join(input_dir, name)
        dst = os.path.join(output_dir, name)
        img = cv2.imread(src)
        if img is None:
            print(f"warning: cannot read {src}")
            continue
        annotated = process_frame(img)
        cv2.imwrite(dst, annotated)
    print(f"Processed {len(imgs)} frames -> {output_dir}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input directory with frames")
    parser.add_argument("--output", required=True, help="Output dir for annotated frames")
    args = parser.parse_args()
    run(args.input, args.output)

if __name__ == "__main__":
    main()
