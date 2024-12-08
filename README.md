# Cell_Stitching
2D image stitching codes for microscopy images. A quick method and Python implementation for imaging stitching with an iterative method for pairwise stitching of the Fiji (Image2) plugin.  It is especially useful for microscopy images. Adapted from https://github.com/imagej/pyimagej/issues/119. The original algorithm proposed by [Preibisch, Bioinformatics, 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2682522/).
## Quick start
The only dependency is [PyImageJ](https://github.com/imagej/pyimagej). OpenJDK and Maven are required. Please follow their [instructions](https://github.com/imagej/pyimagej?tab=readme-ov-file#installation) for installation. Then you're ready to go! The [tutorials](https://py.imagej.net/en/latest/) are also good resources for Python implementations of the Fiji plugins. Theoretically all the micros and plugins in ImageJ2 can be implemented with PyImageJ.
## Why this repo?
I'm working on cell imaging and my data has plenty of overlappings that the grid stitching plugin embedded in the ImageJ is not working (terrible actually). The pairwise stitching works well but mannal stitching is time-consuming. Many public repositories like [OpenStitching](https://github.com/OpenStitching/stitching) for images stitching works well for the images with sufficient features, unfortunately my datas with sparse cells are not that kind.
## Examples
Release soon.
