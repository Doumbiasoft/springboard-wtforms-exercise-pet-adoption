from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField,SelectField,URLField,FileField
from wtforms.validators import InputRequired,Optional,Length,NumberRange,URL,ValidationError
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename

folder_path='static/images/pets/'
file_allowed=['jpg', 'jpeg', 'png']

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name",validators=[InputRequired(),Length(min=4,message='Pet name must to be at least 4 characters!')])
    species = SelectField("Species", choices=[("", "-- --"),("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],validators=[InputRequired()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes = StringField("Notes",validators=[Optional(), Length(min=10)])
    photo_url = StringField("Photo URL",validators=[Optional()])
    photo = FileField('Photo', validators=[Optional(), FileAllowed(file_allowed, 'Images only!')])
    available = BooleanField("Is Available")
  
    def save_photo(self):
        """Function to save photo in static folder."""
        if self.photo.data:
            filename = secure_filename(self.photo.data.filename)
            self.photo.data.save(folder_path + filename)
            return folder_path + filename


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    name = StringField("Pet Name",validators=[InputRequired(),Length(min=4,message='Pet name must to be at least 4 characters!')])
    species = SelectField("Species", choices=[("", "-- --"),("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],validators=[InputRequired()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes = StringField("Notes",validators=[Optional(), Length(min=10)])
    photo_url = StringField("Photo URL",validators=[Optional()])
    photo = FileField('Photo', validators=[Optional(), FileAllowed(file_allowed, 'Images only!')])
    available = BooleanField("Is Available")
  
    def save_photo(self):
        """Function to save photo in static folder."""
        if self.photo.data:
            filename = secure_filename(self.photo.data.filename)
            self.photo.data.save(folder_path + filename)
            return folder_path + filename



