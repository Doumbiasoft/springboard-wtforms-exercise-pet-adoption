
from models import Pet
from app import app, db

with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    # Add sample pet
    pet1 = Pet(name='Vegeta', species='dog', age=12, notes='', photo_url='http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcQIBOmtSwpL-Ew0d0-IOXIgbA8-q3FLOSYAhjKlI4NJ3Pirj54sGbG94L_GW9mleEmnxDi8F2mgXENFKGE')
    pet2 = Pet(name='Beerus', species='dog', age=5, notes='', photo_url='http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcSobapPy3Vd5bfbFgCGp9GuMbc3aiY71a-4MfBHWKCQ6t33htkw47vXOLcjstGAjsYES_oKSjjBAUES4io')
    pet3 = Pet(name='Naruto', species='cat', age=7, notes='', photo_url='https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-domestic-cat-mjf-1540-382ba2.jpg')


    db.session.add_all([pet1, pet2, pet3])
    db.session.commit()
   



