


class User(UserMixin):

	@property
	def is_authenticated(self):
	    return True
	
	