class DatabaseError(Exception):
    """Base class for other database-related exceptions"""
    pass


class UserNotFoundError(DatabaseError):
    """Raised when a user is not found in the database"""
    pass


class UserCreationError(DatabaseError):
    """Raised when there is an error creating a user"""
    pass


class UserUpdateError(DatabaseError):
    """Raised when there is an error updating a user"""
    pass


class UserAlreadyExists(DatabaseError):
    """Raised when user already exists in database"""
    pass
