import rasterio
import matplotlib.pyplot as plt
import numpy as np

with rasterio.open("NDVI_small_area.tif") as src:
    ndvi = src.read(1)

plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI")
plt.title("NDVI - Sentinel-2")
plt.show()
plt.savefig("ndvi.png", dpi=300)

