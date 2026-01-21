from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_image_product_back_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='front_image',
            field=models.ImageField(upload_to='products/front/', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='back_image',
            field=models.ImageField(upload_to='products/back/', blank=True, null=True),
        ),
    ]
