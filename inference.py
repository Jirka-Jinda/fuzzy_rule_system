import fuzzy_set as fs
import fuzzy_set_operations as fo
import numpy as np

# slajdy I: http://belohlavek.inf.upol.cz/vyuka/flfs_I.pdf
# slajdy II, 42: http://belohlavek.inf.upol.cz/vyuka/flfs_II.pdf
# rukopis: http://belohlavek.inf.upol.cz/vyuka/UI-6-fuzzy-rules.pdf
# 3D grafy: https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

def infer(rules: np.ndarray, inputs: list(fs.fuzzy_set), operation=fo.tnorm_Lukas) -> fs.fuzzy_set:
    result = []
    # apply rule for every set
    for k in range(len(inputs)):
        # consider rule_i a m*n matrix, where: m = |input|, n = |output|
        rule_matrix = fo.rule_to_matrix(rules[k])
        # and input as 1*m matrix
        input_matrix = fo.fs_to_matrix(inputs[k])
        # product of multiplication is n*1 matrix
        result_k = np.matmul(input_matrix, rule_matrix)
        # which is result that we transform back to fuzzy set
        result_k = fo.matrix_to_fs(result_k)
        # and append to results
        result.append(result_k)

    # combine all results into one output