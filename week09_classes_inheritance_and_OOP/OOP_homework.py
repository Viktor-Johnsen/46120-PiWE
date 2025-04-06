
'''This is a file'''

import numpy as np
import yaml
import matplotlib.pyplot as plt
import seaborn as sns


class GeneralWindTurbine:
    '''This is a class meant for all types of wind turbines'''
    def __init__(self, specs_, name_=None):
        self.rotor_diameter = specs_['rotor_diameter']  # [m]
        self.hub_height = specs_['hub_height']  # [m]
        self.rated_power = specs_['rated_power']  # [kW]
        self.v_in = specs_['cut_in_wind_speed']  # [m/s]
        self.v_rated = specs_['rated_wind_speed']  # [m/s]
        self.v_out = specs_['cut_out_wind_speed']  # [m/s]
        self.name = name_

    def get_power(self, wind_speeds_):
        ''' This method returns the theoretical power curve.'''
        power_out = np.empty(len(wind_speeds_))
        for i, v in enumerate(wind_speeds_):
            print(i, v)
            if v < self.v_in or v > self.v_out:
                power_out[i] = 0
            elif self.v_in <= v < self.v_rated:
                power_out[i] = self.rated_power * (v / self.v_rated) ** 3
            else:  # v_rated <= v <= v_out
                power_out[i] = self.rated_power
        return power_out


class WindTurbine(GeneralWindTurbine):
    ''' This class helps produce the true power curve.'''
    def __init__(self, specs_, power_curve_, name_=None):
        GeneralWindTurbine.__init__(
            self, specs_, name_=None)
        self.power_curve_data = power_curve_
        # wind speed [m/s] and power [kW]

    def get_power(self, wind_speeds_):
        ''' This method produces the true power curve.'''
        power_out = np.interp(wind_speeds_,
                              self.power_curve_data[:, 0],
                              self.power_curve_data[:, 1])
        return power_out


if __name__ == "__main__":
    power_curve = np.loadtxt("LEANWIND_Reference_8MW_164.csv",
                             delimiter=',',
                             skiprows=1,
                             usecols=(0, 1))
    wind_speeds = np.arange(4, 25, 0.5)
    specs = yaml.safe_load(open("LEANWIND_Reference_8MW_164.yaml",
                                encoding='UTF-8'))
    wt1 = GeneralWindTurbine(specs, name_='wt1')
    wt2 = WindTurbine(specs, power_curve, name_='wt2')

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(wind_speeds, wt1.get_power(wind_speeds),
            label='General Wind Turbine', color='blue')
    ax.plot(wind_speeds, wt2.get_power(wind_speeds),
            label='Wind Turbine', color='orange')
    ax.set_title('Wind Turbine Power Curves')
    ax.set_xlabel('Wind Speed [m/s]')
    ax.set_ylabel('Power [kW]')
    ax.legend()
    plt.grid()
    plt.show()
