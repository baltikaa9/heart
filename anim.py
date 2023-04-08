from matplotlib.animation import FuncAnimation

from mathematics import InputParameters, f


class Animation:
    def __init__(self, fig):
        self.fig = fig
        self.params = InputParameters(100, 0.1)
        self.ax = self.fig.add_subplot()
        self.ax.set(facecolor='#181a1b')
        self.line, = self.draw(self.params.x, self.params.y, color='#dc7a77')
        self.animation = FuncAnimation(
            self.fig,
            func=self.update,
            frames=self.params.range,
            # fargs=(self.line, x),
            interval=10,
            blit=True,
            repeat=True
        )
        # self.animation.save('heart.mp4', writer='ffmpeg', fps=30)

    def draw(self, x: list, y: list, **kwargs):
        return self.ax.plot(x, y, **kwargs)

    def update(self, n):
        self.line.set_ydata([f(x, n) for x in self.params.x])
        return [self.line]

    def restart(self, n, speed):
        self.animation._stop()
        self.params = InputParameters(n, speed)
        self.animation = FuncAnimation(
            self.fig,
            func=self.update,
            frames=self.params.range,
            # fargs=(self.line, x),
            interval=10,
            blit=True,
            repeat=True
        )

    def pause(self):
        self.animation.pause()

    def resume(self):
        self.animation.resume()
