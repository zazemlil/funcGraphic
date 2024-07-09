import matplotlib.pyplot as plt
import matplotlib.pylab as plab 
from numpy import *

from Model.Graphic import Graphic

class PyplotGraphic(Graphic):
    def __init__(self, window_title, graphic_title, xlabel, ylabel):
        super().__init__(window_title, graphic_title, xlabel, ylabel)
        self._x = linspace(-22, 22, 301)
        
    def draw(self) -> None:
        try:
            # clear previous figures
            plt.close()
            # creating graphic
            _, axes = plt.subplots()
            
            # adding graphs
            for item in self._funcs:
                y, x = self._exec_func(item)
                if x == "-":
                    if isinstance(y, int) or isinstance(y, float):
                        y = [y for i in range(len(self._x))]
                    axes.plot(self._x, y)
                else:
                    if isinstance(x, int) or isinstance(x, float):
                        x = [x for i in range(len(self._x))]
                    axes.plot(x, linspace(-50, 50, 301))

            # configure graphic
            self._configure_graphic(axes)
            # showing graphic
            plt.show()
        except Exception as error:
            #print(f"{error=}, {type(error)=}")
            self.notify(str(error) + "\nFunction: " + str(item))
                
    def _exec_func(self, item) -> list[dict, str] | list[str, dict]:
        x = self._x
        ldic = locals()
        with errstate(divide='ignore', invalid='ignore'):
            exec(item, globals(), ldic)
            if "y" in ldic:
                return ldic['y'], "-"
            else:
                return "-", ldic['x']

    def _configure_graphic(self, axes) -> None:
        fig = plab.gcf()
        fig.canvas.manager.set_window_title(self._window_title)

        axes.set_title(self._graphic_title, fontsize=15, fontname='Times New Roman')
        axes.set_xlabel(self._xlabel, color='gray')
        axes.set_ylabel(self._ylabel, color='gray')
        axes.grid(True)
        axes.legend(self._funcs)