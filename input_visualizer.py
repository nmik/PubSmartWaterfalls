import argparse
import numpy as np
import matplotlib.pyplot as plt
from utils import load_grb_images_from_list, WATERFALL_DICT

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--datafolder", type=str, required=True,
                    help = "Path to folder with the .npy files")
parser.add_argument("-s", "--save_figs", type=bool, required = False, default= False,
	                help='Save the comparison reconstructed-true images')
args = parser.parse_args()


GRB_LIST = [
            # 'GRB170817529', # GW-GRB NSNS
            # 'GRB200415367', 
            # 'GRB180128215',  # MGFs 'GRB231115A' (not in ht esample)
            # 'GRB221009553', # Collapsar (The BOAT)
            # 'GRB200826187', # shortest collapsar
            'GRB230307656', 
            # 'GRB211211549', #long mergers
            ]
GRB_TAGS = [
            # 'GRB 170817A', # GW-GRB NSNS
            # 'GRB 200415A', # MGFs 
            # 'GRB 180128A', # MGFs 
            # 'GRB 221009A', # Collapsar (The BOAT)
            # 'GRB 200826A', # shortest collapsar
            'GRB 230307A', #long mergers
            # 'GRB 211211A' #long mergers
            ]


def visualize_input(file_folder_path, grb_list, save=False, show=False):
    """
    Plot a given GRB*.npy file.
    
    Parameters
    ----------
    npy_file : str
          .npy files containing the 12 imaages of the GRB waterfalls.
    tobeopen: bool
          if False, assume that the npy file is already open (the input is the 
                 set of images)
          
    """
    name_grb, grb = load_grb_images_from_list(file_folder_path, grb_list)

    for i, g in enumerate(grb):

        fig, axs = plt.subplots(3, 4, figsize=(14,7), )
        # fig.suptitle(GRB_TAGS[i], fontsize="x-large")
        # plt.title(name_grb[i])
        

        VMIN, VMAX = np.min(g), np.max(g)

        ax1 = axs[0, 0].imshow(g[0], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Long_hard']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[0, 0].set_title(WATERFALL_DICT['Long_hard']['title'])
        ax2 = axs[0, 1].imshow(g[1], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Long_norm']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[0, 1].set_title(WATERFALL_DICT['Long_norm']['title'])
        ax3 = axs[0, 2].imshow(g[2], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Long_soft']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[0, 2].set_title( WATERFALL_DICT['Long_soft']['title'])
        ax4 = axs[0, 3].imshow(g[3], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Long_blackbody']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[0, 3].set_title( WATERFALL_DICT['Long_blackbody']['title'])
        # plt.colorbar(ax1)
        # plt.colorbar(ax2)
        # plt.colorbar(ax3)
        # plt.colorbar(ax4)
        axs[0,0].set_xlabel('Time around trigger', size=12)
        axs[0,1].set_xlabel('Time around trigger', size=12)
        axs[0,2].set_xlabel('Time around trigger', size=12)
        axs[0,3].set_xlabel('Time around trigger', size=12)
        axs[0,0].set_ylabel('Timescale', size=12)
        axs[0,1].set_ylabel('Timescale', size=12)
        axs[0,2].set_ylabel('Timescale', size=12)
        axs[0,3].set_ylabel('Timescale', size=12)
        axs[0,0].annotate('32.768 s', xy=(7100, 0.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('16.384 s', xy=(7100, 1.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('8.192 s', xy=(7500, 2.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('4.096 s', xy=(7500, 3.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('2.048 s', xy=(7500, 4.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('1.024 s', xy=(7500, 5.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('0.512 s', xy=(7500, 6.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('0.256 s', xy=(7500, 7.2), xycoords='data', fontsize=9)
        axs[0,0].annotate('(8 x 9376)', xy=(100, 7.2), xycoords='data', fontsize=12)

        g_med = g[:, :, :7500]
        g_med = g[:, :3, :]
        ax5 = axs[1, 0].imshow(g_med[4], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Med_hard']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[1, 0].set_title( WATERFALL_DICT['Med_hard']['title'])
        ax6 = axs[1, 1].imshow(g_med[5], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Med_norm']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[1, 1].set_title( WATERFALL_DICT['Med_norm']['title'])
        ax7 = axs[1, 2].imshow(g_med[6], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Med_soft']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[1, 2].set_title( WATERFALL_DICT['Med_soft']['title'])
        ax8 = axs[1, 3].imshow(g_med[7], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Med_blackbody']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[1, 3].set_title( WATERFALL_DICT['Med_blackbody']['title'])


        # plt.colorbar(ax5)
        # plt.colorbar(ax6)
        # plt.colorbar(ax7)
        # plt.colorbar(ax8)
        axs[1,0].set_xlabel('Time around trigger', size=12)
        axs[1,1].set_xlabel('Time around trigger', size=12)
        axs[1,2].set_xlabel('Time around trigger', size=12)
        axs[1,3].set_xlabel('Time around trigger', size=12)
        axs[1,0].set_ylabel('Timescale', size=12)
        axs[1,1].set_ylabel('Timescale', size=12)
        axs[1,2].set_ylabel('Timescale', size=12)
        axs[1,3].set_ylabel('Timescale', size=12)
        axs[1,0].annotate('0.128 s', xy=(7500, 0.2), xycoords='data', fontsize=9)
        axs[1,0].annotate('0.064 s', xy=(7500, 1.2), xycoords='data', fontsize=9)
        axs[1,0].annotate('0.032 s', xy=(7500, 2.2), xycoords='data', fontsize=9)
        axs[1,0].annotate('(3 x 7500)', xy=(100, 2.4), xycoords='data', fontsize=12)


        g_short = g[:, :, :6000]
        g_short = g[:, :4, :]
        ax9 = axs[2, 0].imshow(g_short[8], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Short_hard']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[2, 0].set_title( WATERFALL_DICT['Short_hard']['title'])
        ax10 = axs[2, 1].imshow(g_short[9], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Short_norm']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[2, 1].set_title( WATERFALL_DICT['Short_norm']['title'])
        ax11 = axs[2, 2].imshow(g_short[10], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Short_soft']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[2, 2].set_title( WATERFALL_DICT['Short_soft']['title'])
        ax12 = axs[2, 3].imshow(g_short[11], origin='upper', aspect='auto', cmap=WATERFALL_DICT['Short_blackbody']['cmap'],
                                vmin=VMIN, vmax=VMAX)
        axs[2, 3].set_title( WATERFALL_DICT['Short_blackbody']['title'])
        # plt.colorbar(ax9)
        # plt.colorbar(ax10)
        # plt.colorbar(ax11)
        # plt.colorbar(ax12)
        axs[2,0].set_xlabel('Time around trigger', size=12)
        axs[2,1].set_xlabel('Time around trigger', size=12)
        axs[2,2].set_xlabel('Time around trigger', size=12)
        axs[2,3].set_xlabel('Time around trigger', size=12)
        axs[2,0].set_ylabel('Timescale', size=12)
        axs[2,1].set_ylabel('Timescale', size=12)
        axs[2,2].set_ylabel('Timescale', size=12)
        axs[2,3].set_ylabel('Timescale', size=12)
        axs[2,0].annotate('0.016 s', xy=(7500, 0.2), xycoords='data', fontsize=9)
        axs[2,0].annotate('0.008 s', xy=(7500, 1.2), xycoords='data', fontsize=9)
        axs[2,0].annotate('0.004 s', xy=(7500, 2.2), xycoords='data', fontsize=9)
        axs[2,0].annotate('0.002 s', xy=(7500, 3.2), xycoords='data', fontsize=9)
        axs[2,0].annotate('(3 x 6000)', xy=(100, 3.4), xycoords='data', fontsize=12)

        

        plt.subplots_adjust(hspace=0.3)
        plt.subplots_adjust(wspace=0.2)

        plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[]);
        plt.tight_layout()
        if save:
            plt.savefig('figs/%s_input.png'%(name_grb[i]), dpi=200)

        if show:
            plt.show()
    return 0

file_folder_path = args.datafolder
save_figs=args.save_figs

name_list, dataset = load_grb_images_from_list(file_folder_path, GRB_LIST)
print('Number of GRB in our sample', name_list.shape)



visualize_input(file_folder_path, GRB_LIST, save=args.save_figs, show=True)