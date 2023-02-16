from recipes.models import RecipeIngredient
from meals.models import Meal

from django.contrib.auth import get_user_model
from django.db.models import Sum

User = get_user_model()
users = User.objects.all()

queue = Meal.objects.by_user(users[1]).pending().prefetch_related('recipe__recipeingredient')
ids = queue.values_list('recipe__recipeingredient__id', flat=True)
qs = RecipeIngredient.objects.filter(id__in=ids)
data = qs.values("name", "unit").annotate(total=Sum("quantity_as_float"))

for d in data:
    print(d['total'], d['unit'], d['name'])

