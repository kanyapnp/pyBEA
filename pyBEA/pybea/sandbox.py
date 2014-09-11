"""
TODO:

1. Create functions out of the subclasses of the Request object.

"""
import numpy as np
import pandas as pd

from api import *


def get_data_set_list(UserID, ResultFormat='JSON'):
    """
    Retrieve list of currently available data sets.

    Parameters
    ----------
    UserID : str
        Before using the API, users must obtain a unique 36-character UserID by
        registering at http://www.bea.gov/api/signup/.
    ResultFormat : str (default='JSON')
        The API returns data in one of two formats: JSON or XML. The
        ResultFormat parameter can be included on any request to specify the
        format of the results. If ResultFormat is not supplied on the request,
        or an invalid ResultFormat is specified, the default format returned is
        JSON. The valid values for ResultFormat are 'JSON' and 'XML'.

    Returns
    -------
    data_set_list : Pandas.DataFrame
        A Pandas DataFrame containing the DatasetName and DatasetDescription
        attributes for all available data sets.

    """
    tmp_request = DataSetListRequest(UserID=UserID,
                                     Method='GetDataSetList',
                                     ResultFormat=ResultFormat,
                                     )
    data_set_list = pd.DataFrame(tmp_request.data_set, dtype=np.int64)
    return data_set_list


def get_parameter_list(UserID, DataSetName, ResultFormat='JSON'):
    """
    Retrieve list of required and optional parameters for a given data set.

    Parameters
    ----------
    UserID : str
        Before using the API, users must obtain a unique 36-character UserID by
        registering at http://www.bea.gov/api/signup/.
    DataSetName : str

    ResultFormat : str (default='JSON')
        The API returns data in one of two formats: JSON or XML. The
        ResultFormat parameter can be included on any request to specify the
        format of the results. If ResultFormat is not supplied on the request,
        or an invalid ResultFormat is specified, the default format returned is
        JSON. The valid values for ResultFormat are 'JSON' and 'XML'.

    Returns
    -------
    parameter_list : Pandas.DataFrame
        A Pandas DataFrame containing the metadata associated with the
        parameters of the requested data set.

    Notes
    -----
    The function returns the following metadata for each required and optional
    parameter in the specified data set.

    - ParameterName: the name of the parameter as used in a data request
    - ParameterDataType: String or Integer
    - ParameterDescription: a description of the parameter
    - ParameterIsRequired: 0 if the parameter can be omitted from a request, 1
    if required.
    - ParameterDefaultValue: the default value used for the request if the
    parameter is not supplied
    - MultipleAcceptedFlag: 0 if the parameter may only have a single value, 1
    if multiple values are permitted. Note that multiple values for a parameter
    are submitted as a comma-separated string.
    - AllValue: the special value for a parameter that means all valid values
    are used without supplying them individually

    """
    tmp_request = ParameterListRequest(UserID=UserID,
                                       Method='GetParameterList',
                                       DataSetName=DataSetName,
                                       ResultFormat=ResultFormat,
                                       )
    parameter_list = pd.DataFrame(tmp_request.parameter_list, dtype=np.int64)
    return parameter_list


def get_parameter_values(self, UserID, DataSetName, ParameterName,
                         ResultFormat='JSON', **params):
    """
    Retrieve list of valid parameter values for a given data set.

    Parameters
    ----------
    UserID : str
        Before using the API, users must obtain a unique 36-character UserID by
        registering at http://www.bea.gov/api/signup/.
    DataSetName : str

    ParameterName : str

    ResultFormat : str (default='JSON')
        The API returns data in one of two formats: JSON or XML. The
        ResultFormat parameter can be included on any request to specify the
        format of the results. If ResultFormat is not supplied on the request,
        or an invalid ResultFormat is specified, the default format returned is
        JSON. The valid values for ResultFormat are 'JSON' and 'XML'.
    params : dict

    Returns
    -------
    data : Pandas.DataFrame
        A Pandas DataFrame containing the requested data.

    """
    tmp_request = Request(UserID=UserID,
                          Method='GetParameterValues',
                          DataSetName=DataSetName,
                          ParameterName=DataSetName,
                          ResultFormat=ResultFormat,
                          **params)

    return tmp_request.response.content


def get_data(UserID, DataSetName, ResultFormat='JSON', **params):
    """
    Retrieve data from the Bureau of Economic Analysis (BEA) data api.

    Parameters
    ----------
    UserID : str
        Before using the API, users must obtain a unique 36-character UserID by
        registering at http://www.bea.gov/api/signup/.
    DataSetName : str

    ResultFormat : str (default='JSON')
        The API returns data in one of two formats: JSON or XML. The
        ResultFormat parameter can be included on any request to specify the
        format of the results. If ResultFormat is not supplied on the request,
        or an invalid ResultFormat is specified, the default format returned is
        JSON. The valid values for ResultFormat are 'JSON' and 'XML'.
    params : dict

    Returns
    -------
    data : Pandas.DataFrame
        A Pandas DataFrame containing the requested data.

    """
    if DataSetName == 'RegionalData':
        tmp_request = RegionalDataRequest(UserID=UserID,
                                          Method='GetData',
                                          ResultFormat=ResultFormat,
                                          **params)
    elif DataSetName == 'NIPA':
        tmp_request = NIPARequest(UserID=UserID,
                                  Method='GetData',
                                  ResultFormat=ResultFormat,
                                  **params)
    elif DataSetName == 'NIUnderlyingDetail':
        tmp_request = NIPARequest(UserID=UserID,
                                  Method='GetData',
                                  ResultFormat=ResultFormat,
                                  **params)
    elif DataSetName == 'FixedAssets':
        tmp_request = NIPARequest(UserID=UserID,
                                  Method='GetData',
                                  ResultFormat=ResultFormat,
                                  **params)
    else:
        raise ValueError("Invalid DataSetName requested.")

    # convert to DataFrame
    tmp_df = pd.DataFrame(tmp_request.data, dtype=np.int64)

    return tmp_df
