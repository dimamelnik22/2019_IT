import numpy as np
import matplotlib.pyplot as plt


def pareto(n, m):
    X = np.random.random((n, m))
    pareto_opt = np.empty([0, m])
    not_opt = np.empty([0, m])
    for i in range(n):
        A = X[i]<=X
        dominance = np.sum(A.dot(np.ones([m, 1])) == m)
        if (dominance > 1):
            not_opt = np.vstack((not_opt, X[i]))
        else:
            pareto_opt = np.vstack((pareto_opt, X[i]))
    return (pareto_opt, not_opt)

def main():
    pareto_optimal, not_optimal = pareto(10,5)

    fig = plt.figure(figsize=[15, 15])
    ax = fig.add_subplot(212, projection="polar")
    ax.yaxis.grid(False)
    ax.set_yticks([])
    plt.thetagrids(np.arange(0, 360, 360.0/pareto_optimal[0].shape[0]), labels=np.arange(0, pareto_optimal[0].shape[0], 1))
    xax = np.arange(0, pareto_optimal[0].shape[0], 1)
    xax = np.append(xax, 0)
    xax = xax * 2 * 3.14 / pareto_optimal[0].shape[0]
    for x in not_optimal:  
        yax = np.append(x, x[0])
        ax.plot(xax, yax, color="red")
    for x in pareto_optimal:
        yax = np.append(x, x[0])
        ax.plot(xax, yax, color="green")
    
if __name__ == "__main__":
    main()