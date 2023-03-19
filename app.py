from flask import Flask,request,render_template,redirect,url_for,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm,EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] ="azertyqwerty"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECT'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
#app.config['WTF_CSRF_ENABLED'] = False
toolbar = DebugToolbarExtension(app)


with app.app_context():
     connect_db(app)
     db.create_all()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def home():
    pets=Pet.query.filter(Pet.available==True).all()
    pets_not=Pet.query.filter(Pet.available==False).all()
    return render_template('pets/home.html',pets=pets,pets_not=pets_not)

@app.route("/show/<int:pet_id>")
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pets/show.html',pet=pet)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        #data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        #new_pet = Pet(**data)
        if form.photo_url.data and form.photo.data:

            flash(f"You can only provide either a photo_url or a photo!","danger")
            return render_template("pets/add.html", form=form)

        if form.photo_url.data:
            # Handle photo_url input
            filename = form.photo_url.data
            
        elif form.photo.data:
            # Handle file upload
            filename = form.save_photo()

        new_pet =Pet(name=form.name.data, species=form.species.data, age=form.age.data, notes=form.notes.data, photo_url=filename)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added successfully.","success")
        return redirect(url_for('home'))

    else:
        return render_template("pets/add.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        if form.photo_url.data and form.photo.data:

            flash(f"You can only provide either a photo_url or a photo!","danger")
            return render_template("pets/edit.html", form=form, pet=pet)
        
        if form.photo_url.data:
            # Handle photo_url input
            filename = form.photo_url.data
            
        elif form.photo.data:
            # Handle file upload
            filename = form.save_photo()

        pet.name = form.name.data
        pet.age = form.age.data
        pet.species = form.species.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = filename
        db.session.commit()
        flash(f"{pet.name} updated successfully.","success")
        return redirect(url_for('home'))
    else:
        return render_template("pets/edit.html", form=form, pet=pet)

@app.route("/<int:id>/delete")
def delete_pet(id):
    """delete pet."""
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    flash(f"{pet.name} deleted successfully","success")
    return redirect(url_for('home'))

