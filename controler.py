"""
Controler Class for user imput
"""
class TextController():
    """
    requests user input to inicialize harmonograph
    """

    def input(self):
        """
        user inputs either one of the specified notes that maps to a frequency,
        or they directly enter a frequency and the frequency entered is
        returned.  If the user attempt and invalid imput, they are propted to
        try again.
        """
        notes = {
            "C":261.63, "Cs":277.18, "D":293.66, "Ds":311.13, "E":329.63,
            "F":349.23, "Fs":369.99, "G":392, "Gs":415.3, "A":440, "As":466.16,
            "B":493.88
        }
        note = input(
                f"What note would you like to set the pendulum to: " \
                f"Choose(C, Cs, D, Ds, E, F, Fs, G, Gs, A, As, B) " \
                f"or a custom number for frequency"
            )
        try:
            if note in [
                "C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"
                ]:
                frequncy = notes[note]
                print(f"Chosen Frequency: {frequncy}")
                return frequncy

            if float(note):
                frequncy = float(note)
                print(frequncy, "Frequency")
                return frequncy

            raise ValueError

        except (ValueError, IndexError):
            print("Invalid Entry, Try Again")
            return self.input()
