
import numpy as np

from _load import load_solution

correlation = load_solution("math-expectation-variance-covariance").correlation


def correlation_matrix(x: np.ndarray) -> np.ndarray:
    """
    x is (num_samples, num_features). Returns a (num_features,
    num_features) matrix where entry [i, j] is the correlation
    (03-probability/03-covariance-correlation's `correlation`, already
    provided above) between feature column i and feature column j.

    The diagonal is always 1.0 (every feature correlates perfectly
    with itself), and the matrix is symmetric (corr(i, j) == corr(j, i)).
    """
    n_feat = x.shape[1]
    result = np.eye(n_feat)
    for i in range (n_feat):
        for j in range (i + 1, n_feat):
            val = correlation(x[:,i], x[:,j])
            result[i,j] = val
            result[j,i] = val
    return result

def most_correlated_pair(corr_matrix: np.ndarray) -> tuple[int, int]:
    """
    Given a correlation matrix, returns the (row, col) index of the
    single most correlated pair of DIFFERENT features (excluding the
    diagonal, which is always a trivial 1.0), by absolute value (a
    strong NEGATIVE correlation counts too).
    """
    n = corr_matrix.shape[0]
    x = corr_matrix.copy()
    np.fill_diagonal(x, 0.0)
    flat_idx = np.argmax(np.abs(x))
    return tuple(np.unravel_index(flat_idx,(n, n)))
