import pyotp
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import User


class UserUISerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "dark_mode",
            "show_community_scripts",
            "agent_dblclick_action",
            "default_agent_tbl_tab",
            "client_tree_sort",
            "client_tree_splitter",
            "loading_bar_color",
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "last_login",
        )


class TOTPSetupSerializer(ModelSerializer):

    qr_url = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "totp_key",
            "qr_url",
        )

    def get_qr_url(self, obj):
        return pyotp.totp.TOTP(obj.totp_key).provisioning_uri(
            obj.username, issuer_name="Tactical RMM"
        )
