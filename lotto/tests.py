from django.test import TestCase
from lotto.models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):

    def test_generate(self):
        g = GuessNumbers(name="Test Numbers", text='selected numebers')
        g.generate()
        # g.lottos # -> 6개씩 5 set 총 30개의 리스트의 str
        print(g.update_date)
        print(g.lottos)

        self.assertTrue( len(g.lottos) > 20 )

    
