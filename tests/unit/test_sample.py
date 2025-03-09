from src.analyzers import example_function  # Importa una función de `src/`


def test_example_function():
    """Prueba que verifica que example_function() retorna el valor esperado."""
    result = example_function()
    assert result == "Función de ejemplo ejecutada"
