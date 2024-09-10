"""
border-radius
"""
import tkinter as tk


class MyFrame(tk.Frame):
    def __init__(self, master=None, corner_radius=60, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.corner_radius = corner_radius
        self.bg = "#CEFDFF"
        self._setupWidgets()

    def _setupWidgets(self):
        # 创建Canvas作为背景
        self.canvas = tk.Canvas(self, bg=self.bg, highlightthickness=0)
        self.canvas.place(x=0, y=0, relheight=1, relwidth=1)

        # 绑定事件以更新Canvas大小
        self.bind("<Configure>", self._updateCanvas)

    def _updateCanvas(self, event):
        self.canvas.delete("all")
        width, height = event.width, event.height
        self._drawRoundedRectangle(self.canvas, 0, 0, width, height, self.corner_radius)
        self._drawLine(self.canvas, width)

    def _drawRoundedRectangle(self, canvas, x1, y1, x2, y2, radius):
        points = [x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1,
                  x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2,
                  x2 - radius, y2, x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2,
                  x1, y2 - radius, x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1]
        canvas.create_polygon(points, fill=self.bg, outline='black', smooth=True)
        canvas.create_line(x2 - 1, radius / 3, x2 - 1, y2 - radius / 3)
        canvas.create_line(radius / 3, y2 - 1, x2 - radius / 3, y2 - 1)

    def _drawLine(self, canvas, width, height=40):
        canvas.create_line(0, height, width, height)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('test')
    root.state('zoomed')

    frame = MyFrame(root, width=200, height=100)
    frame.place(x=100, y=100)

    tk.Label(frame, text='Hello World!', bg='#CEFDFF').place(x=100, y=10)
    tk.Button(frame, text='Button', width=10).place(x=30, y=200)
    tk.Button(frame, text='A B C D', width=10).place(x=30, y=100)
    root.mainloop()
