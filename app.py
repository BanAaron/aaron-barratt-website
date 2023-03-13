from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# TODO: fix about-me images on desktop
# TODO: 10. General: Probably want to add contact details (mobile/email) next to your socials
# TODO: 11. Projects - Might be worth putting in bigger descriptions - talk about why you wanted to do the project, what you used, what you learnt - that kind of thing. Maybe put in a few images here as well
