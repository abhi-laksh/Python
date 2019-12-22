
a = {"Test" :1 , "lorem" : 2}
prefs = {
        'profile.default_content_setting_values.notifications' : 2 ,
        'profile.default_content_settings.popups' : 0,
        "download.prompt_for_download": False,
        **a
        }
print(prefs)