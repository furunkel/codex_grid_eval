
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_by_email(email):
    """
    Given a string 'email', return the user object associated with that email.
    If 'email' is an empty string, return None.
    If 'email' is not associated with any user, return None.
    """
    if email == '':
        return None
    else:
        return User.query.filter_by(email=email).first()


def get_user_by_id(user_id):
    """
    Given an integer 'user_id', return the user object associated with that id.
    If 'user_id' is not associated with any user, return None.
    """
    return User.query.filter_by(id=user_id).first()


def get_user_by_username(username):
    """
    Given a string 'username', return the user object associated with that username.
    If 'username' is an empty string, return None.
    If 'username' is not associated with any user, return None.
    """
    if username == '':
        return None
    else:
        return User.query.filter_by(username=username).first()


def get_user_by_username_or_email(username_or_email):
    """
    Given a string 'username_or_email', return the user object associated with that username or email.
    If 'username_or_email' is an empty string, return None.
    If 'username_or_email' is not associated with any user, return None.
    """
    if username_or_email == '':
        return None
    else:
        return User.query.filter(or_(User.username == username_or_email, User.email == username_or_email)).first()


def get_user_by_reset_token(reset_token):
    """
    Given a string 'reset_token', return the user object associated with that reset token.
    If 'reset_token' is an empty string, return None.
    If 'reset