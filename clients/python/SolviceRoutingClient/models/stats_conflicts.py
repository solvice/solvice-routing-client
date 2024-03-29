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


class StatsConflicts(object):
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
        'weight': 'int',
        'reasons': 'list[str]'
    }

    attribute_map = {
        'weight': 'weight',
        'reasons': 'reasons'
    }

    def __init__(self, weight=None, reasons=None):  # noqa: E501
        """StatsConflicts - a model defined in Swagger"""  # noqa: E501
        self._weight = None
        self._reasons = None
        self.discriminator = None
        if weight is not None:
            self.weight = weight
        if reasons is not None:
            self.reasons = reasons

    @property
    def weight(self):
        """Gets the weight of this StatsConflicts.  # noqa: E501

        Specific weight for unresolved goal reasons.  # noqa: E501

        :return: The weight of this StatsConflicts.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this StatsConflicts.

        Specific weight for unresolved goal reasons.  # noqa: E501

        :param weight: The weight of this StatsConflicts.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def reasons(self):
        """Gets the reasons of this StatsConflicts.  # noqa: E501


        :return: The reasons of this StatsConflicts.  # noqa: E501
        :rtype: list[str]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this StatsConflicts.


        :param reasons: The reasons of this StatsConflicts.  # noqa: E501
        :type: list[str]
        """

        self._reasons = reasons

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
        if issubclass(StatsConflicts, dict):
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
        if not isinstance(other, StatsConflicts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
