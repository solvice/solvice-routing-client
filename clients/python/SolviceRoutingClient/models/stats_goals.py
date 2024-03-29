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
from SolviceRoutingClient.models.stats_conflicts import StatsConflicts  # noqa: F401,E501


class StatsGoals(object):
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
        'goal': 'str',
        'weight': 'int',
        'conflicts': 'list[StatsConflicts]'
    }

    attribute_map = {
        'goal': 'goal',
        'weight': 'weight',
        'conflicts': 'conflicts'
    }

    def __init__(self, goal=None, weight=None, conflicts=None):  # noqa: E501
        """StatsGoals - a model defined in Swagger"""  # noqa: E501
        self._goal = None
        self._weight = None
        self._conflicts = None
        self.discriminator = None
        if goal is not None:
            self.goal = goal
        if weight is not None:
            self.weight = weight
        if conflicts is not None:
            self.conflicts = conflicts

    @property
    def goal(self):
        """Gets the goal of this StatsGoals.  # noqa: E501

        Goal name  # noqa: E501

        :return: The goal of this StatsGoals.  # noqa: E501
        :rtype: str
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """Sets the goal of this StatsGoals.

        Goal name  # noqa: E501

        :param goal: The goal of this StatsGoals.  # noqa: E501
        :type: str
        """

        self._goal = goal

    @property
    def weight(self):
        """Gets the weight of this StatsGoals.  # noqa: E501

        Weight total for goal.  # noqa: E501

        :return: The weight of this StatsGoals.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this StatsGoals.

        Weight total for goal.  # noqa: E501

        :param weight: The weight of this StatsGoals.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def conflicts(self):
        """Gets the conflicts of this StatsGoals.  # noqa: E501


        :return: The conflicts of this StatsGoals.  # noqa: E501
        :rtype: list[StatsConflicts]
        """
        return self._conflicts

    @conflicts.setter
    def conflicts(self, conflicts):
        """Sets the conflicts of this StatsGoals.


        :param conflicts: The conflicts of this StatsGoals.  # noqa: E501
        :type: list[StatsConflicts]
        """

        self._conflicts = conflicts

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
        if issubclass(StatsGoals, dict):
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
        if not isinstance(other, StatsGoals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
