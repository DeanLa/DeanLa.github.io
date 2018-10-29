import matplotlib.pyplot as plt
import os

'''Library for charting.'''
PACKAGE_DIR = os.path.dirname(__file__)


def set_blog_style():
    '''
    Set styling for charts
    '''

    style_path = os.path.join(PACKAGE_DIR, 'blog.style')
    plt.style.use(['classic', 'ggplot', 'seaborn-poster', style_path])
