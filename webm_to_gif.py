import argparse
import cv2
import imageio
import numpy as np


def convert_webm_to_gif(input_file, output_file):
    video_capture = cv2.VideoCapture(input_file)
    still_reading, image = video_capture.read()
    frame_count = 0
    images = []
    while still_reading:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        images.append(image)
        still_reading, image = video_capture.read()
        frame_count += 1
    imageio.mimsave(
        output_file,
        [np.array(img) for i, img in enumerate(images) if i % 2 == 0],
        duration=0.1,
        loop=0x7FFF * 2 + 1,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert WebM to GIF")
    parser.add_argument("-i", "--input", type=str, help="Input WebM file")
    parser.add_argument("-o", "--output", type=str, help="Output GIF file")
    args = parser.parse_args()

    if not args.input:
        parser.error("Please specify the input file using the -i or --input flag.")
    if not args.output:
        parser.error("Please specify the output file using the -o or --output flag.")

    convert_webm_to_gif(args.input, args.output)
