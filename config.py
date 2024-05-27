class Config:
    SECRET_KEY = '123secretkey'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@DESKTOP-DJ1UNI3/online_drive?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    PAYU_CLIENT_ID = '300746'
    PAYU_CLIENT_SECRET = '2ee86a66e5d97e3fadc400c9f19b065d'
    PAYU_API_URL = 'https://secure.snd.payu.com'
    PAYU_NOTIFY_URL = 'http://127.0.0.1:5000/notify'
    PAYU_CONTINUE_URL = 'http://127.0.0.1:5000/profile'