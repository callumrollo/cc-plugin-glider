#!/usr/bin/env python
"""
cc_plugin_glider/required_var_attrs.py

Dictionary of required variables and their attributes

Attributes with values set to None mean we only check that the attribute exists, not whether the value matches
"""
required_var_attrs = {
    "time": {
        "dtype": "f8",
        "standard_name": "time",
        "units": "seconds since 1970-01-01T00:00:00Z",
        "calendar": "gregorian",
        "long_name": "Time",
        "observation_type": "measured",
    },
    "lat": {
        "standard_name": "latitude",
        "units": "degrees_north",
        "_FillValue": None,
        "ancillary_variables": None,
        "comment": None,
        "coordinate_reference_frame": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "reference": None,
        "valid_max": None,
        "valid_min": None,
    },
    "lon": {
        "standard_name": "longitude",
        "units": "degrees_east",
        "_FillValue": None,
        "ancillary_variables": None,
        "comment": None,
        "coordinate_reference_frame": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "reference": None,
        "valid_max": None,
        "valid_min": None,
    },
    "trajectory": {"cf_role": None, "comment": None, "long_name": None},
    "profile_id": {
        "dtype": "<i4",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "valid_min": None,
        "valid_max": None,
    },
    "profile_time": {
        "dtype": "<f8",
        "standard_name": "time",
        "units": "seconds since 1970-01-01T00:00:00Z",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
    },
    "profile_lat": {
        "dtype": "<f8",
        "standard_name": "latitude",
        "units": "degrees_north",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "valid_min": None,
        "valid_max": None,
    },
    "profile_lon": {
        "dtype": "<f8",
        "standard_name": "longitude",
        "units": "degrees_east",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "valid_min": None,
        "valid_max": None,
    },
    "depth": {
        "standard_name": "depth",
        "units": None,
        "_FillValue": None,
        "accuracy": None,
        "ancillary_variables": None,
        "comment": None,
        "instrument": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "positive": None,
        "precision": None,
        "reference_datum": None,
        "resolution": None,
        "standard_name": None,
        "valid_max": None,
        "valid_min": None,
    },
    "pressure": {
        "standard_name": "sea_water_pressure",
        "units": None,
        "_FillValue": None,
        "accuracy": None,
        "ancillary_variables": None,
        "comment": None,
        "instrument": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "positive": None,
        "precision": None,
        "reference_datum": None,
        "resolution": None,
        "standard_name": None,
        "valid_max": None,
        "valid_min": None,
    },
    "temperature": {
        "dtype": "f8",
        "standard_name": "sea_water_temperature",
        "units": "degrees_C",
        "_FillValue": None,
        "accuracy": None,
        "ancillary_variables": None,
        "instrument": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "precision": None,
        "resolution": None,
        "valid_max": None,
        "valid_min": None,
    },
    "conductivity": {
        "dtype": "f8",
        "standard_name": "sea_water_electrical_conductivity",
        "units": None,
        "_FillValue": None,
        "accuracy": None,
        "ancillary_variables": None,
        "instrument": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "precision": None,
        "resolution": None,
        "valid_max": None,
        "valid_min": None,
    },
    "salinity": {
        "dtype": "f8",
        "standard_name": "sea_water_practical_salinity",
        "units": None,
        "_FillValue": None,
        "accuracy": None,
        "ancillary_variables": None,
        "instrument": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "precision": None,
        "resolution": None,
        "valid_max": None,
        "valid_min": None,
    },
    "density": {
        "dtype": "f8",
        "standard_name": "sea_water_density",
        "units": None,
        "_FillValue": None,
        "accuracy": None,
        "ancillary_variables": None,
        "instrument": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "precision": None,
        "resolution": None,
        "valid_max": None,
        "valid_min": None,
    },
    "time_uv": {
        "standard_name": "time",
        "units": "seconds since 1970-01-01T00:00:00Z",
        "_FillValue": None,
        "observation_type": None,
    },
    "lat_uv": {
        "dtype": "<f8",
        "standard_name": "latitude",
        "units": "degrees_north",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "valid_min": None,
        "valid_max": None,
    },
    "lon_uv": {
        "dtype": "<f8",
        "standard_name": "longitude",
        "units": "degrees_east",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "valid_min": None,
        "valid_max": None,
    },
    "u": {
        "dtype": "<f8",
        "standard_name": "eastward_sea_water_velocity",
        "units": "m s-1",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "valid_min": None,
        "valid_max": None,
    },
    "v": {
        "dtype": "<f8",
        "standard_name": "northward_sea_water_velocity",
        "units": "m s-1",
        "_FillValue": None,
        "comment": None,
        "long_name": None,
        "observation_type": None,
        "platform": None,
        "valid_min": None,
        "valid_max": None,
    },
    "platform": {
        "dtype": "<i4",
        "_FillValue": None,
        "comment": None,
        "id": None,
        "instrument": None,
        "long_name": None,
        "type": None,
        "wmo_id": None,
    },
    "instrument_ctd": {
        "dtype": "<i4",
        "_FillValue": None,
        "calibration_date": None,
        "calibration_report": None,
        "comment": None,
        "factory_calibrated": None,
        "long_name": None,
        "make_model": None,
        "platform": None,
        "serial_number": None,
        "type": None,
    },
}
