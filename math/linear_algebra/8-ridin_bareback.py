def mat_mul(mat1, mat2):
    """A function that performs matrix multiplication"""
    if not mat1 or not mat2 or len(mat1[0]) != len(mat2):
        return None

    return [
        [
            sum(a * b for a, b in zip(row, col))
            for col in zip(*mat2)
        ]
        for row in mat1
    ]
