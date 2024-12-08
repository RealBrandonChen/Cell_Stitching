
'''
Georgia Tech
@Author Peng CHEN
Created on 12-07-2024
Stitch overlapped images with Fiji (Image2) plugin - Pairwise stitching. Especially useful for microscopy imaging.
Adapted from https://github.com/imagej/pyimagej/issues/119. Orignal algorithm proposed by Preibisch, Bioinformatics, 2009
v1.0: cells stitching for large field of view.
'''
import imagej
import scyjava as sj
import os

# The image tiles are stored in the target folder
parent_dir = str(os.getcwd()) + '\PathTo\yourImageFolder'

# rename the images in the folder as sequences
def renameTiff(parent_dir):
    # print(parent_dir)
    image_count = 0
    os.chdir(parent_dir)
    for filename in os.listdir(parent_dir):
        os.rename(filename, "{}.tiff".format(image_count))
        image_count += 1
    return image_count

total_image_tiles = renameTiff(parent_dir)
print("Rename images finished, image stitching starts...")

# ///////////////////////////////////////////////////////////////////////// #
# start imagej, use without headless mode, can also use your local FiJi software
ij = imagej.init('sc.fiji:fiji:2.14.0', headless=False)

# get ConvertService and ImagePlus class
ConvertService = ij.get('org.scijava.convert.ConvertService')
ImagePlus = sj.jimport('ij.ImagePlus')

stitching_image_name = "paired_image.tiff"
# total_image_tiles = 400 # indicate the total images manually or from the counted number in the folder above
print("Current dir: " + str(os.getcwd()))

# total images for stitching, use for loop to iterate each image with pairwise stitching
for i in range(total_image_tiles-1):
    # open images
    if i == 0:
        img_temp_a = ij.io().open(os.path.join(parent_dir, '{}.tiff'.format(0)))
        img_temp_b = ij.io().open(os.path.join(parent_dir, '{}.tiff'.format(1)))
    else:
        img_temp_a = ij.io().open(os.path.join(parent_dir, stitching_image_name))
        img_temp_b = ij.io().open(os.path.join(parent_dir, '{}.tiff'.format(i+1)))
    # convert Img to ImagePlus
    imp_temp_a = ConvertService.convert(img_temp_a, ImagePlus)
    imp_temp_b = ConvertService.convert(img_temp_b, ImagePlus)

    # setup plugin args, may adjust here for your applications
    # plugin name
    plugin = "Pairwise stitching"
    stitching_image_name = "paired_image_{}.tiff".format(i)
    args = {"first_image":imp_temp_a,
            "second_image":imp_temp_b,
            "fusion_method":"[Linear Blending]",
            "fused_image": stitching_image_name,
            "check_peaks":5,
            "compute_overlap":True,
            "x":0.0000,
            "y":0.0000,
            "registration_channel_image_1":"[Average all channels]",
            "registration_channel_image_2":"[Average all channels]",
        }

    # now you can show and hide an image, here show image to perform as the window manager.
    # ImageJ1 <-> ImageJ2 synchronization has an issue that the older ImageJ1 plugins expect an open window/image
    # which in a headless mode doesn't exist. The PyImageJ is still working on this issue, as far to 12/07/2024, they still have it.
    # The following mehtod is a compromised way to stitch the images, while you will see the process generate the image and colse the windows continuouly.
    # If you have future modifications, please indicate it in the issues.:)
    imp_temp_a.show()
    imp_temp_a.getWindow().setVisible(False)
    imp_temp_b.show()
    imp_temp_b.getWindow().setVisible(False)

    # run plugin
    ij.py.run_plugin(plugin, args)

    # get stitched result, convert to Dataset and save
    stitched_imp= ij.py.active_image_plus()
    stitched_imp_python=ij.py.to_dataset(stitched_imp)
   
    ij.io().save(stitched_imp_python, os.path.join(parent_dir, stitching_image_name))

    # close all windows
    ij.py.window_manager().closeAllWindows()

print("Stitching finished! The stitched image was saved in your original folder.")