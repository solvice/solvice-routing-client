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
from SolviceRoutingClient.models.order_date_windows import OrderDateWindows  # noqa: F401,E501
from SolviceRoutingClient.models.order_windows import OrderWindows  # noqa: F401,E501


class Order(object):
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
        'name': 'str',
        'location': 'str',
        'activity': 'str',
        'ride': 'str',
        'priority': 'int',
        'duration': 'int',
        'demand': 'int',
        'demand2': 'int',
        'type': 'list[str]',
        'windows': 'list[OrderWindows]',
        'duration_squash': 'int',
        'date_windows': 'list[OrderDateWindows]',
        'allowed_vehicles': 'list[str]',
        'disallowed_vehicles': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'activity': 'activity',
        'ride': 'ride',
        'priority': 'priority',
        'duration': 'duration',
        'demand': 'demand',
        'demand2': 'demand2',
        'type': 'type',
        'windows': 'windows',
        'duration_squash': 'durationSquash',
        'date_windows': 'dateWindows',
        'allowed_vehicles': 'allowedVehicles',
        'disallowed_vehicles': 'disallowedVehicles'
    }

    def __init__(self, name=None, location=None, activity='PICKUP', ride=None, priority=None, duration=None, demand=None, demand2=None, type=None, windows=None, duration_squash=None, date_windows=None, allowed_vehicles=None, disallowed_vehicles=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._location = None
        self._activity = None
        self._ride = None
        self._priority = None
        self._duration = None
        self._demand = None
        self._demand2 = None
        self._type = None
        self._windows = None
        self._duration_squash = None
        self._date_windows = None
        self._allowed_vehicles = None
        self._disallowed_vehicles = None
        self.discriminator = None
        self.name = name
        self.location = location
        if activity is not None:
            self.activity = activity
        if ride is not None:
            self.ride = ride
        if priority is not None:
            self.priority = priority
        if duration is not None:
            self.duration = duration
        if demand is not None:
            self.demand = demand
        if demand2 is not None:
            self.demand2 = demand2
        if type is not None:
            self.type = type
        if windows is not None:
            self.windows = windows
        if duration_squash is not None:
            self.duration_squash = duration_squash
        if date_windows is not None:
            self.date_windows = date_windows
        if allowed_vehicles is not None:
            self.allowed_vehicles = allowed_vehicles
        if disallowed_vehicles is not None:
            self.disallowed_vehicles = disallowed_vehicles

    @property
    def name(self):
        """Gets the name of this Order.  # noqa: E501

        Unique name of an order  # noqa: E501

        :return: The name of this Order.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Order.

        Unique name of an order  # noqa: E501

        :param name: The name of this Order.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def location(self):
        """Gets the location of this Order.  # noqa: E501

        Location of an order; should be in location list.  # noqa: E501

        :return: The location of this Order.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Order.

        Location of an order; should be in location list.  # noqa: E501

        :param location: The location of this Order.  # noqa: E501
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def activity(self):
        """Gets the activity of this Order.  # noqa: E501

        Activity type. When defining a PDP problem, be sure to have both a pickup and a delivery activity for the same ride. See ride.  # noqa: E501

        :return: The activity of this Order.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this Order.

        Activity type. When defining a PDP problem, be sure to have both a pickup and a delivery activity for the same ride. See ride.  # noqa: E501

        :param activity: The activity of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["PICKUP", "DROPOFF", "EXECUTE", "BREAK"]  # noqa: E501
        if activity not in allowed_values:
            raise ValueError(
                "Invalid value for `activity` ({0}), must be one of {1}"  # noqa: E501
                .format(activity, allowed_values)
            )

        self._activity = activity

    @property
    def ride(self):
        """Gets the ride of this Order.  # noqa: E501

        Only applicable for PDP. Use the same ride string for a pickup and a delivery activity.  # noqa: E501

        :return: The ride of this Order.  # noqa: E501
        :rtype: str
        """
        return self._ride

    @ride.setter
    def ride(self, ride):
        """Sets the ride of this Order.

        Only applicable for PDP. Use the same ride string for a pickup and a delivery activity.  # noqa: E501

        :param ride: The ride of this Order.  # noqa: E501
        :type: str
        """

        self._ride = ride

    @property
    def priority(self):
        """Gets the priority of this Order.  # noqa: E501

        Priority allows you to make certain visits a priority over others. In some cases you have more visits than you can serve, resulting in a few unserved. But if you want to make sure your high priority visits take precedence, use this parameter and set it to 100.   # noqa: E501

        :return: The priority of this Order.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Order.

        Priority allows you to make certain visits a priority over others. In some cases you have more visits than you can serve, resulting in a few unserved. But if you want to make sure your high priority visits take precedence, use this parameter and set it to 100.   # noqa: E501

        :param priority: The priority of this Order.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def duration(self):
        """Gets the duration of this Order.  # noqa: E501

        Duration of the service in minutes  # noqa: E501

        :return: The duration of this Order.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Order.

        Duration of the service in minutes  # noqa: E501

        :param duration: The duration of this Order.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def demand(self):
        """Gets the demand of this Order.  # noqa: E501

        Load in cargo for capacity type 1.  # noqa: E501

        :return: The demand of this Order.  # noqa: E501
        :rtype: int
        """
        return self._demand

    @demand.setter
    def demand(self, demand):
        """Sets the demand of this Order.

        Load in cargo for capacity type 1.  # noqa: E501

        :param demand: The demand of this Order.  # noqa: E501
        :type: int
        """

        self._demand = demand

    @property
    def demand2(self):
        """Gets the demand2 of this Order.  # noqa: E501

        Load in cargo for capacity type 2.  # noqa: E501

        :return: The demand2 of this Order.  # noqa: E501
        :rtype: int
        """
        return self._demand2

    @demand2.setter
    def demand2(self, demand2):
        """Sets the demand2 of this Order.

        Load in cargo for capacity type 2.  # noqa: E501

        :param demand2: The demand2 of this Order.  # noqa: E501
        :type: int
        """

        self._demand2 = demand2

    @property
    def type(self):
        """Gets the type of this Order.  # noqa: E501

        Type restriction which can force some orders to be executed by Vehicles with the same type.  # noqa: E501

        :return: The type of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Order.

        Type restriction which can force some orders to be executed by Vehicles with the same type.  # noqa: E501

        :param type: The type of this Order.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def windows(self):
        """Gets the windows of this Order.  # noqa: E501

        A time window consists of a starttime and an endtime. The order cannot be processed before the starttime and should start being processed before endtime. If the time window is hard, then it should always be fulfilled. E.g. a driver would prefer to drive 3 hours longer than not be on time wrt that time window for that order. So hard time window constraints are pretty extreme!  # noqa: E501

        :return: The windows of this Order.  # noqa: E501
        :rtype: list[OrderWindows]
        """
        return self._windows

    @windows.setter
    def windows(self, windows):
        """Sets the windows of this Order.

        A time window consists of a starttime and an endtime. The order cannot be processed before the starttime and should start being processed before endtime. If the time window is hard, then it should always be fulfilled. E.g. a driver would prefer to drive 3 hours longer than not be on time wrt that time window for that order. So hard time window constraints are pretty extreme!  # noqa: E501

        :param windows: The windows of this Order.  # noqa: E501
        :type: list[OrderWindows]
        """

        self._windows = windows

    @property
    def duration_squash(self):
        """Gets the duration_squash of this Order.  # noqa: E501

        When multiple orders are on the same location, the service duration can be lower due to simultaneous handling. The duration will then be this value. is useful when you have many stops at the same location, which could be an apartment complex. Normally, each stop has a duration value of let's say 10 minutes, which accounts for parking and finding the entrance. If you had 6 stops assigned to a driver at the same time, it doesn't take an hour in total! Use this parameter to squash the durations of each subsequent delivery at the same address. If you set it to 1, it will squash it to 1 minute, so the total duration for the above 6 stops would be 15 minutes.  # noqa: E501

        :return: The duration_squash of this Order.  # noqa: E501
        :rtype: int
        """
        return self._duration_squash

    @duration_squash.setter
    def duration_squash(self, duration_squash):
        """Sets the duration_squash of this Order.

        When multiple orders are on the same location, the service duration can be lower due to simultaneous handling. The duration will then be this value. is useful when you have many stops at the same location, which could be an apartment complex. Normally, each stop has a duration value of let's say 10 minutes, which accounts for parking and finding the entrance. If you had 6 stops assigned to a driver at the same time, it doesn't take an hour in total! Use this parameter to squash the durations of each subsequent delivery at the same address. If you set it to 1, it will squash it to 1 minute, so the total duration for the above 6 stops would be 15 minutes.  # noqa: E501

        :param duration_squash: The duration_squash of this Order.  # noqa: E501
        :type: int
        """

        self._duration_squash = duration_squash

    @property
    def date_windows(self):
        """Gets the date_windows of this Order.  # noqa: E501

        List of start/end date/time combinations.  # noqa: E501

        :return: The date_windows of this Order.  # noqa: E501
        :rtype: list[OrderDateWindows]
        """
        return self._date_windows

    @date_windows.setter
    def date_windows(self, date_windows):
        """Sets the date_windows of this Order.

        List of start/end date/time combinations.  # noqa: E501

        :param date_windows: The date_windows of this Order.  # noqa: E501
        :type: list[OrderDateWindows]
        """

        self._date_windows = date_windows

    @property
    def allowed_vehicles(self):
        """Gets the allowed_vehicles of this Order.  # noqa: E501

        List of vehicle names that are allowed to be assigned to this order  # noqa: E501

        :return: The allowed_vehicles of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_vehicles

    @allowed_vehicles.setter
    def allowed_vehicles(self, allowed_vehicles):
        """Sets the allowed_vehicles of this Order.

        List of vehicle names that are allowed to be assigned to this order  # noqa: E501

        :param allowed_vehicles: The allowed_vehicles of this Order.  # noqa: E501
        :type: list[str]
        """

        self._allowed_vehicles = allowed_vehicles

    @property
    def disallowed_vehicles(self):
        """Gets the disallowed_vehicles of this Order.  # noqa: E501

        List of vehicle names that are not allowed to be assigned to this order  # noqa: E501

        :return: The disallowed_vehicles of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._disallowed_vehicles

    @disallowed_vehicles.setter
    def disallowed_vehicles(self, disallowed_vehicles):
        """Sets the disallowed_vehicles of this Order.

        List of vehicle names that are not allowed to be assigned to this order  # noqa: E501

        :param disallowed_vehicles: The disallowed_vehicles of this Order.  # noqa: E501
        :type: list[str]
        """

        self._disallowed_vehicles = disallowed_vehicles

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
