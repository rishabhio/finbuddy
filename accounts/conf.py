class UserType(object):
    ADMINUSER = 0
    WEBAPPUSER = 1

    USER_TYPES = (
        (ADMINUSER, 'Admin'),
        (WEBAPPUSER, 'EndUser'),
    )
