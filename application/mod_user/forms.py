from wtforms import Form, TextField, PasswordField, SelectField, TextAreaField, validators, ValidationError

class RegistrationForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ], description = "Email")
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ], description = "First Name")
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ], description = "Last Name")
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")
    confirm_password = PasswordField("Confirm Password", description = "Confirm Password")

    def validate_confirm_password(form, field):
        password = form['password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")

class LoginForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address."
    )], description = "Email")
    password = PasswordField("Password", [], description = "Password")

class EmailForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address."
    )], description = "Email")

class RecoverForm(Form):
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")
    confirm_password = PasswordField("Confirm Password", description = "Confirm Password")

    def validate_confirm_password(form, field):
        password = form['password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")

class ChangePasswordForm(Form):
    password = PasswordField("Password", [
        validators.Required(message = "You must enter your current password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")

    new_password = PasswordField("New Password", [
        validators.Required(message = "You must choose a new password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "New Password")
    confirm_password = PasswordField("Confirm New Password", description = "Confirm New Password")

    def validate_confirm_password(form, field):
        password = form['new_password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")


class ApplicationForm(Form):
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ])
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ])
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ])
    school = TextField("School Name", [
        validators.Required(message = "Enter your school's name.")
    ])

    gender = SelectField("Gender", choices = [("Male","Male"), ("Female","Female"), ("NA", "Rather Not Say")])
    has_programmed = SelectField("Never Programmed?", choices = [("Yes", "Yes"), ("No", "No")])
    ethnicity = SelectField("Ethnicity", choices = [("White", "White"), ("African American", "African American"), ("Asian or Pacific Islander", "Asian or Pacific Islander"), ("American Indian or Alaskan Native", "American Indian or Alaskan Native"), ("Multiracial", "Multiracial"), ("Hispanic origin", "Hispanic origin"), ("NA", "Rather Not Say")])
    grade = SelectField("Grade", choices = [("9", "9th"), ("10", "10th"), ("11", "11th"), ("12", "12th")])
    num_hackathons = SelectField("How many hackathons have you attended?", choices = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5+", "5+")])

    github = TextField("Link to your Github Profile?", [validators.optional()])
    linkedin = TextField("Link to your LinkedIn Profile?", [validators.optional()])
    personal_site = TextField("Link to your personal Website?", [validators.optional()])
    other = TextField("Is there something else you want to show us? If so, link it here.", [validators.optional()])

    free_response1 = TextAreaField("What do you hope to learn and accomplish?", [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ])

    free_response2 = TextAreaField("What is something you’re proud of (it doesn’t have to be tech related)?", [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ])

    free_response3 = TextAreaField("Is there anything else you want us to know?", [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ])
