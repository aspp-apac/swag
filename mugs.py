import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import itertools
import pandas as pd
from skimage import io
 
names = list(pd.read_csv('survey.csv')['Mug'])

template = io.imread('mug-aspp-01.png')
mug_size = (19.3/2.54, 7.9/2.54)
 
for name in names:
    this_code = itertools.dropwhile(
        lambda s: 'this_code' not in s,
        open(__file__))
    code_str = str.join('', this_code)
    fig = plt.Figure(figsize=mug_size)
    canvas = FigureCanvas(fig)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(template)
    ax.text(1250, 50, code_str,
            fontname='Andale Mono',
            fontsize=9,
            horizontalalignment='left',
            verticalalignment='top')
    ax.text(580, 170, f'{name}',
            fontname='Arial',
            fontstyle='italic',
            fontsize=28,
            horizontalalignment='center',
            verticalalignment='baseline')
    ax.set_axis_off()
    fig.savefig(f'mug-{name}.png', dpi=300)
