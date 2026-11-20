"""Tests de la práctica 1: conversor de unidades creado por IA."""

import pytest

import m1_practica_conversor_IA as conversor


def test_constantes() -> None:
    assert conversor.KM_POR_MILLA == 1.609344
    assert conversor.KG_POR_LIBRA == 0.45359237


@pytest.mark.parametrize(
    ("celsius", "fahrenheit"),
    [(0, 32), (100, 212), (-40, -40), (37, 98.6)],
)
def test_conversiones_de_temperatura(
    celsius: float, fahrenheit: float
) -> None:
    assert conversor.celsius_a_fahrenheit(celsius) == pytest.approx(fahrenheit)
    assert conversor.fahrenheit_a_celsius(fahrenheit) == pytest.approx(celsius)


@pytest.mark.parametrize(
    ("convertir", "valor", "esperado"),
    [
        (conversor.km_a_millas, 1.609344, 1.0),
        (conversor.millas_a_km, 26.2, 42.1648128),
        (conversor.kg_a_libras, 0.45359237, 1.0),
        (conversor.libras_a_kg, 150, 68.0388555),
    ],
)
def test_conversiones_de_distancia_y_peso(
    convertir, valor: float, esperado: float
) -> None:
    assert convertir(valor) == pytest.approx(esperado)


def test_conversiones_devuelven_float() -> None:
    assert isinstance(conversor.celsius_a_fahrenheit(10), float)
    assert isinstance(conversor.millas_a_km(10), float)
    assert isinstance(conversor.libras_a_kg(10), float)


def test_conversiones_inversas() -> None:
    assert conversor.millas_a_km(
        conversor.km_a_millas(42)
    ) == pytest.approx(42)
    assert conversor.libras_a_kg(
        conversor.kg_a_libras(80)
    ) == pytest.approx(80)


def test_formatear() -> None:
    assert conversor.formatear(
        100, "°C", 212.0, "°F"
    ) == "100.00 °C = 212.00 °F"
    assert conversor.formatear(
        5, "km", 3.106855, "mi"
    ) == "5.00 km = 3.11 mi"


@pytest.mark.parametrize(
    ("opcion", "valor", "esperado"),
    [
        ("1", "100", "100.00 °C = 212.00 °F"),
        ("2", "212", "212.00 °F = 100.00 °C"),
        ("3", "10", "10.00 km = 6.21 mi"),
        ("4", "10", "10.00 mi = 16.09 km"),
        ("5", "10", "10.00 kg = 22.05 lb"),
        ("6", "10", "10.00 lb = 4.54 kg"),
    ],
)
def test_main_realiza_la_conversion_elegida(
    monkeypatch, capsys, opcion: str, valor: str, esperado: str
) -> None:
    respuestas = iter([opcion, valor, "0"])
    monkeypatch.setattr("builtins.input", lambda *_: next(respuestas))

    conversor.main()

    assert esperado in capsys.readouterr().out


@pytest.mark.parametrize("opcion", ["7", "texto", ""])
def test_main_rechaza_opciones_no_validas(
    monkeypatch, capsys, opcion: str
) -> None:
    respuestas = iter([opcion, "0"])
    monkeypatch.setattr("builtins.input", lambda *_: next(respuestas))

    conversor.main()

    assert "Opción no válida" in capsys.readouterr().out


def test_main_sale_con_cero(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda *_: "0")

    conversor.main()

    salida = capsys.readouterr().out
    assert "0. Salir" in salida
    assert "Hasta luego." in salida


def test_main_permite_varias_conversiones(monkeypatch, capsys) -> None:
    respuestas = iter(["1", "0", "3", "10", "0"])
    monkeypatch.setattr("builtins.input", lambda *_: next(respuestas))

    conversor.main()

    salida = capsys.readouterr().out
    assert "0.00 °C = 32.00 °F" in salida
    assert "10.00 km = 6.21 mi" in salida
