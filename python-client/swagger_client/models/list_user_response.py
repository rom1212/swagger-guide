# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ListUserResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'users': 'list[User]',
        'next_page_token': 'str'
    }

    attribute_map = {
        'users': 'users',
        'next_page_token': 'nextPageToken'
    }

    def __init__(self, users=None, next_page_token=None):
        """
        ListUserResponse - a model defined in Swagger
        """

        self._users = None
        self._next_page_token = None

        if users is not None:
          self.users = users
        if next_page_token is not None:
          self.next_page_token = next_page_token

    @property
    def users(self):
        """
        Gets the users of this ListUserResponse.

        :return: The users of this ListUserResponse.
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this ListUserResponse.

        :param users: The users of this ListUserResponse.
        :type: list[User]
        """

        self._users = users

    @property
    def next_page_token(self):
        """
        Gets the next_page_token of this ListUserResponse.

        :return: The next_page_token of this ListUserResponse.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """
        Sets the next_page_token of this ListUserResponse.

        :param next_page_token: The next_page_token of this ListUserResponse.
        :type: str
        """

        self._next_page_token = next_page_token

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ListUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
