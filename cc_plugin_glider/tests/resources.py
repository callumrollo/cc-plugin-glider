#!/usr/bin/env python
"""
cc_plugin_glider/tests/resources.py
"""
import os
import subprocess

from pkg_resources import resource_filename


def get_filename(path):
    """
    Returns the path to a valid dataset
    """
    filename = resource_filename("cc_plugin_glider", path)
    nc_path = filename.replace(".cdl", ".nc")
    if not os.path.exists(nc_path):
        generate_dataset(filename, nc_path)
    return nc_path


def generate_dataset(cdl_path, nc_path):
    subprocess.call(["ncgen", "-o", nc_path, cdl_path])


STATIC_FILES = {
    "bad_metadata": get_filename("tests/data/bad_metadata.cdl"),
    "glider_std": get_filename("tests/data/IOOS_Glider_NetCDF_v2.0.cdl"),
    "glider_std3": get_filename("tests/data/IOOS_Glider_NetCDF_v3.0.cdl"),
    "bad_location": get_filename("tests/data/bad_location.cdl"),
    "bad_qc": get_filename("tests/data/bad_qc.cdl"),
    "no_qc": get_filename("tests/data/no_qc.cdl"),
    "bad_standard_name": get_filename("tests/data/bad_standard_name.cdl"),
    "bad_units": get_filename("tests/data/bad_units.cdl"),
}
