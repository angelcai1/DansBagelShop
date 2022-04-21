from django.db import migrations
from django.utils import timezone

def populate_db(apps, schema_editor):
        Order = apps.get_model('menu', 'Order')

        order_1 = Order(items="1x Plain Bagel", total="2")
        order_1.save()
        
        order_2 = Order(items="2x Bagel + Cheese", total="4")
        order_2.save()
        
        order_3 = Order(items="1x Bagel + Avocado", total="9.99")
        order_3.save()
        
class Migration(migrations.Migration):
    
    dependencies = [
        ('menu', '0003_order'),
    ]

    operations = [
        # I must add this call to `migrations.RunPython()` myself
        migrations.RunPython(populate_db)
    ]