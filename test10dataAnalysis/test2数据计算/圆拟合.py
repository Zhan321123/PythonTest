import matplotlib
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
from math import sqrt, pi
matplotlib.use('TkAgg')

def calc_R(x, y, xc, yc):
    """
    calculate the distance of each 2D points from the center (xc, yc)
    """
    return np.sqrt((x - xc) ** 2 + (y - yc) ** 2)


def f(c, x, y):
    """
    calculate the algebraic distance between the data points
    and the mean circle centered at c=(xc, yc)
    """
    Ri = calc_R(x, y, *c)
    return Ri - Ri.mean()


def sigma(coords, x, y, r):
    """Computes Sigma for circle fit."""
    dx, dy, sum_ = 0., 0., 0.

    for i in range(len(coords)):
        dx = coords[i][1] - x
        dy = coords[i][0] - y
        sum_ += (sqrt(dx * dx + dy * dy) - r) ** 2
    return sqrt(sum_ / len(coords))


def hyper_fit(coords, IterMax=99, verbose=False):
    """
    Fits coords to circle using hyperfit algorithm.
    Inputs:
        - coords, list or numpy array with len>2 of the form:
        [
    [x_coord, y_coord],
    ...,
    [x_coord, y_coord]
    ]
        or numpy array of shape (n, 2)
    Outputs:
        - xc : x-coordinate of solution center (float)
        - yc : y-coordinate of solution center (float)
        - R : Radius of solution (float)
        - residu : s, sigma - variance of data wrt solution (float)
    """
    if isinstance(coords, np.ndarray):
        X = coords[:, 0]
        Y = coords[:, 1]
    elif isinstance(coords, list):
        X = np.array([x[0] for x in coords])
        Y = np.array([x[1] for x in coords])
    else:
        raise Exception("Parameter 'coords' is an unsupported type: " + str(type(coords)))

    n = X.shape[0]

    Xi = X - X.mean()
    Yi = Y - Y.mean()
    Zi = Xi * Xi + Yi * Yi

    # compute moments
    Mxy = (Xi * Yi).sum() / n
    Mxx = (Xi * Xi).sum() / n
    Myy = (Yi * Yi).sum() / n
    Mxz = (Xi * Zi).sum() / n
    Myz = (Yi * Zi).sum() / n
    Mzz = (Zi * Zi).sum() / n

    # computing the coefficients of characteristic polynomial
    Mz = Mxx + Myy
    Cov_xy = Mxx * Myy - Mxy * Mxy
    Var_z = Mzz - Mz * Mz

    A2 = 4 * Cov_xy - 3 * Mz * Mz - Mzz
    A1 = Var_z * Mz + 4. * Cov_xy * Mz - Mxz * Mxz - Myz * Myz
    A0 = Mxz * (Mxz * Myy - Myz * Mxy) + Myz * (Myz * Mxx - Mxz * Mxy) - Var_z * Cov_xy
    A22 = A2 + A2

    # finding the root of the characteristic polynomial
    y = A0
    x = 0.
    for i in range(IterMax):
        Dy = A1 + x * (A22 + 16. * x * x)
        xnew = x - y / Dy
        if xnew == x or not np.isfinite(xnew):
            break
        ynew = A0 + xnew * (A1 + xnew * (A2 + 4. * xnew * xnew))
        if abs(ynew) >= abs(y):
            break
        x, y = xnew, ynew

    det = x * x - x * Mz + Cov_xy
    Xcenter = (Mxz * (Myy - x) - Myz * Mxy) / det / 2.
    Ycenter = (Myz * (Mxx - x) - Mxz * Mxy) / det / 2.

    x = Xcenter + X.mean()
    y = Ycenter + Y.mean()
    r = sqrt(abs(Xcenter ** 2 + Ycenter ** 2 + Mz))
    s = sigma(coords, x, y, r)
    iter_ = i
    if verbose:
        print('Regression complete in {} iterations.'.format(iter_))
        print('Sigma computed: ', s)
    return x, y, r, s


def least_squares_circle(coords):
    """
    Circle fit using least-squares solver.
    Inputs:
        - coords, list or numpy array with len>2 of the form:
        [
    [x_coord, y_coord],
    ...,
    [x_coord, y_coord]
    ]
        or numpy array of shape (n, 2)
    Outputs:
        - xc : x-coordinate of solution center (float)
        - yc : y-coordinate of solution center (float)
        - R : Radius of solution (float)
        - residu : MSE of solution against training data (float)
    """

    x, y = None, None
    if isinstance(coords, np.ndarray):
        x = coords[:, 0]
        y = coords[:, 1]
    elif isinstance(coords, list):
        x = np.array([point[0] for point in coords])
        y = np.array([point[1] for point in coords])
    else:
        raise Exception("Parameter 'coords' is an unsupported type: " + str(type(coords)))

    # coordinates of the barycenter
    x_m = np.mean(x)
    y_m = np.mean(y)
    center_estimate = x_m, y_m
    center, _ = optimize.leastsq(f, center_estimate, args=(x, y))
    xc, yc = center
    Ri = calc_R(x, y, *center)
    R = Ri.mean()
    residu = np.sum((Ri - R) ** 2)
    return xc, yc, R, residu


def plot_data_circle(x, y, xc, yc, R):
    """
    Plot data and a fitted circle.
    Inputs:
        x : data, x values (array)
        y : data, y values (array)
        xc : fit circle center (x-value) (float)
        yc : fit circle center (y-value) (float)
        R : fir circle radius (float)
    Output:
        None (generates matplotlib plot).
    """
    f = plt.figure(facecolor='white')
    plt.axis('equal')

    theta_fit = np.linspace(-pi, pi, 180)

    x_fit = xc + R * np.cos(theta_fit)
    y_fit = yc + R * np.sin(theta_fit)
    plt.plot(x_fit, y_fit, 'b-', label="fitted circle", lw=2)
    plt.plot([xc], [yc], 'bD', mec='y', mew=1)
    plt.xlabel('x')
    plt.ylabel('y')
    # plot data
    plt.scatter(x, y, c='red', label='data')

    plt.legend(loc='best', labelspacing=0.1)
    plt.grid()
    plt.title('Fit Circle')
    plt.show()


if __name__ == '__main__':
    data = [[0.0, 0.0], [0.048990249, 0.00176418], [0.09592396799999998, 0.006914879999999999],
            [0.14075000699999998, 0.01524258], [0.183422976, 0.02654208], [0.22390312499999998, 0.0406125],
            [0.26215622399999994, 0.05725727999999998], [0.29815344299999996, 0.07628418000000001],
            [0.331871232, 0.09750528000000001], [0.36329120100000006, 0.12073698000000001],
            [0.3924, 0.14580000000000004], [0.419189199, 0.17251938], [0.443655168, 0.20072447999999998],
            [0.465798957, 0.23024898000000002], [0.485626176, 0.26093088000000003],
            [0.5031468749999999, 0.29261249999999994], [0.5183754239999999, 0.32514047999999995],
            [0.5313303930000001, 0.35836578], [0.5420344320000002, 0.39214368000000005],
            [0.5505141510000001, 0.42633378000000005], [0.5568000000000003, 0.4608000000000002],
            [0.560926149, 0.49541058000000004], [0.5629303680000001, 0.53003808], [0.562853907, 0.56455938],
            [0.560741376, 0.5988556800000001], [0.556640625, 0.6328125], [0.550602624, 0.66631968],
            [0.5426813429999999, 0.6992713799999999], [0.532933632, 0.7315660800000001],
            [0.5214191009999999, 0.7631065799999999], [0.5081999999999999, 0.7937999999999998],
            [0.4933410989999999, 0.8235577799999998], [0.47690956799999984, 0.8522956799999999],
            [0.45897485699999985, 0.8799337799999998], [0.43960857599999986, 0.90639648],
            [0.41888437500000003, 0.9316124999999998], [0.39687782400000005, 0.9555148800000001],
            [0.37366629299999987, 0.9780409800000001], [0.349328832, 0.9991324800000001],
            [0.3239460509999999, 1.0187353799999999], [0.2976, 1.0368000000000002],
            [0.2703740490000003, 1.0532809800000003], [0.24235276800000013, 1.0681372800000002],
            [0.21362180700000014, 1.0813321800000002], [0.18426777600000005, 1.0928332800000002],
            [0.15437812500000006, 1.1026125000000002], [0.12404102400000012, 1.1106460800000004],
            [0.09334524300000002, 1.11691458], [0.062380032000000085, 1.12140288],
            [0.03123500100000004, 1.1241001800000001], [0.0, 1.125], [-0.031235001000000095, 1.1241001800000001],
            [-0.06238003200000006, 1.1214028799999998], [-0.093345243, 1.11691458], [-0.12404102400000006, 1.11064608],
            [-0.15437812500000014, 1.1026124999999998], [-0.1842677760000002, 1.09283328],
            [-0.2136218069999999, 1.08133218], [-0.2423527679999998, 1.06813728], [-0.27037404899999995, 1.05328098],
            [-0.2975999999999999, 1.0368000000000002], [-0.323946051, 1.01873538],
            [-0.3493288319999999, 0.9991324800000001], [-0.37366629300000004, 0.9780409800000001],
            [-0.39687782399999993, 0.95551488], [-0.4188843750000001, 0.9316125], [-0.439608576, 0.90639648],
            [-0.45897485700000007, 0.87993378], [-0.476909568, 0.8522956799999998],
            [-0.49334109899999995, 0.8235577800000002], [-0.5082, 0.7938000000000002],
            [-0.521419101, 0.7631065800000001], [-0.532933632, 0.7315660800000001],
            [-0.5426813429999999, 0.6992713799999999], [-0.5506026239999999, 0.66631968], [-0.556640625, 0.6328125],
            [-0.560741376, 0.59885568], [-0.5628539069999999, 0.5645593799999999], [-0.562930368, 0.53003808],
            [-0.5609261489999999, 0.4954105799999998], [-0.5568, 0.4607999999999999],
            [-0.5505141509999999, 0.4263337799999998], [-0.542034432, 0.3921436800000001],
            [-0.5313303930000001, 0.3583657800000002], [-0.518375424, 0.3251404800000002],
            [-0.503146875, 0.29261250000000005], [-0.485626176, 0.26093088000000003],
            [-0.46579895699999996, 0.23024898000000002], [-0.443655168, 0.20072447999999998],
            [-0.41918919899999996, 0.17251938], [-0.39239999999999997, 0.14579999999999996],
            [-0.3632912009999999, 0.12073697999999994], [-0.33187123199999985, 0.0975052799999999],
            [-0.29815344299999985, 0.07628417999999991], [-0.2621562240000002, 0.057257280000000105],
            [-0.2239031250000002, 0.04061250000000007], [-0.18342297600000015, 0.026542080000000044],
            [-0.14075000700000012, 0.015242580000000026], [-0.09592396800000008, 0.006914880000000012],
            [-0.04899024900000004, 0.0017641800000000032], [0.0, 0.0]]

    circle = hyper_fit(data)
    print(circle)

    circle = least_squares_circle(data)
    print(circle)

    plot_data_circle(*list(zip(*data)), circle[0], circle[1], circle[2])