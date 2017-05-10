import numpy as np
from scipy.misc import comb


class kurve():
    def bernstein_poly(self,i, n, t):        #The Bernstein polynomial of n, i as a function of t
        return comb(n, i) * (t ** (n - i)) * (1 - t) ** i

    def bezier_curve(self, points, nTimes=1000):
        """
           Given a set of control points, return the
           bezier curve defined by the control points.

           * points should be a list of lists, or list of tuples
            such as [ [1,1],
                     [2,3],
                     [4,5], ..[Xn, Yn] ]
            * nTimes is the number of time steps, defaults to 1000
        """
        nPoints = len(points)
        xPoints = np.array([p[0] for p in points])
        yPoints = np.array([p[1] for p in points])

        t = np.linspace(0.0, 1.0, nTimes)

        polynomial_array = np.array([self.bernstein_poly(self=self,i=i, n=(nPoints - 1), t=t) for i in range(nPoints)])

        xvals = np.dot(xPoints, polynomial_array)
        yvals = np.dot(yPoints, polynomial_array)

        return xvals, yvals

    def Length(self,x, y):   #return the length of curve
        """
            length = np.zeros(len(x-1))
            for i in (range(len(x) - 1)):
                length[i] = (((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 )
                print(length[i])
        """
        return sum(((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 for i in (range(len(x) - 1)))

if __name__ == "__main__":
    from matplotlib import pyplot as plt

    Kurve = kurve
    nPoints = 3
    ##points = [[0, 0],[0,4],[1,5],[5 ,5]]#np.random.rand(nPoints,2)*200
    points = np.random.rand(nPoints,2)*200
    xpoints = [p[0] for p in points]
    ypoints = [p[1] for p in points]

    xvals, yvals = Kurve.bezier_curve(self = Kurve,points=points)
    plt.plot(xvals, yvals)
    plt.plot(xpoints, ypoints, "ro")
    for nr in range(len(points)):
        plt.text(points[nr][0], points[nr][1], nr)

    plt.show()
    print(Kurve.Length(self = Kurve,x=xvals,y=yvals))

