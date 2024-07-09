import matplotlib.pyplot as plt
import matplotlib.pylab as plab 
from numpy import *
import sympy as sp
from Model.Graphic import Graphic

class PyplotGraphic(Graphic):
    def __init__(self, window_title, graphic_title, xlabel, ylabel):
        super().__init__(window_title, graphic_title, xlabel, ylabel)
        self._x = linspace(-22, 22, 301)
        self._minX = -24
        self._maxX = 24
        self._freq = 301
        
    def draw(self) -> None:
        try:
            
            # clear previous figures
            plt.close()
            # creating graphic
            _, axes = plt.subplots()
            
            # adding graphs
            for item in self._funcs:
                # simplification of the function
                solved_item = self._solve_func(item)

                # execution of the function
                y, x = self._exec_func(solved_item)
                if solved_item[0] == 'y':
                    if isinstance(y, int) or isinstance(y, float):
                        y = [y for i in range(len(self._x))]
                    axes.plot(self._x, y)
                elif solved_item[0] == 'x':
                    if isinstance(x, int) or isinstance(x, float):
                        x = [x for i in range(len(self._x))]
                    axes.plot(x, self._x)

            # configure and show graphic 
            self._configure_graphic(axes)

            plt.show()
        except Exception as error:
            self.notify({"error": str(error), "func": str(item), "index": self._funcs.index(item)})
                
    def _solve_func(self, item) -> str:
        x, y = sp.symbols('x y')
        item_half_1, item_half_2 = item[ : item.find("=")], item[item.find("=") + 1 : ]
        
        availableFunctions = {
                            "x": x, "y": y, "pi": sp.pi, "e": sp.E, "sqrt": sp.sqrt, "abs": sp.Abs,
                            "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "exp": sp.exp, "log": sp.log,
                            "sinh": sp.sinh, "cosh": sp.cosh, "tanh": sp.tanh,
                            "arcsin": sp.asin, "arccos": sp.acos, "arctan": sp.atan, "asin": sp.asin, "acos": sp.acos, "atan": sp.atan,
                            "arcsinh": sp.asinh, "arccosh": sp.acosh, "arctanh": sp.atanh, "asinh": sp.asinh, "acosh": sp.acosh, "atanh": sp.atanh
                            }
        equation = sp.Eq(eval(item_half_1, availableFunctions), eval(item_half_2, availableFunctions))
        
        if item.count('y') > 0:
            solution = sp.solve(equation, y)
            if solution == []:
                solution = sp.solve(equation, x)
                solution = str(solution[0]).replace(" ", "")
                return "x="+solution
            print(solution) # сделать возвращения нескольких значений
            solution = str(solution[0]).replace(" ", "").lower()
            return "y="+solution
        elif item.count('x') > 0:
            solution = sp.solve(equation, x)
            solution = str(solution[0]).replace(" ", "").lower()
            return "x="+solution

    def _exec_func(self, item) -> list[dict, None] | list[None, dict]:
        if item[0] == 'y':
            x = self._x
            ldic = locals()
            with errstate(divide='ignore', invalid='ignore'):
                exec(item, globals(), ldic)
                print(ldic["y"]) # -----------------------------------------------------------
                print(self._x) # -----------------------------------------------------------
                return ldic['y'], None
        elif item[0] == 'x':
            y = self._x
            ldic = locals()
            with errstate(divide='ignore', invalid='ignore'):
                exec(item, globals(), ldic)
                return None, ldic['x']

    def _configure_graphic(self, axes) -> None:
        fig = plab.gcf()
        fig.canvas.manager.set_window_title(self._window_title)

        axes.set_title(self._graphic_title, fontsize=15, fontname='Times New Roman')
        axes.set_xlabel(self._xlabel, color='gray')
        axes.set_ylabel(self._ylabel, color='gray')
        axes.grid(True)
        axes.legend(self._funcs)

    def set_minX(self, minX: int) -> None:
        self._minX = minX

    def set_maxX(self, maxX: int) -> None:
        self._maxX = maxX

    def set_freq(self, freq: int) -> None:
        self._freq = freq

    def set_x(self) -> None:
        self._x = linspace(int(self._minX), int(self._maxX), int(self._freq))