# ==========================================================
# 1. Configure Windows Conda environment (GDAL and PROJ)
# ==========================================================

import os
from pathlib import Path

prefix = os.environ.get("CONDA_PREFIX") or os.path.dirname(os.sys.executable)
lib = os.path.join(prefix, "Library")

os.environ["PATH"] = (
    os.path.join(lib, "bin") + os.pathsep + os.environ["PATH"]
)

os.environ["GDAL_DATA"] = os.path.join(lib, "share", "gdal")
os.environ["PROJ_LIB"] = os.path.join(lib, "share", "proj")

print("GDAL_DATA:", os.environ["GDAL_DATA"])
print("PROJ_LIB:", os.environ["PROJ_LIB"])


# ==========================================================
# 2. Import packages
# ==========================================================

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shapely
import fiona
import libpysal
import esda

print("\nAll required packages imported successfully.")


# ==========================================================
# 3. Define project directory and dataset
# ==========================================================

project_dir = Path(r"D:\Spatial Data Analysis")
data_path = project_dir / "efdi_wm_clean.gpkg"


# ==========================================================
# 4. Read the GeoPackage
# ==========================================================

food = gpd.read_file(
    data_path,
    engine="fiona"
)


# ==========================================================
# 5. Display dataset information
# ==========================================================

print("\nFirst five observations:")
display(food.head())

print("\nDataset dimensions:", food.shape)
print("Total observations:", len(food))

print("\nCoordinate Reference System:")
print(food.crs)

print("\nGeometry types:")
print(food.geom_type.value_counts())

print("\nMissing values:")
print(food.isna().sum())