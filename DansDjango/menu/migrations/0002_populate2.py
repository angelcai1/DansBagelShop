from django.db import migrations
from django.utils import timezone

def populate_db(apps, schema_editor):
        Section = apps.get_model('menu', 'Section')
        Option = apps.get_model('menu', 'Option')

        section_one = Section(title="Bagels")
        section_one.save()
        
        section_two = Section(title="Shmeres")
        section_two.save()
        
        section_three = Section(title="Sandwiches")
        section_three.save()
        
        section_four = Section(title="Drinks")
        section_four.save()
        
        option_one = Option(section=section_one, name="plain", price="$2.00", quantity=100)
        option_one.save()
        
        option_two = Option(section=section_one, name="onion", price="$2.00", quantity=100)
        option_two.save()
        
        option_3 = Option(section=section_one, name="cinnamon raisin", price="$2.00", quantity=100)
        option_3.save()
        
        option_4 = Option(section=section_one, name="Sesame", price="$2.00", quantity=100)
        option_4.save()
        
        option_5 = Option(section=section_one, name="Cheesy", price="$2.00", quantity=100)
        option_5.save()
        
        option_6 = Option(section=section_one, name="Pumpernickel", price="$2.00", quantity=100)
        option_6.save()
        
        optionTwo_1 = Option(section=section_two, name="Plain", price="$1.00", quantity=100)
        optionTwo_1.save()
        
        optionTwo_2 = Option(section=section_two, name="Honey Nut", price="$1.00", quantity=100)
        optionTwo_2.save()
        
        optionTwo_3 = Option(section=section_two, name="Strawberry", price="$1.00", quantity=100)
        optionTwo_3.save()
        
        optionTwo_4 = Option(section=section_two, name="French Onion", price="$1.00", quantity=100)
        optionTwo_4.save()
        
        optionThree_1 = Option(section=section_three, name="Bagel + Bacon", price="$1.00", quantity=100)
        optionThree_1.save()
        
        optionThree_2 = Option(section=section_three, name="Bagel + Egg", price="$2.00", quantity=100)
        optionThree_2.save()
        
        optionThree_3 = Option(section=section_three, name="Bagel + Cheese", price="$2.00", quantity=100)
        optionThree_3.save()
        
        optionThree_4 = Option(section=section_three, name="Bagel + Sausage", price="$2.00", quantity=100)
        optionThree_4.save()
        
        optionThree_5 = Option(section=section_three, name="Bagel + Avocado", price="$9.99", quantity=100)
        optionThree_5.save()
        
        optionThree_6 = Option(section=section_three, name="Bagel + Turkey", price="$2.00", quantity=100)
        optionThree_6.save()
        
        optionThree_7 = Option(section=section_three, name="Bagel + Ham", price="$2.00", quantity=100)
        optionThree_7.save()
        
        optionThree_8 = Option(section=section_three, name="Bagel + Spinach", price="$1.00", quantity=100)
        optionThree_8.save()
        
        optionThree_9 = Option(section=section_three, name="Bagel + Tomato", price="$1.00", quantity=100)
        optionThree_9.save()
        
        optionThree_10 = Option(section=section_three, name="Bagel + Lax", price="$9.99", quantity=100)
        optionThree_10.save()
        
        optionFour_1 = Option(section=section_four, name="Coffee", price="$2.00", quantity=100)
        optionFour_1.save()
        
        optionFour_2 = Option(section=section_four, name="Milk", price="$2.00", quantity=100)
        optionFour_2.save()
        
        optionFour_3 = Option(section=section_four, name="Orange Juice", price="$2.00", quantity=100)
        optionFour_3.save()
        
        optionFour_4 = Option(section=section_four, name="Water", price="$1.00", quantity=100)
        optionFour_4.save()
        
        
class Migration(migrations.Migration):
    
    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        # I must add this call to `migrations.RunPython()` myself
        migrations.RunPython(populate_db)
    ]