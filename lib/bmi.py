#!/usr/bin/env python3

class BMI:
    """BMI Calculations"""    
    @staticmethod
    def calculate_bmi_meters_kilograms(
            height: float,
            weight: float
    ) -> float:
        '''Calculates BMI using Meters and Kilograms'''
        return weight / (height ** 2)

    @staticmethod
    def cacluclate_bmi_centimeters_kilograms(
            weight: float,
            height: float
    ) -> float:
        '''Calculates BMI using Centimeters and Kilograms'''
        return weight / ((height / 100) ** 2)

    @staticmethod
    def calculate_bmi_inches_pounds(
            weight: float,
            height: float
    ) -> float:
        '''Calculates BMI using Inches and Pounds'''
        return (weight / (height ** 2)) * 703

    @staticmethod
    def calculate_bmi_feet_inches_pounds(
            weight: float,
            height: float,
            inches: float
    ) -> float:
        '''Calculates BMI using Feet, Inches and Pounds'''
        total_inches = (height * 12) + inches
        return (weight / (total_inches ** 2)) * 703
