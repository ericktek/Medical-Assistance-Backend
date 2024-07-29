from django.conf import settings

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    
)

VISIT = (
    ('physical', 'physical'),
    ('online', 'online'),
    ('instant', 'instant')
)

STATUS = (
    ('active', 'active'),
    ('ongoing', 'ongoing'),
    ('completed', 'completed'),
    ('cancelled', 'cancelled')
)

LEVEL_CHOICES =(
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('S', 'S'),
)
modelling = settings.STATICFILES_DIRS[0] + r'/modelling/model.joblib'
dataset = settings.STATICFILES_DIRS[0] + r'/dataset'
visit_url = settings.VISIT_URL + r'/api/v1/visit/'
sso_url = settings.SSO_URL + r'/api/v1/auth/'
