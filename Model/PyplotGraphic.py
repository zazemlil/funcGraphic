import matplotlib.pyplot as plt
import matplotlib.pylab as plab 
from numpy import *

from Graphic import Graphic

class PyplotGraphic(Graphic):
    def __init__(self, window_title, graphic_title, xlabel, ylabel):
        super().__init__(window_title, graphic_title, xlabel, ylabel)
        self._x = linspace(-20, 20, 301)
        
    def draw(self):
        try:
            # clear previous figures
            plt.close()
            # creating graphic
            _, axes = plt.subplots()
            
            # adding graphs
            for item in self._funcs:
                y = self._exec_func(item)
                if isinstance(y, int):
                    y = [y for i in range(len(self._x))]
                
                axes.plot(self._x, y)

            # configure graphic
            self._configure_graphic(axes)
            # showing graphic
            plt.show()
        except Exception as error:
            print(f"{error=}, {type(error)=}")
                
    def _exec_func(self, item):
        x = self._x
        with errstate(divide='ignore', invalid='ignore'):
            exec(item)
        return locals()['y']

    def _configure_graphic(self, axes):
        fig = plab.gcf()
        fig.canvas.manager.set_window_title(self._window_title)

        axes.set_title(self._graphic_title, fontsize=15, fontname='Times New Roman')
        axes.set_xlabel(self._xlabel, color='gray')
        axes.set_ylabel(self._ylabel, color='gray')
        axes.grid(True)
        axes.legend(self._funcs)