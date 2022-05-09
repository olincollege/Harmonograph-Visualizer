"""
Harmonograph View
"""
import matplotlib.pyplot as plt


class HarmonographView():
    """
    Plot of the harmonograph
    """
    def __init__(self, pendulum1x, pendulum2x, pendulum1y, pendulum2y):
        """
        Creates the 4 pendulums to be used for the visualization.

        Args:
            pendulum1X: class instance representing the first pendulum in the X
            dimension.

            pendulum2X: class instance representing the secound pendulum in the
            X dimension.

            pendulum1Y: class instance representing the first pendulum in the Y
            dimension.

            pendulum2Y: class instance representing the secound pendulum in the
            X dimension.

        """
        self.pendulum1x = pendulum1x
        self.pendulum2x = pendulum2x
        self.pendulum1y = pendulum1y
        self.pendulum2y = pendulum2y

    def update_all_pendulums(self):
        """
        Updates the pendulums by calling the update pendulum method.  This is
        done before plotting
        """

        self.pendulum1x.update_pendulum()
        self.pendulum2x.update_pendulum()
        self.pendulum1y.update_pendulum()
        self.pendulum2y.update_pendulum()

    def draw(self, filename):
        """
        Display a representation of the harmonograph drawing. Updates pendulums,
        and then plots and saves as an svg

        args:
            filename: str, the name that the user wants the file to be saved as
        """
        self.update_all_pendulums() #updates all pendulums


        plt.figure(figsize= (15, 15), frameon=False)
        plt.title("Randomly Seeded Harmonograph Drawing with Selected \
            Frequencies")
        labels = f"Choosen Frequencies: "\
            f"Pendulum_X1={round(self.pendulum1x.frequency, 2)}  "\
            f"Pendulum_X2={round(self.pendulum2x.frequency, 2)}  "\
            f"Pendulum_Y1={round(self.pendulum1y.frequency, 2)}  "\
            f"Pendulum_Y2={round(self.pendulum2y.frequency, 2)}"
        plt.xlabel(labels, fontsize = 10)


        plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)


        plt.plot(
            (self.pendulum1x.read() + self.pendulum2x.read()),
            (self.pendulum1y.read() + self.pendulum2y.read()), color = "k"
        )
        plt.savefig(f"{str(filename)}.svg")
