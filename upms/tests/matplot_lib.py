import                      sys
import                      matplotlib
import                      matplotlib.pyplot as plt
import                      numpy as np

matplotlib.use('TkAgg')


class Diagram():
    def __init__(self):

        pass

    def data(self):
        y = np.array([35, 25, 25, 15])
        labels = ["apples", "bananas", "cherries", "dates"]

        plt.pie(y, labels=labels, startangle=90)
        plt.show()

        try:
            plt.savefig(sys.stdout.buffer)
            sys.stdout.flush()
        except:
            plt.savefig(sys.stderr.buffer)
            sys.stderr.flush()


if __name__ == "__main__":
    Diagram().data()
