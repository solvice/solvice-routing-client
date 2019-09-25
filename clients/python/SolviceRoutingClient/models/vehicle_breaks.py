# coding: utf-8

"""
    OnRoute API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class VehicleBreaks(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'breakstart': 'int',
        'breakend': 'int',
        'breakduration': 'int'
    }

    attribute_map = {
        'breakstart': 'breakstart',
        'breakend': 'breakend',
        'breakduration': 'breakduration'
    }

    def __init__(self, breakstart=None, breakend=None, breakduration=None):  # noqa: E501
        """VehicleBreaks - a model defined in Swagger"""  # noqa: E501
        self._breakstart = None
        self._breakend = None
        self._breakduration = None
        self.discriminator = None
        self.breakstart = breakstart
        self.breakend = breakend
        self.breakduration = breakduration

    @property
    def breakstart(self):
        """Gets the breakstart of this VehicleBreaks.  # noqa: E501

        Earliest starting time of break  # noqa: E501

        :return: The breakstart of this VehicleBreaks.  # noqa: E501
        :rtype: int
        """
        return self._breakstart

    @breakstart.setter
    def breakstart(self, breakstart):
        """Sets the breakstart of this VehicleBreaks.

        Earliest starting time of break  # noqa: E501

        :param breakstart: The breakstart of this VehicleBreaks.  # noqa: E501
        :type: int
        """
        if breakstart is None:
            raise ValueError("Invalid value for `breakstart`, must not be `None`")  # noqa: E501

        self._breakstart = breakstart

    @property
    def breakend(self):
        """Gets the breakend of this VehicleBreaks.  # noqa: E501

        Earliest ending time of break.  # noqa: E501

        :return: The breakend of this VehicleBreaks.  # noqa: E501
        :rtype: int
        """
        return self._breakend

    @breakend.setter
    def breakend(self, breakend):
        """Sets the breakend of this VehicleBreaks.

        Earliest ending time of break.  # noqa: E501

        :param breakend: The breakend of this VehicleBreaks.  # noqa: E501
        :type: int
        """
        if breakend is None:
            raise ValueError("Invalid value for `breakend`, must not be `None`")  # noqa: E501

        self._breakend = breakend

    @property
    def breakduration(self):
        """Gets the breakduration of this VehicleBreaks.  # noqa: E501

        Duration of break, should be less than end minus start.  # noqa: E501

        :return: The breakduration of this VehicleBreaks.  # noqa: E501
        :rtype: int
        """
        return self._breakduration

    @breakduration.setter
    def breakduration(self, breakduration):
        """Sets the breakduration of this VehicleBreaks.

        Duration of break, should be less than end minus start.  # noqa: E501

        :param breakduration: The breakduration of this VehicleBreaks.  # noqa: E501
        :type: int
        """
        if breakduration is None:
            raise ValueError("Invalid value for `breakduration`, must not be `None`")  # noqa: E501

        self._breakduration = breakduration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VehicleBreaks, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VehicleBreaks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
