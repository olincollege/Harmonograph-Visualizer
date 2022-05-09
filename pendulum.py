"""
Pendulum Implementation
"""

import random
import numpy as np
import matplotlib.pyplot as plt

class Pendulum:
    """
    Attributes:
    """

    def __init__(self):
        """
        Creates a new pendulum
        """
        self.cycles = 80
        num_samples = 80000
        self.damping_constant = .015
        self.amplitude = 1
        self.frequency = 1
        self.phase = 0
        self.amplitude = 1
        self.pendulum_array = np.linspace(0, self.cycles*np.pi, num_samples)
        self.pendulum = np.sin(self.pendulum_array)


    def update_pendulum(self):
        """
        updates the pendulum instance to incoporate changes to the frequency
        phase and amplitude atributes.  Also randomizes the phase and amplitude
        so that each run will be slightly different.
        """
        #shifts phase between 0 and pi
        self.phase = random.uniform(0, np.pi)

        #sets inicial amplitude between .8 and 1
        self.amplitude = random.uniform(.8, 1)

        #incorporates a small frequency variation to more accuratly model a
        #real system.  It is plus or minus half a percent of the frequency given
        frequency_variation = random.uniform(
            (-self.frequency/200),(self.frequency/200)
            )
        self.frequency = self.frequency + frequency_variation

        #the main equation for setting up each pendulums motion.  The motion is
        #approximated as a simple damped sine wave.
        self.pendulum = (
            self.amplitude * np.exp(-self.pendulum_array*self.damping_constant)
            *np.sin(self.pendulum_array*self.frequency/self.cycles + self.phase)
        )

    def friction_off(self):
        """
        turns friction off in the model by setting the damping constant to 0
        """
        self.damping_constant = 0

    def draw_1pendulum(self, filename):
        """
        Used to visualize the motion of a single pendulum in order to make sure
        that the damping is working as expected. Saves the resulting plot as a
        JPG with the name filename

        args:
            filename: str, the name that the user wants the file to be saved as
        """
        plt.figure(figsize= (20, 20), frameon=False)
        plt.title("Amplitude over Time of a Single Pendulum", fontsize = 50)
    
        plt.xlabel("Time", fontsize = 30)
        plt.ylabel("Amplitude", fontsize = 30)


        plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

        self.update_pendulum()
        plt.plot(self.pendulum)
        plt.savefig(f"{str(filename)}.jpg")

    def read(self):
        """
        This could likely be avvoided, but I needed a method to return just the
        numpy array of the pendulum and not the class instance.
        """
        return self.pendulum
