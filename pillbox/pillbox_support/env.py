import os

app_name = 'pillbox'
app_version = '1.0.0'


app_conf_dir = '.' + app_name
app_conf_file = app_name + '.conf'
app_root_dir = app_name


def get_app_conf_path(resource=None):
    cur_user_path = os.path.expanduser('~')
    app_conf_path = os.path.join(cur_user_path, app_conf_dir)
    if not os.path.exists(app_conf_path):
        os.makedirs(app_conf_path)
    if resource:
        return os.path.join(app_conf_path, resource)
    else:
        return app_conf_path


def get_app_root_path(*dir_or_file):
    cur_user_path = os.path.expanduser('~')
    path = os.path.join(cur_user_path, app_root_dir, *dir_or_file)
    path_dir = os.path.dirname(path)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    return path
