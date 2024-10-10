import pyclesperanto_prototype as cle  # version 0.24.4
import argparse
from pathlib import Path
from skimage.io import imread, imsave
import os


def cellpose_segmentation(path_file):

    basename = os.path.splitext(os.path.basename(path_file))[0]
    folder_path = os.path.dirname(path_file)
    image = imread(path_file)
    nuclei = image[:,1,:,:]
    image2_gb = cle.gaussian_blur(nuclei, None, 1.0, 1.0, 0.0)
    image3_vol = cle.voronoi_otsu_labeling(image2_gb, None, 9.0, 2.0)
    image4_cl = cle.closing_labels(image3_vol, None, 3.0)
    image5_eloe = cle.exclude_labels_on_edges(
    image4_cl, None, True, True, False, True, True, False)

    output_path = os.path.join(folder_path, basename+'_label.tif')
    imsave(output_path, image, imagej=True)#, resolution=(0.3, 0.1, 0.1))



def create_argparser_inference():
    parser = argparse.ArgumentParser()
    print(parser)
    parser.add_argument("--img_path", required=True, help="Path to image")
    return parser

if __name__ == "__main__":
    parser = create_argparser_inference()
    print(parser)
    cli_args = parser.parse_args()
    
    path_file = cli_args.img_path  
    if not Path(path_file).is_file():
        raise FileNotFoundError(f"Image not found: {path_file}")
    cellpose_segmentation(path_file)
