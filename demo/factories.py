import factory
import factory.fuzzy
from .models import Student


class StudentFactory(factory.django.DjangoModelFactory):
	name = factory.fuzzy.FuzzyText()
	course = factory.fuzzy.FuzzyText()
	college = factory.fuzzy.FuzzyText()
	fees = factory.fuzzy.FuzzyDecimal(low=1000.00)

	class Meta:
		model = Student