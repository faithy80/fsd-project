from django.db import models
from gdstorage.storage import GoogleDriveStorage


# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


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
        storage=gd_storage,
        upload_to='product_images'
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
