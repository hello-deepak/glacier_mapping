#!/usr/bin/env python
"""
Utilities for Managing VRTs

2020-05-05 18:11:08
"""
import numpy as np
import argparse
import pandas as pd
import fiona
import shapely.geometry
import pathlib
from osgeo import gdal
import rasterio
from PIL import Image
import tempfile

def reproject_directory(input_dir, output_dir, crs_string="EPSG:4326"):
    inputs = pathlib.Path(input_dir).glob("*.tif")
    for im in inputs:
        print(f"reprojecting {str(im)}")
        gdal.Warp(pathlib.Path(output_dir, s.stem), s, dstSRS=crs_string)


def vrt_from_dir(input_dir, output_path="./output.vrt", **kwargs):
    inputs = list(pathlib.Path(input_dir).glob("*.tif"))
    vrt_opts = gdal.BuildVRTOptions(**kwargs)
    print(inputs)
    gdal.BuildVRT(output_path, inputs, options=vrt_opts)


def tiles(input_file, output_dir, zoom_levels="15-17"):
    gdal2tiles.generate_tiles(input_file, output_dir, zoom="15-17")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge to a VRT")
    parser.add_argument("-d", "--input_dir", type=str, default="../../data_glaciers/")
    parser.add_argument("-o", "--output_dir", type=str, default="./")
    parser.add_argument("-n", "--name", type=str, default="output.vrt")
    parser.add_argument("-t", "--tile", default=False)
    args = parser.parse_args()

    tmp = tempfile.mkdtemp()
    reproject_directory(args.input_dir, tmp)
    vrt_path = pathlib.Path(args.output_dir, args.name)
    vrt_from_dir(tmp, vrt_path)

    if args.tile:
        tiles(vrt_path, args.output_dir)
