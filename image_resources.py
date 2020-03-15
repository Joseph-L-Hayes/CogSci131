import numpy as np
import random
import matplotlib.pyplot as plt
import time

interpol_methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

color_maps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

#Good ones: 4, 3 best for this assignment
#Good cmaps (in order best to worst): 'inferno', 'plasma', 'seismic_r' (very clear), 'gist_heat', 'Accent', 'gist_stern' (interesting), 'brg'
#cmaps cont: 'afmhot', 'magma'

# def live_update_demo():
#
#     plt.subplot(2, 1, 1)
#     h1 = plt.imshow(np.random.randn(30, 30))
#     redraw_figure()
#     # plt.subplot(2, 1, 2)
#     # h2, = plt.plot(np.random.randn(50))
#     # redraw_figure()
#
#     t_start = time.time()
#     for i in range(1000):
#         h1.set_data(np.random.randn(30, 30))
#         redraw_figure()
#         # h2.set_ydata(np.random.randn(50))
#         # redraw_figure()
#         print('Mean Frame Rate: %.3gFPS' % ((i+1) / (time.time() - t_start)))
#
# def redraw_figure():
#     plt.draw()
#     plt.pause(0.00001)
#
# live_update_demo()



#scrap:
            # label = self.get_label()
            # data = self.data_set[label] #this should give data for 0 or 1, then random into that
            #if the data is label 1 and we get 0 as output, that means it was incorrect
            #if data is label 0 and we get 1 as output, weights incorrect
            # sub_data = random.choice(data) #this should be one of the (784,) arrays
            # print("intended :", intended)
            # print("label: ", label)
            # print("sub_data: ", sub_data.shape)

    # def buildData(self, *args):
    #     """Takes in a list of data sets and returns a dictionary with keys as labels for the data sets.
    #         The key labels are generated based on index in args, so they must be input in the correct order.
    #         For example: data set for 0 images must be first arg in args, 1 images must be next"""
    #     data = dict()
    #     for k in range(len(args)):
    #         data[k] = args[k]
    #     return data
