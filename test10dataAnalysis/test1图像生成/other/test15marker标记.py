"""
matplotlib marker标记类型:
    {'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_down', '^': 'triangle_up', '<': 'triangle_left',
     '>': 'triangle_right', '1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right', '8': 'octagon',
     's': 'square', 'p': 'pentagon', '*': 'star', 'h': 'hexagon1', 'H': 'hexagon2', '+': 'plus', 'x': 'x',
     'D': 'diamond', 'd': 'thin_diamond', '|': 'vline', '_': 'hline', 'P': 'plus_filled', 'X': 'x_filled',
     0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup',
     7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase',
     'None': 'nothing', 'none': 'nothing', ' ': 'nothing', '': 'nothing'}

让标记为空心的方法，设置参数:
    markerfacecolor='none',
    markeredgecolor='r',
    markeredgewidth=1

"""
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
import matplotlib.lines as mlines


def emptyMarker(ax):
    """让标记为空心的方法"""
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], label='$y=x^2$', marker='*',
                  markerfacecolor='none',
                  markeredgecolor='r',
                  markeredgewidth=1)

def displayAllMarkers(ax):
    """展示所有标记"""
    x, y = 0, 0
    import matplotlib.lines as mlines # 所有标记类型
    ms = mlines.Line2D.markers
    for marker in ms:
        ax.plot(x, y, marker=marker)
        ax.text(x, y + 0.3, marker, ha='center', fontsize=8)
        x += 1
        if x > 8:
            x = 0
            y += 1

if __name__ == '__main__':
    print("所有标记类型:")
    print(mlines.Line2D.markers)

    fig, axs = plt.subplots(2, 2)
    emptyMarker(axs[0][0])
    displayAllMarkers(axs[0][1])

    plt.show()
