"""
This module implements various functions for physical units conversion.
"""

import numbers


def convert_speed(value, actual_unit: str, target_unit: str):
    """
    Convert speed value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (mph, kph)
    :param target_unit: string target physical unit (mph, kph)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    try:
        # test acceptable inputs
        if isinstance(value, numbers.Number) and \
                all(x in ["mph", "kph"] for x in [actual_unit, target_unit]):
            # check units equality
            if actual_unit == target_unit:
                return value

            # dictionary for conversion, key is target unit
            conversion = {"kph": lambda x: x * 0.621371192,
                          "mph": lambda x: x * 1.60934
                          }
            return conversion[target_unit](value)
    except Exception as ex:
        print(f"Something is wrong: {ex}")

    raise ValueError("value must be numeric,"
                     " actual_unit and target_unit accept only mph or kph values")

def convert_temperature(value, actual_unit: str, target_unit: str):
    """
    Convert temperature value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (F, K)
    :param target_unit: string target physical unit (F, K)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    try:
        # test acceptable inputs
        if isinstance(value, numbers.Number) and \
                all(x in ["F", "K"] for x in [actual_unit, target_unit]):
            if actual_unit == target_unit:
                return value

            # dictionary for conversion, key is target unit
            conversion = {"K": lambda x: 1.8 * (x - 273.15) + 32,
                          "F": lambda x: ((x - 32) / 1.8) + 273.15
                         }
            return conversion[target_unit](value)
    except Exception as ex:
        print(f"Something is wrong: {ex}")

    raise ValueError("value must be numeric,"
                         " actual_unit and target_unit accept only K or F values")

def convert_length(value, actual_unit: str, target_unit: str):
    """
    Convert length value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (m, km)
    :param target_unit: string target physical unit (m, km)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    try:
        # test acceptable inputs
        if isinstance(value, numbers.Number) and \
                all(x in ["m", "km"] for x in [actual_unit, target_unit]):
            if actual_unit == target_unit:
                return value

            # dictionary for conversion, key is target unit
            conversion = {"m": lambda x: x * 1000,
                          "km": lambda x: x / 1000
                         }
            return conversion[target_unit](value)
    except Exception as ex:
        print(f"Something is wrong: {ex}")

    raise ValueError("value must be numeric,"
                         " actual_unit and target_unit accept only m or km values")
