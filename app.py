from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# TODO: add resume to bottom of page as final section
# TODO: make desktop layout a bit nicer
# TODO: 9. General: Seems a bit plain? I would increase the profile picture size significantly and maybe add some more images - after all you want to get them to know you, so make it personal. If you don't want to put too much on the front page, then maybe add a page that is specifically about you and your interests.
# TODO: 10. General: Probably want to add contact details (mobile/email) next to your socials
# TODO: 11. Projects - Might be worth putting in bigger descriptions - talk about why you wanted to do the project, what you used, what you learnt - that kind of thing. Maybe put in a few images here as well
# TODO: 12. Job role too closely matches the background colour, it probably wants to stand out as much if not more than the company names
# TODO: 13. Make "Aaron Barratt" on the home page link to about me page
