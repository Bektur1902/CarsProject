import requests
import json
from settings import settings

class Cars:
    type_body = ('седан', 'уневерсал', 'купе', 'хэтчбэк', 'минивэн', 'внедороэник', 'пикап')

    def list_records(self):
        print('Listing records')
        req = requests.get(settings.get_url + settings.URL_, headers=settings.HEADER)
        return req.json()

    def retrieve_record(self, id_):
        """ Get a record by ID. """
        print('Retrieving record...')
        req = requests.get(settings.get_url + f'/{id_}', headers=settings.HEADER)
        return req.json()

    def create_record(self):
        print('Creating record')
        data =   {
            "fields": {
                'mark': input('Enter mark of car: '),
                'model': input('Enter model: '),
                'year': input('Enter year: '),
                'engine': input('Enter engine capacity: '),
                'color': input('Enter color: '),
                'body': input(f'Select type of body {Cars.type_body}: '),
                'mileage': input('Enter mileage: '),
                'price': input('Enter price: ')
            },
            'typecast': True
        }
        req = requests.post(settings.get_url, headers=settings.HEADER, data=json.dumps(data))
        return req.json()

    def update_record(self, id_):
        
        print('Update record:\n')

        data = {'records': [{'id': id_, 'fields': {'mark': input('Car brand: '),
         'model': input('brand model: '),
          'year': int(input('Year: ')),
           'engine': float(input('volume: ')),
            'color': input('Color: '),
            'body': input(f'Select body Type {Cars.type_body}: '),
            'mileage': int(input('mileage: ')),
            'price': float(input('price: '))}}]}
        
        data = json.dumps(data)
        req = requests.patch(settings.get_url, headers=settings.HEADER, data=data)
        return req.json()

    def delete_record(self, id_):
        """ Delete a record by ID. """
        print('Deleting record...')
        req = requests.delete(settings.get_url + f'/{id_}', headers={'Authorization': settings.TOKEN}, data=f'records[]={id_}')
        return req.json()

crud = Cars()
# print(crud.list_records())
# print(crud.retrieve_record('recgNo3dqFMWo4Ppv'))
# print(crud.create_record())
print(crud.update_record('recgNo3dqFMWo4Ppv'))
# print(crud.delete_record('recS67QtTKcEjTLh7'))
# # print(crud.retrieve_record())