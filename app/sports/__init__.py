from flask import Blueprint

# Визначаємо, що коренева папка шаблонів для блюпринта — це 'templates'
sports_bp = Blueprint('sports', __name__, template_folder='templates') 
# ----------------------------------------^^^^^^^^^^^^^^^
# Тобі потрібно прибрати '/sports' звідси.

from . import views