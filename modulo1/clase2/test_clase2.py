from ...utilities import get_annotations_and_rvalues
from .clase2 import ejercicios_de_la_clase_2


ordered_answers = ejercicios_de_la_clase_2()
collected_types = get_annotations_and_rvalues(ejercicios_de_la_clase_2)


def _get_next_answer():
    try:
        if ordered_answers is not None:
            return next(ordered_answers)
    except StopIteration:
        print("No more answers")


def test_a_assignment():
    result = _get_next_answer()
    assert result == 10, "La primera asignación de `a` no es correcta"


def test_a_reassignment():
    assert _get_next_answer() == 20, "La reasignación de `a` no es correcta"


def test_b_assignment():
    assert _get_next_answer() == 5, "La asignación de `b` no es correcta"


def test_c_assignment():
    assert _get_next_answer() == 78.5, "La asignación de `c` no es correcta"


def test_d_assignment():
    assert _get_next_answer() is True, "La asignación de `d` no es correcta"


def test_e_assignment():
    assert _get_next_answer() == "Hola Mundo", "La asignación de `e` no es correcta"


def test_e_expression():
    expression = collected_types.get("e", "")[1]
    err_msg = "La expresión de `e` no es correcta"

    assert expression.find("Hola") != -1, err_msg
    assert expression.find("Mundo") != -1, err_msg
    assert expression.find("+") != -1, err_msg


def test_f_assignment():
    result = _get_next_answer()
    err_msg = "La asignación de `f` no es correcta"
    assert isinstance(result, list), err_msg
    for i in range(1, 6):
        assert i in result, err_msg


def test_g_assignment():
    result = _get_next_answer()
    err_msg = "La asignación de `g` no es correcta"
    assert isinstance(result, dict), err_msg
    assert result.get("a", "") == 1, err_msg
    assert result.get("b", "") == 2, err_msg
    assert result.get("c", "") == 3, err_msg


def test_h_assignment():
    result = _get_next_answer()
    err_msg = "La asignación de `h` no es correcta"
    assert isinstance(result, tuple), err_msg
    for i in range(1, 6):
        assert i in result, err_msg


def test_i_assignment():
    result = _get_next_answer()
    err_msg = "La asignación de `i` no es correcta"
    assert isinstance(result, set), err_msg
    for i in range(1, 6):
        assert i in result, err_msg
