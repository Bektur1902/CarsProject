class Settings:

    TOKEN = 'Bearer keyM52bqmPw1u1JHA'
    HEADER = {'Authorization': TOKEN, 'Content-Type': 'application/json'} 
    TABLE_NAME = 'Cars' 
    BASE_ID = 'app8EVJNjSPP0i0ix'

    URL_ = f'?maxRecords=3&view=Grid%20view'


    @property
    def get_url(self):
        """Returns the URL for the API."""
        return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}'

settings = Settings()