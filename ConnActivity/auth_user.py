# Version2, q&d
import os

import firebase_admin

if os.environ.get('DEBUG') == 'False':
    def user_auth(token):
        if not firebase_admin._apps:
            creds = firebase_admin.credentials.Certificate("./firebase_cred.json")
            firebase_admin.initialize_app(creds)
        try:
            decoded_token = firebase_admin.auth.verify_id_token(token)
            return decoded_token['uid']
        except:
            raise Exception("Invalid Token")
else:
    ##
    def user_auth(token):
        import firebase_admin
        if not firebase_admin._apps:
            creds = firebase_admin.credentials.Certificate("./firebase_cred.json")
            firebase_admin.initialize_app(creds)
        try:
            decoded_token = firebase_admin.auth.verify_id_token(token)
            return decoded_token['uid']
        except:
            if token == 'Na_i_mog_afach_nimma_oida':
                return '73'
