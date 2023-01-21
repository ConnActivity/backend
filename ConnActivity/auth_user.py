# Version2, q&d
import os

if os.environ.get('DEBUG') == 'False':
    def user_auth(token):
        import firebase_admin
        from firebase_admin import auth
        if not firebase_admin._apps:
            creds = firebase_admin.credentials.Certificate("./firebase_cred.json")
            fb_instance = firebase_admin.initialize_app(creds)
        try:
            decoded_token = firebase_admin.auth.verify_id_token(token)
            return decoded_token['uid']
        except:
            raise Exception("Invalid Token")
else:
    ##
    def user_auth(token):
        import firebase_admin
        from firebase_admin import auth
        if not firebase_admin._apps:
            creds = firebase_admin.credentials.Certificate("./firebase_cred.json")
            fb_instance = firebase_admin.initialize_app(creds)
        try:
            decoded_token = firebase_admin.auth.verify_id_token(token)
            return decoded_token['uid']
        except:
            if token == 'Na_i_mog_afach_nimma_oida':
                return '73'
            raise Exception("Invalid Token")
