from django.db import models
import os
import uuid


def content_file_name(instance, filename):
    """
    This function prevents that a file is uploaded with an existing name
    """
    
    path = 'product_images'
    generated_id = uuid.uuid4().hex.upper()
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.product_name, generated_id, ext)
    return os.path.join(path, filename)


class Product(models.Model):
    """
    Model definition for the product
    """

    product_name = models.CharField(
        'Product name',
        max_length=50,
    )
    product_description = models.CharField(
        'Product description',
        max_length=200,
    )
    product_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    product_image = models.ImageField(
        'Product image',
        upload_to=content_file_name,
    )

    def __str__(self):
        """
        Unicode representation of the product
        """

        return self.product_name

    def delete(self, *args, **kwargs):
        """
        The file from the media folder also deleted on the
        removal from the database
        """

        self.product_image.delete()
        super().delete(*args, **kwargs)
