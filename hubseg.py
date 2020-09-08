import paddlehub as hub
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

module = hub.Module(name="deeplabv3p_xception65_humanseg")
res = module.segmentation(paths = ["./test_mask_detection.jpg"], visualization=True, output_dir='humanseg_output')