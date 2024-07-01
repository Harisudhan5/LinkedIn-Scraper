from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('harisudhans574@gmail.com', '1@AiDataLearning')

# GET a profile
profile = api.get_profile('billy-g')

