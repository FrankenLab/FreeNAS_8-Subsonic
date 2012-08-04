from subprocess import Popen, PIPE
import os
import platform

subsonic_pbi_path = "/usr/pbi/subsonic-" + platform.machine()
subsonic_etc_path = os.path.join(subsonic_pbi_path, "etc")
subsonic_mnt_path = os.path.join(subsonic_pbi_path, "mnt")
subsonic_fcgi_pidfile = "/var/run/subsonic.pid"
subsonic_fcgi_wwwdir = os.path.join(subsonic_pbi_path, "www")
subsonic_control = "/usr/local/etc/rc.d/subsonic"
subsonic_config = os.path.join(subsonic_etc_path, "mt-daapd.conf")
subsonic_icon = os.path.join(subsonic_pbi_path, "default.png")
subsonic_oauth_file = os.path.join(subsonic_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_subsonic_oauth_creds():
    f = open(subsonic_oauth_file)
    lines = f.readlines()
    f.close()

    key = secret = None
    for l in lines:
        l = l.strip()

        if l.startswith("key"):
            pair = l.split("=")
            if len(pair) > 1:
                key = pair[1].strip()

        elif l.startswith("secret"):
            pair = l.split("=")
            if len(pair) > 1:
                secret = pair[1].strip()

    return key, secret


subsonic_advanced_vars = {
    "set_cwd": {
        "type": "checkbox",
        "on": "-a",
        },
    "debuglevel": {
        "type": "textbox",
        "opt": "-d",
        },
    "debug_modules": {
        "type": "textbox",
        "opt": "-D",
        },
    "disable_mdns": {
        "type": "checkbox",
        "on": "-m",
        },
    "non_root_user": {
        "type": "checkbox",
        "on": "-y",
        },
    "ffid": {
        "type": "textbox",
        "opt": "-b",
        },
}
