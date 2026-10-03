from core.models import User

def test_should_check_password(db) -> None:
    user = User.objects.create_user("A")
    user.set_password("secret")
    assert user.check_password("secret") is True

def test_should_not_check_unusable_password(db) -> None:
    user = User.objects.create_user("A")
    user.set_password("secret")
    user.set_unusable_password()
    assert user.check_password("secret") is False