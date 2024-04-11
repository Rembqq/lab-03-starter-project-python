from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/multiply_matrices')
def multiply_matrices() -> dict:
    # Generate two random matrices of size 10x10
    matrix_a = np.random.rand(10, 10)
    matrix_b = np.random.rand(10, 10)

    # Multiply the matrices
    result_matrix = np.dot(matrix_a, matrix_b)

    return {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "result_matrix": result_matrix.tolist()
    }