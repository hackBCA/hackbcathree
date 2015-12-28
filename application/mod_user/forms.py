from wtforms import Form, TextField, PasswordField, validators, ValidationError

class RegistrationForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."), 
        validators.Email(message = "Invalid email address."
    )])
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name."), 
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ])
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name."), 
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ])
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."), 
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ])
    confirm_password = PasswordField("Confirm Password")

    def validate_confirm_password(form, field):
        password = form['password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")
        
