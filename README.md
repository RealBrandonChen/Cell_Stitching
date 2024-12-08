# Cell_Stitching
2D image stitching codes for microscopy images. A quick method and python implementation for imaging stitching with iterative method for pairwise stitching of the FiJi (Image2) plugin.  Especially useful for microscopy images. Adapted from https://github.com/imagej/pyimagej/issues/119. Orignal algorithm proposed by Preibisch, Bioinformatics, 2009.
## Quick start
The only dependency is [PyImageJ](https://github.com/imagej/pyimagej). OpenJDK and Maven are required. Please follow their [instructions](https://github.com/imagej/pyimagej?tab=readme-ov-file#installation) for installation.  Then you're ready to go! The [tutorials](https://py.imagej.net/en/latest/) are also good resources for python implementations of the Fiji plugins.
## Why this repo?
I'm working on cell imaging and my data has plenty of overlappings that the grid stitching plugin embedded in the ImageJ is not working (terrible actually). The pairwise stitching works well but mannal stitching is time-consuming. Many public repositories like [OpenStitching](https://github.com/OpenStitching/stitching) for images stitching works well for the images with sufficient features, unfortunately my data is not that kind.
## Examples
Coming soon.