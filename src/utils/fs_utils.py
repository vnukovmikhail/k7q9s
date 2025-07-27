import sys, os, json, shutil, time, asyncio, random

def Initialize():
    if not os.path.isdir('public'):
        print('creating root')
        os.mkdir('public')
    else:
        print('already exists')

def CreateCollection(name = 'default'):
    try:
        os.mkdir(f'public/{name}')
    except FileExistsError:
        print('already exists')
    
CreateCollection('ho')